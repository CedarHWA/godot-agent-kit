> Source: https://docs.godotengine.org/en/4.7/classes/class_node3dgizmo.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="node3dgizmo"></a>

<a id="class-node3dgizmo"></a>

# Node3DGizmo

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo)

Abstract class to expose editor gizmos for [Node3D](class_node3d.md#class-node3d).

<a id="description"></a>

## Description

This abstract class helps connect the [Node3D](class_node3d.md#class-node3d) scene with the editor-specific [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) class.

**Node3DGizmo** by itself has no exposed API, refer to [Node3D.add_gizmo()](class_node3d.md#class-node3d-method-add-gizmo) and pass it an [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) instance.
