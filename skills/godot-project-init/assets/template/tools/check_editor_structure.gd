extends SceneTree
## Validate the project's declared editor contract with Godot, before any _ready runs.
## This is a structural check, not a replacement for editing trials or visual review.

var _failures: Array[String] = []
var _checks: int = 0


func _initialize() -> void:
	_run.call_deferred()


func _run() -> void:
	var file: String = "res://docs/editor-contract.json"
	for argument: String in OS.get_cmdline_user_args():
		if argument.begins_with("--contract="):
			file = argument.trim_prefix("--contract=")
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(file))
	if not parsed is Dictionary or parsed.get("version", 0) != 1:
		push_error("Editor contract is missing, invalid or unsupported: " + file)
		quit(1)
		return
	var contract: Dictionary = parsed
	_expect(not contract.get("scenes", []).is_empty(), "Contract declares at least one scene")
	for spec: Dictionary in contract.get("scenes", []):
		var scene: PackedScene = load(spec["path"]) as PackedScene
		_expect(scene != null, "Scene loads: " + str(spec["path"]))
		if scene == null:
			continue
		var instance: Node = scene.instantiate()
		_expect(instance != null, "Scene instantiates: " + str(spec["path"]))
		if instance == null:
			continue
		for required: Dictionary in spec.get("nodes", []):
			var node: Node = instance.get_node_or_null(required["path"])
			_expect(
				node != null and node.is_class(required["type"]),
				(
					"Authored %s exists before _ready: %s/%s"
					% [required["type"], spec["path"], required["path"]]
				)
			)
		for property: Dictionary in spec.get("exports", []):
			var node: Node = instance.get_node_or_null(property.get("node", "."))
			var exported: bool = false
			if node != null:
				for info: Dictionary in node.get_property_list():
					if info["name"] == property["property"]:
						exported = bool(int(info["usage"]) & PROPERTY_USAGE_EDITOR)
			_expect(exported, "Inspector property: %s" % property)
		instance.free()
	for path: String in contract.get("resources", []):
		var resource: Resource = load(path)
		_expect(resource != null, "Resource loads with dependencies: " + path)
	if _failures.is_empty():
		print("EDITOR_STRUCTURE_OK: %d declared structure checks" % _checks)
	else:
		for failure: String in _failures:
			push_error(failure)
	quit(0 if _failures.is_empty() else 1)


func _expect(condition: bool, message: String) -> void:
	_checks += 1
	if not condition:
		_failures.append(message)
