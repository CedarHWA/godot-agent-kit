> Source: https://docs.godotengine.org/en/4.7/classes/class_lightmapgidata.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="lightmapgidata"></a>

<a id="class-lightmapgidata"></a>

# LightmapGIData

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Contains baked lightmap and dynamic object probe data for [LightmapGI](class_lightmapgi.md#class-lightmapgi).

<a id="description"></a>

## Description

**LightmapGIData** contains baked lightmap and dynamic object probe data for [LightmapGI](class_lightmapgi.md#class-lightmapgi). It is replaced every time lightmaps are baked in [LightmapGI](class_lightmapgi.md#class-lightmapgi).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [TextureLayered](class_texturelayered.md#class-texturelayered) | [light_texture](class_lightmapgidata.md#class-lightmapgidata-property-light-texture) |  |
| [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] | [lightmap_textures](class_lightmapgidata.md#class-lightmapgidata-property-lightmap-textures) | `[]` |
| [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] | [shadowmask_textures](class_lightmapgidata.md#class-lightmapgidata-property-shadowmask-textures) | `[]` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_user](class_lightmapgidata.md#class-lightmapgidata-method-add-user)(path: [NodePath](class_nodepath.md#class-nodepath), uv_scale: [Rect2](class_rect2.md#class-rect2), slice_index: [int](class_int.md#class-int), sub_instance: [int](class_int.md#class-int)) |
| void | [clear_users](class_lightmapgidata.md#class-lightmapgidata-method-clear-users)() |
| [int](class_int.md#class-int) | [get_user_count](class_lightmapgidata.md#class-lightmapgidata-method-get-user-count)() const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_user_path](class_lightmapgidata.md#class-lightmapgidata-method-get-user-path)(user_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_using_spherical_harmonics](class_lightmapgidata.md#class-lightmapgidata-method-is-using-spherical-harmonics)() const |
| void | [set_uses_spherical_harmonics](class_lightmapgidata.md#class-lightmapgidata-method-set-uses-spherical-harmonics)(uses_spherical_harmonics: [bool](class_bool.md#class-bool)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-lightmapgidata-shadowmaskmode"></a>

enum **ShadowmaskMode**: [🔗](class_lightmapgidata.md#enum-lightmapgidata-shadowmaskmode)

<a id="class-lightmapgidata-constant-shadowmask-mode-none"></a>

[ShadowmaskMode](class_lightmapgidata.md#enum-lightmapgidata-shadowmaskmode) **SHADOWMASK_MODE_NONE** = `0`

Shadowmasking is disabled. No shadowmask texture will be created when baking lightmaps. Existing shadowmask textures will be removed during baking.

<a id="class-lightmapgidata-constant-shadowmask-mode-replace"></a>

[ShadowmaskMode](class_lightmapgidata.md#enum-lightmapgidata-shadowmaskmode) **SHADOWMASK_MODE_REPLACE** = `1`

Shadowmasking is enabled. Directional shadows that are outside the [DirectionalLight3D.directional_shadow_max_distance](class_directionallight3d.md#class-directionallight3d-property-directional-shadow-max-distance) will be rendered using the shadowmask texture. Shadows that are inside the range will be rendered using real-time shadows exclusively. This mode allows for more precise real-time shadows up close, without the potential "smearing" effect that can occur when using lightmaps with a high texel size. The downside is that when the camera moves fast, the transition between the real-time light and shadowmask can be obvious. Also, objects that only have shadows baked in the shadowmask (and no real-time shadows) won't display any shadows up close.

<a id="class-lightmapgidata-constant-shadowmask-mode-overlay"></a>

[ShadowmaskMode](class_lightmapgidata.md#enum-lightmapgidata-shadowmaskmode) **SHADOWMASK_MODE_OVERLAY** = `2`

Shadowmasking is enabled. Directional shadows will be rendered with real-time shadows overlaid on top of the shadowmask texture. This mode makes for smoother shadow transitions when the camera moves fast, at the cost of a potential smearing effect for directional shadows that are up close (due to the real-time shadow being mixed with a low-resolution shadowmask). Objects that only have shadows baked in the shadowmask (and no real-time shadows) will keep their shadows up close.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-lightmapgidata-property-light-texture"></a>

[TextureLayered](class_texturelayered.md#class-texturelayered) **light_texture** [🔗](class_lightmapgidata.md#class-lightmapgidata-property-light-texture)

- void **set_light_texture**(value: [TextureLayered](class_texturelayered.md#class-texturelayered))
- [TextureLayered](class_texturelayered.md#class-texturelayered) **get_light_texture**()

**Deprecated:** The lightmap atlas can now contain multiple textures. See [lightmap_textures](class_lightmapgidata.md#class-lightmapgidata-property-lightmap-textures).

The lightmap atlas texture generated by the lightmapper.

---


<a id="class-lightmapgidata-property-lightmap-textures"></a>

[Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] **lightmap_textures** = `[]` [🔗](class_lightmapgidata.md#class-lightmapgidata-property-lightmap-textures)

- void **set_lightmap_textures**(value: [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)])
- [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] **get_lightmap_textures**()

The lightmap atlas textures generated by the lightmapper.

---


<a id="class-lightmapgidata-property-shadowmask-textures"></a>

[Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] **shadowmask_textures** = `[]` [🔗](class_lightmapgidata.md#class-lightmapgidata-property-shadowmask-textures)

- void **set_shadowmask_textures**(value: [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)])
- [Array](class_array.md#class-array)[[TextureLayered](class_texturelayered.md#class-texturelayered)] **get_shadowmask_textures**()

The shadowmask atlas textures generated by the lightmapper.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-lightmapgidata-method-add-user"></a>

void **add_user**(path: [NodePath](class_nodepath.md#class-nodepath), uv_scale: [Rect2](class_rect2.md#class-rect2), slice_index: [int](class_int.md#class-int), sub_instance: [int](class_int.md#class-int)) [🔗](class_lightmapgidata.md#class-lightmapgidata-method-add-user)

Adds an object that is considered baked within this **LightmapGIData**.

---


<a id="class-lightmapgidata-method-clear-users"></a>

void **clear_users**() [🔗](class_lightmapgidata.md#class-lightmapgidata-method-clear-users)

Clear all objects that are considered baked within this **LightmapGIData**.

---


<a id="class-lightmapgidata-method-get-user-count"></a>

[int](class_int.md#class-int) **get_user_count**() const [🔗](class_lightmapgidata.md#class-lightmapgidata-method-get-user-count)

Returns the number of objects that are considered baked within this **LightmapGIData**.

---


<a id="class-lightmapgidata-method-get-user-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_user_path**(user_idx: [int](class_int.md#class-int)) const [🔗](class_lightmapgidata.md#class-lightmapgidata-method-get-user-path)

Returns the [NodePath](class_nodepath.md#class-nodepath) of the baked object at index `user_idx`.

---


<a id="class-lightmapgidata-method-is-using-spherical-harmonics"></a>

[bool](class_bool.md#class-bool) **is_using_spherical_harmonics**() const [🔗](class_lightmapgidata.md#class-lightmapgidata-method-is-using-spherical-harmonics)

If `true`, lightmaps were baked with directional information. See also [LightmapGI.directional](class_lightmapgi.md#class-lightmapgi-property-directional).

---


<a id="class-lightmapgidata-method-set-uses-spherical-harmonics"></a>

void **set_uses_spherical_harmonics**(uses_spherical_harmonics: [bool](class_bool.md#class-bool)) [🔗](class_lightmapgidata.md#class-lightmapgidata-method-set-uses-spherical-harmonics)

If `uses_spherical_harmonics` is `true`, tells the engine to treat the lightmap data as if it was baked with directional information.

**Note:** Changing this value on already baked lightmaps will not cause them to be baked again. This means the material appearance will look incorrect until lightmaps are baked again, in which case the value set here is discarded as the entire **LightmapGIData** resource is replaced by the lightmapper.
