> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshader.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshader"></a>

<a id="class-visualshader"></a>

# VisualShader

**Inherits:** [Shader](class_shader.md#class-shader) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A custom shader program with a visual editor.

<a id="description"></a>

## Description

This class provides a graph-like visual editor for creating a [Shader](class_shader.md#class-shader). Although **VisualShader**s do not require coding, they share the same logic with script shaders. They use [VisualShaderNode](class_visualshadernode.md#class-visualshadernode)s that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

<a id="tutorials"></a>

## Tutorials

- [Using VisualShaders](../tutorials/shaders/visual_shaders.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [graph_offset](class_visualshader.md#class-visualshader-property-graph-offset) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_node](class_visualshader.md#class-visualshader-method-add-node)(type: [Type](class_visualshader.md#enum-visualshader-type), node: [VisualShaderNode](class_visualshadernode.md#class-visualshadernode), position: [Vector2](class_vector2.md#class-vector2), id: [int](class_int.md#class-int)) |
| void | [add_varying](class_visualshader.md#class-visualshader-method-add-varying)(name: [String](class_string.md#class-string), mode: [VaryingMode](class_visualshader.md#enum-visualshader-varyingmode), type: [VaryingType](class_visualshader.md#enum-visualshader-varyingtype)) |
| void | [attach_node_to_frame](class_visualshader.md#class-visualshader-method-attach-node-to-frame)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), frame: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [can_connect_nodes](class_visualshader.md#class-visualshader-method-can-connect-nodes)(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [connect_nodes](class_visualshader.md#class-visualshader-method-connect-nodes)(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) |
| void | [connect_nodes_forced](class_visualshader.md#class-visualshader-method-connect-nodes-forced)(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) |
| void | [detach_node_from_frame](class_visualshader.md#class-visualshader-method-detach-node-from-frame)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) |
| void | [disconnect_nodes](class_visualshader.md#class-visualshader-method-disconnect-nodes)(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) |
| [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) | [get_node](class_visualshader.md#class-visualshader-method-get-node)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [get_node_connections](class_visualshader.md#class-visualshader-method-get-node-connections)(type: [Type](class_visualshader.md#enum-visualshader-type)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_node_list](class_visualshader.md#class-visualshader-method-get-node-list)(type: [Type](class_visualshader.md#enum-visualshader-type)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_node_position](class_visualshader.md#class-visualshader-method-get-node-position)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_valid_node_id](class_visualshader.md#class-visualshader-method-get-valid-node-id)(type: [Type](class_visualshader.md#enum-visualshader-type)) const |
| [bool](class_bool.md#class-bool) | [has_varying](class_visualshader.md#class-visualshader-method-has-varying)(name: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [is_node_connection](class_visualshader.md#class-visualshader-method-is-node-connection)(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) const |
| void | [remove_node](class_visualshader.md#class-visualshader-method-remove-node)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) |
| void | [remove_varying](class_visualshader.md#class-visualshader-method-remove-varying)(name: [String](class_string.md#class-string)) |
| void | [replace_node](class_visualshader.md#class-visualshader-method-replace-node)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), new_class: [StringName](class_stringname.md#class-stringname)) |
| void | [set_mode](class_visualshader.md#class-visualshader-method-set-mode)(mode: [Mode](class_shader.md#enum-shader-mode)) |
| void | [set_node_position](class_visualshader.md#class-visualshader-method-set-node-position)(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshader-type"></a>

enum **Type**: [🔗](class_visualshader.md#enum-visualshader-type)

<a id="class-visualshader-constant-type-vertex"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_VERTEX** = `0`

A vertex shader, operating on vertices.

<a id="class-visualshader-constant-type-fragment"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_FRAGMENT** = `1`

A fragment shader, operating on fragments (pixels).

<a id="class-visualshader-constant-type-light"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_LIGHT** = `2`

A shader for light calculations.

<a id="class-visualshader-constant-type-start"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_START** = `3`

A function for the "start" stage of particle shader.

<a id="class-visualshader-constant-type-process"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_PROCESS** = `4`

A function for the "process" stage of particle shader.

<a id="class-visualshader-constant-type-collide"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_COLLIDE** = `5`

A function for the "collide" stage (particle collision handler) of particle shader.

<a id="class-visualshader-constant-type-start-custom"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_START_CUSTOM** = `6`

A function for the "start" stage of particle shader, with customized output.

<a id="class-visualshader-constant-type-process-custom"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_PROCESS_CUSTOM** = `7`

A function for the "process" stage of particle shader, with customized output.

<a id="class-visualshader-constant-type-sky"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_SKY** = `8`

A shader for 3D environment's sky.

<a id="class-visualshader-constant-type-fog"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_FOG** = `9`

A compute shader that runs for each froxel of the volumetric fog map.

<a id="class-visualshader-constant-type-texture-blit"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_TEXTURE_BLIT** = `10`

A shader used to process blit calls to a DrawableTexture.

<a id="class-visualshader-constant-type-max"></a>

[Type](class_visualshader.md#enum-visualshader-type) **TYPE_MAX** = `11`

Represents the size of the [Type](class_visualshader.md#enum-visualshader-type) enum.

---


<a id="enum-visualshader-varyingmode"></a>

enum **VaryingMode**: [🔗](class_visualshader.md#enum-visualshader-varyingmode)

<a id="class-visualshader-constant-varying-mode-vertex-to-frag-light"></a>

[VaryingMode](class_visualshader.md#enum-visualshader-varyingmode) **VARYING_MODE_VERTEX_TO_FRAG_LIGHT** = `0`

Varying is passed from `Vertex` function to `Fragment` and `Light` functions.

<a id="class-visualshader-constant-varying-mode-frag-to-light"></a>

[VaryingMode](class_visualshader.md#enum-visualshader-varyingmode) **VARYING_MODE_FRAG_TO_LIGHT** = `1`

Varying is passed from `Fragment` function to `Light` function.

<a id="class-visualshader-constant-varying-mode-max"></a>

[VaryingMode](class_visualshader.md#enum-visualshader-varyingmode) **VARYING_MODE_MAX** = `2`

Represents the size of the [VaryingMode](class_visualshader.md#enum-visualshader-varyingmode) enum.

---


<a id="enum-visualshader-varyingtype"></a>

enum **VaryingType**: [🔗](class_visualshader.md#enum-visualshader-varyingtype)

<a id="class-visualshader-constant-varying-type-float"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_FLOAT** = `0`

Varying is of type [float](class_float.md#class-float).

<a id="class-visualshader-constant-varying-type-int"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_INT** = `1`

Varying is of type [int](class_int.md#class-int).

<a id="class-visualshader-constant-varying-type-uint"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_UINT** = `2`

Varying is of type unsigned [int](class_int.md#class-int).

<a id="class-visualshader-constant-varying-type-vector-2d"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_VECTOR_2D** = `3`

Varying is of type [Vector2](class_vector2.md#class-vector2).

<a id="class-visualshader-constant-varying-type-vector-3d"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_VECTOR_3D** = `4`

Varying is of type [Vector3](class_vector3.md#class-vector3).

<a id="class-visualshader-constant-varying-type-vector-4d"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_VECTOR_4D** = `5`

Varying is of type [Vector4](class_vector4.md#class-vector4).

<a id="class-visualshader-constant-varying-type-boolean"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_BOOLEAN** = `6`

Varying is of type [bool](class_bool.md#class-bool).

<a id="class-visualshader-constant-varying-type-transform"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_TRANSFORM** = `7`

Varying is of type [Transform3D](class_transform3d.md#class-transform3d).

<a id="class-visualshader-constant-varying-type-max"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **VARYING_TYPE_MAX** = `8`

Represents the size of the [VaryingType](class_visualshader.md#enum-visualshader-varyingtype) enum.

---


<a id="constants"></a>

## Constants

<a id="class-visualshader-constant-node-id-invalid"></a>

**NODE_ID_INVALID** = `-1` [🔗](class_visualshader.md#class-visualshader-constant-node-id-invalid)

Indicates an invalid **VisualShader** node.

<a id="class-visualshader-constant-node-id-output"></a>

**NODE_ID_OUTPUT** = `0` [🔗](class_visualshader.md#class-visualshader-constant-node-id-output)

Indicates an output node of **VisualShader**.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshader-property-graph-offset"></a>

[Vector2](class_vector2.md#class-vector2) **graph_offset** [🔗](class_visualshader.md#class-visualshader-property-graph-offset)

- void **set_graph_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_graph_offset**()

**Deprecated:** This property does nothing and always equals to zero.

Deprecated.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visualshader-method-add-node"></a>

void **add_node**(type: [Type](class_visualshader.md#enum-visualshader-type), node: [VisualShaderNode](class_visualshadernode.md#class-visualshadernode), position: [Vector2](class_vector2.md#class-vector2), id: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-add-node)

Adds the specified `node` to the shader.

---


<a id="class-visualshader-method-add-varying"></a>

void **add_varying**(name: [String](class_string.md#class-string), mode: [VaryingMode](class_visualshader.md#enum-visualshader-varyingmode), type: [VaryingType](class_visualshader.md#enum-visualshader-varyingtype)) [🔗](class_visualshader.md#class-visualshader-method-add-varying)

Adds a new varying value node to the shader.

---


<a id="class-visualshader-method-attach-node-to-frame"></a>

void **attach_node_to_frame**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), frame: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-attach-node-to-frame)

Attaches the given node to the given frame.

---


<a id="class-visualshader-method-can-connect-nodes"></a>

[bool](class_bool.md#class-bool) **can_connect_nodes**(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) const [🔗](class_visualshader.md#class-visualshader-method-can-connect-nodes)

Returns `true` if the specified nodes and ports can be connected together.

---


<a id="class-visualshader-method-connect-nodes"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **connect_nodes**(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-connect-nodes)

Connects the specified nodes and ports.

---


<a id="class-visualshader-method-connect-nodes-forced"></a>

void **connect_nodes_forced**(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-connect-nodes-forced)

Connects the specified nodes and ports, even if they can't be connected. Such connection is invalid and will not function properly.

---


<a id="class-visualshader-method-detach-node-from-frame"></a>

void **detach_node_from_frame**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-detach-node-from-frame)

Detaches the given node from the frame it is attached to.

---


<a id="class-visualshader-method-disconnect-nodes"></a>

void **disconnect_nodes**(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-disconnect-nodes)

Connects the specified nodes and ports.

---


<a id="class-visualshader-method-get-node"></a>

[VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **get_node**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) const [🔗](class_visualshader.md#class-visualshader-method-get-node)

Returns the shader node instance with specified `type` and `id`.

---


<a id="class-visualshader-method-get-node-connections"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_node_connections**(type: [Type](class_visualshader.md#enum-visualshader-type)) const [🔗](class_visualshader.md#class-visualshader-method-get-node-connections)

Returns the list of connected nodes with the specified type.

---


<a id="class-visualshader-method-get-node-list"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_node_list**(type: [Type](class_visualshader.md#enum-visualshader-type)) const [🔗](class_visualshader.md#class-visualshader-method-get-node-list)

Returns the list of all nodes in the shader with the specified type.

---


<a id="class-visualshader-method-get-node-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_node_position**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) const [🔗](class_visualshader.md#class-visualshader-method-get-node-position)

Returns the position of the specified node within the shader graph.

---


<a id="class-visualshader-method-get-valid-node-id"></a>

[int](class_int.md#class-int) **get_valid_node_id**(type: [Type](class_visualshader.md#enum-visualshader-type)) const [🔗](class_visualshader.md#class-visualshader-method-get-valid-node-id)

Returns next valid node ID that can be added to the shader graph.

---


<a id="class-visualshader-method-has-varying"></a>

[bool](class_bool.md#class-bool) **has_varying**(name: [String](class_string.md#class-string)) const [🔗](class_visualshader.md#class-visualshader-method-has-varying)

Returns `true` if the shader has a varying with the given `name`.

---


<a id="class-visualshader-method-is-node-connection"></a>

[bool](class_bool.md#class-bool) **is_node_connection**(type: [Type](class_visualshader.md#enum-visualshader-type), from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) const [🔗](class_visualshader.md#class-visualshader-method-is-node-connection)

Returns `true` if the specified node and port connection exist.

---


<a id="class-visualshader-method-remove-node"></a>

void **remove_node**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int)) [🔗](class_visualshader.md#class-visualshader-method-remove-node)

Removes the specified node from the shader.

---


<a id="class-visualshader-method-remove-varying"></a>

void **remove_varying**(name: [String](class_string.md#class-string)) [🔗](class_visualshader.md#class-visualshader-method-remove-varying)

Removes a varying value node with the given `name`. Prints an error if a node with this name is not found.

---


<a id="class-visualshader-method-replace-node"></a>

void **replace_node**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), new_class: [StringName](class_stringname.md#class-stringname)) [🔗](class_visualshader.md#class-visualshader-method-replace-node)

Replaces the specified node with a node of new class type.

---


<a id="class-visualshader-method-set-mode"></a>

void **set_mode**(mode: [Mode](class_shader.md#enum-shader-mode)) [🔗](class_visualshader.md#class-visualshader-method-set-mode)

Sets the mode of this shader.

---


<a id="class-visualshader-method-set-node-position"></a>

void **set_node_position**(type: [Type](class_visualshader.md#enum-visualshader-type), id: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) [🔗](class_visualshader.md#class-visualshader-method-set-node-position)

Sets the position of the specified node.
