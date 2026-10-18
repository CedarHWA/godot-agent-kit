> Source: https://docs.godotengine.org/en/4.7/classes/class_material.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="material"></a>

<a id="class-material"></a>

# Material

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BlitMaterial](class_blitmaterial.md#class-blitmaterial), [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial), [FogMaterial](class_fogmaterial.md#class-fogmaterial), [PanoramaSkyMaterial](class_panoramaskymaterial.md#class-panoramaskymaterial), [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial), [PhysicalSkyMaterial](class_physicalskymaterial.md#class-physicalskymaterial), [PlaceholderMaterial](class_placeholdermaterial.md#class-placeholdermaterial), [ProceduralSkyMaterial](class_proceduralskymaterial.md#class-proceduralskymaterial), [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)

Virtual base class for applying visual properties to an object, such as color and roughness.

<a id="description"></a>

## Description

**Material** is a base resource used for coloring and shading geometry. All materials inherit from it and almost all [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) derived nodes carry a **Material**. A few flags and parameters are shared between all material types and are configured here.

Importantly, you can inherit from **Material** to create your own custom material type in script or in GDExtension.

<a id="tutorials"></a>

## Tutorials

- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Material](class_material.md#class-material) | [next_pass](class_material.md#class-material-property-next-pass) |
| [int](class_int.md#class-int) | [render_priority](class_material.md#class-material-property-render-priority) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_can_do_next_pass](class_material.md#class-material-private-method-can-do-next-pass)() virtual const |
| [bool](class_bool.md#class-bool) | [_can_use_render_priority](class_material.md#class-material-private-method-can-use-render-priority)() virtual const |
| [Mode](class_shader.md#enum-shader-mode) | [_get_shader_mode](class_material.md#class-material-private-method-get-shader-mode)() virtual required const |
| [RID](class_rid.md#class-rid) | [_get_shader_rid](class_material.md#class-material-private-method-get-shader-rid)() virtual required const |
| [Resource](class_resource.md#class-resource) | [create_placeholder](class_material.md#class-material-method-create-placeholder)() const |
| void | [inspect_native_shader_code](class_material.md#class-material-method-inspect-native-shader-code)() |

---


<a id="constants"></a>

## Constants

<a id="class-material-constant-render-priority-max"></a>

**RENDER_PRIORITY_MAX** = `127` [🔗](class_material.md#class-material-constant-render-priority-max)

Maximum value for the [render_priority](class_material.md#class-material-property-render-priority) parameter.

<a id="class-material-constant-render-priority-min"></a>

**RENDER_PRIORITY_MIN** = `-128` [🔗](class_material.md#class-material-constant-render-priority-min)

Minimum value for the [render_priority](class_material.md#class-material-property-render-priority) parameter.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-material-property-next-pass"></a>

[Material](class_material.md#class-material) **next_pass** [🔗](class_material.md#class-material-property-next-pass)

- void **set_next_pass**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_next_pass**()

Sets the **Material** to be used for the next pass. This renders the object again using a different material.

**Note:** [next_pass](class_material.md#class-material-property-next-pass) materials are not necessarily drawn immediately after the source **Material**. Draw order is determined by material properties, [render_priority](class_material.md#class-material-property-render-priority), and distance to camera.

**Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)s and [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)s with type "Spatial".

---


<a id="class-material-property-render-priority"></a>

[int](class_int.md#class-int) **render_priority** [🔗](class_material.md#class-material-property-render-priority)

- void **set_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_render_priority**()

Sets the render priority for objects in 3D scenes. Higher priority objects will be sorted in front of lower priority objects. In other words, all objects with [render_priority](class_material.md#class-material-property-render-priority) `1` will render on top of all objects with [render_priority](class_material.md#class-material-property-render-priority) `0`.

**Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)s and [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)s with type "Spatial".

**Note:** This will not impact how transparent objects are sorted relative to opaque objects or how dynamic meshes will be sorted relative to other opaque meshes. This is because all transparent objects are drawn after all opaque objects and all dynamic opaque meshes are drawn before other opaque meshes.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-material-private-method-can-do-next-pass"></a>

[bool](class_bool.md#class-bool) **_can_do_next_pass**() virtual const [🔗](class_material.md#class-material-private-method-can-do-next-pass)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if [next_pass](class_material.md#class-material-property-next-pass) should be shown in the editor or not.

---


<a id="class-material-private-method-can-use-render-priority"></a>

[bool](class_bool.md#class-bool) **_can_use_render_priority**() virtual const [🔗](class_material.md#class-material-private-method-can-use-render-priority)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if [render_priority](class_material.md#class-material-property-render-priority) should be shown in the editor or not.

---


<a id="class-material-private-method-get-shader-mode"></a>

[Mode](class_shader.md#enum-shader-mode) **_get_shader_mode**() virtual required const [🔗](class_material.md#class-material-private-method-get-shader-mode)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools.

---


<a id="class-material-private-method-get-shader-rid"></a>

[RID](class_rid.md#class-rid) **_get_shader_rid**() virtual required const [🔗](class_material.md#class-material-private-method-get-shader-rid)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools. Used to access the RID of the **Material**'s [Shader](class_shader.md#class-shader).

---


<a id="class-material-method-create-placeholder"></a>

[Resource](class_resource.md#class-resource) **create_placeholder**() const [🔗](class_material.md#class-material-method-create-placeholder)

Creates a placeholder version of this resource ([PlaceholderMaterial](class_placeholdermaterial.md#class-placeholdermaterial)).

---


<a id="class-material-method-inspect-native-shader-code"></a>

void **inspect_native_shader_code**() [🔗](class_material.md#class-material-method-inspect-native-shader-code)

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Shader.inspect_native_shader_code()](class_shader.md#class-shader-method-inspect-native-shader-code).
