extends SceneTree
## Exercises the configured main scene through a real SceneTree lifecycle.


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	var main_path: String = ProjectSettings.get_setting("application/run/main_scene", "")
	var packed: PackedScene = load(main_path) as PackedScene
	if packed == null:
		push_error("Main scene cannot be loaded")
		quit(1)
		return
	var scene: Node = packed.instantiate()
	root.add_child(scene)
	await process_frame
	await process_frame
	if not is_instance_valid(scene) or not scene.is_inside_tree():
		push_error("Main scene did not survive initialization")
		quit(1)
		return
	scene.queue_free()
	await process_frame
	print("SMOKE_OK")
	quit(0)
