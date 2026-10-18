## Maintainer probes: copy this directory into an isolated project before running.
# Repeated load is intentional: this probe verifies shared cache identity.
# gdlint: disable=duplicated-load
extends SceneTree

const ProbeConfig = preload("probe_config.gd")
const ProbeNode = preload("probe_node.gd")

var _checks: int = 0
var _failures: int = 0


func _init() -> void:
	_run.call_deferred()


func _check(condition: bool, label: String) -> void:
	_checks += 1
	if not condition:
		_failures += 1
		push_error(label)
	else:
		print("PASS: ", label)


func _run() -> void:
	_test_packing()
	_test_resources()
	await _test_lifecycle()
	print("SEMANTICS_RESULT checks=%d failures=%d" % [_checks, _failures])
	if _failures == 0:
		print("SKILL_SEMANTICS_OK")
	quit(1 if _failures else 0)


func _test_packing() -> void:
	var author := Node.new()
	author.name = "Author"
	var child := Node.new()
	child.name = "EditableChild"
	author.add_child(child)
	var packed := PackedScene.new()
	_check(packed.pack(author) == OK, "packing can succeed without child ownership")
	var missing := packed.instantiate()
	_check(not missing.has_node("EditableChild"), "unowned child is absent after instantiation")
	missing.free()
	child.owner = author
	_check(packed.pack(author) == OK, "pack owned editable child")
	_check(ResourceSaver.save(packed, "user://owned.tscn") == OK, "save owned scene")
	var restored := (
		ResourceLoader.load("user://owned.tscn", "PackedScene", ResourceLoader.CACHE_MODE_IGNORE)
		as PackedScene
	)
	var instance := restored.instantiate()
	_check(instance.has_node("EditableChild"), "owned child survives disk round trip")
	instance.free()
	author.free()


func _test_resources() -> void:
	var definition := ProbeConfig.new()
	_check(not definition.has_method("make_unique"), "Resource has no make_unique instance API")
	_check(
		ResourceSaver.save(definition, "user://definition.tres") == OK, "save baseline definition"
	)
	var first := load("user://definition.tres") as Resource
	var second := load("user://definition.tres") as Resource
	_check(first == second, "same path shares cached definition")
	first.set("amount", 5)
	_check(second.get("amount") == 5, "memory mutation affects other references")
	var disk := ResourceLoader.load(
		"user://definition.tres", "Resource", ResourceLoader.CACHE_MODE_IGNORE
	)
	_check(disk.get("amount") == 17, "memory assignment does not implicitly save to disk")
	var aggregate := ProbeConfig.new()
	aggregate.entries.append(first)
	var shallow := aggregate.duplicate()
	var deep := aggregate.duplicate(true)
	var all_copies := aggregate.duplicate_deep(Resource.DEEP_DUPLICATE_ALL)
	_check(shallow.get("entries")[0] == first, "shallow copy keeps nested reference")
	_check(deep.get("entries")[0] == first, "default deep copy retains external resource")
	_check(all_copies.get("entries")[0] != first, "explicit all mode duplicates external resource")
	all_copies.get("entries")[0].set("amount", 99)
	_check(first.get("amount") == 5, "deep all mutation leaves original independent")
	var scene_root := ProbeNode.new()
	scene_root.config = ProbeConfig.new()
	scene_root.config.resource_local_to_scene = true
	var packed := PackedScene.new()
	_check(packed.pack(scene_root) == OK, "pack scene-local config")
	var instance_a := packed.instantiate()
	var instance_b := packed.instantiate()
	instance_a.get("config").set("amount", 4)
	_check(
		instance_b.get("config").get("amount") == 17, "local config independent per scene instance"
	)
	instance_a.free()
	instance_b.free()
	scene_root.free()


func _test_lifecycle() -> void:
	var emitter := ProbeNode.new()
	var receiver := ProbeNode.new()
	root.add_child(emitter)
	root.add_child(receiver)
	await process_frame
	emitter.happened.connect(receiver.observe)
	root.remove_child(receiver)
	emitter.happened.emit()
	_check(receiver.observed_count == 1, "leaving tree does not destroy subscription")
	root.add_child(receiver)
	_check(receiver.ready_count == 1, "ready is not repeated on normal re-entry")
	receiver.free()
	_check(
		emitter.happened.get_connections().is_empty(), "free clears normal object-method connection"
	)
	var once := ProbeNode.new()
	emitter.happened.connect(once.observe, CONNECT_ONE_SHOT)
	_check(
		emitter.happened.is_connected(once.observe), "one-shot remains connected before emission"
	)
	emitter.happened.emit()
	emitter.happened.emit()
	_check(once.observed_count == 1, "one-shot callback runs once after emission")
	_check(
		not emitter.happened.is_connected(once.observe),
		"one-shot removes connection after emission"
	)
	once.free()
	emitter.queue_free()
	await process_frame
