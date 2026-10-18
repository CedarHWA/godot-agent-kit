> Source: https://docs.godotengine.org/en/4.7/classes/class_light2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="light2d"></a>

<a id="class-light2d"></a>

# Light2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [DirectionalLight2D](class_directionallight2d.md#class-directionallight2d), [PointLight2D](class_pointlight2d.md#class-pointlight2d)

Casts light in a 2D environment.

<a id="description"></a>

## Description

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).

<a id="tutorials"></a>

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BlendMode](class_light2d.md#enum-light2d-blendmode) | [blend_mode](class_light2d.md#class-light2d-property-blend-mode) | `0` |
| [Color](class_color.md#class-color) | [color](class_light2d.md#class-light2d-property-color) | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool) | [editor_only](class_light2d.md#class-light2d-property-editor-only) | `false` |
| [bool](class_bool.md#class-bool) | [enabled](class_light2d.md#class-light2d-property-enabled) | `true` |
| [float](class_float.md#class-float) | [energy](class_light2d.md#class-light2d-property-energy) | `1.0` |
| [int](class_int.md#class-int) | [range_item_cull_mask](class_light2d.md#class-light2d-property-range-item-cull-mask) | `1` |
| [int](class_int.md#class-int) | [range_layer_max](class_light2d.md#class-light2d-property-range-layer-max) | `0` |
| [int](class_int.md#class-int) | [range_layer_min](class_light2d.md#class-light2d-property-range-layer-min) | `0` |
| [int](class_int.md#class-int) | [range_z_max](class_light2d.md#class-light2d-property-range-z-max) | `1024` |
| [int](class_int.md#class-int) | [range_z_min](class_light2d.md#class-light2d-property-range-z-min) | `-1024` |
| [Color](class_color.md#class-color) | [shadow_color](class_light2d.md#class-light2d-property-shadow-color) | `Color(0, 0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [shadow_enabled](class_light2d.md#class-light2d-property-shadow-enabled) | `false` |
| [ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) | [shadow_filter](class_light2d.md#class-light2d-property-shadow-filter) | `0` |
| [float](class_float.md#class-float) | [shadow_filter_smooth](class_light2d.md#class-light2d-property-shadow-filter-smooth) | `0.0` |
| [int](class_int.md#class-int) | [shadow_item_cull_mask](class_light2d.md#class-light2d-property-shadow-item-cull-mask) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_height](class_light2d.md#class-light2d-method-get-height)() const |
| void | [set_height](class_light2d.md#class-light2d-method-set-height)(height: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-light2d-shadowfilter"></a>

enum **ShadowFilter**: [🔗](class_light2d.md#enum-light2d-shadowfilter)

<a id="class-light2d-constant-shadow-filter-none"></a>

[ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) **SHADOW_FILTER_NONE** = `0`

No filter applies to the shadow map. This provides hard shadow edges and is the fastest to render. See [shadow_filter](class_light2d.md#class-light2d-property-shadow-filter).

<a id="class-light2d-constant-shadow-filter-pcf5"></a>

[ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) **SHADOW_FILTER_PCF5** = `1`

Percentage closer filtering (5 samples) applies to the shadow map. This is slower compared to hard shadow rendering. See [shadow_filter](class_light2d.md#class-light2d-property-shadow-filter).

<a id="class-light2d-constant-shadow-filter-pcf13"></a>

[ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) **SHADOW_FILTER_PCF13** = `2`

Percentage closer filtering (13 samples) applies to the shadow map. This is the slowest shadow filtering mode, and should be used sparingly. See [shadow_filter](class_light2d.md#class-light2d-property-shadow-filter).

---


<a id="enum-light2d-blendmode"></a>

enum **BlendMode**: [🔗](class_light2d.md#enum-light2d-blendmode)

<a id="class-light2d-constant-blend-mode-add"></a>

[BlendMode](class_light2d.md#enum-light2d-blendmode) **BLEND_MODE_ADD** = `0`

Adds the value of pixels corresponding to the Light2D to the values of pixels under it. This is the common behavior of a light.

<a id="class-light2d-constant-blend-mode-sub"></a>

[BlendMode](class_light2d.md#enum-light2d-blendmode) **BLEND_MODE_SUB** = `1`

Subtracts the value of pixels corresponding to the Light2D to the values of pixels under it, resulting in inversed light effect.

<a id="class-light2d-constant-blend-mode-mix"></a>

[BlendMode](class_light2d.md#enum-light2d-blendmode) **BLEND_MODE_MIX** = `2`

Mix the value of pixels corresponding to the Light2D to the values of pixels under it by linear interpolation.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-light2d-property-blend-mode"></a>

[BlendMode](class_light2d.md#enum-light2d-blendmode) **blend_mode** = `0` [🔗](class_light2d.md#class-light2d-property-blend-mode)

- void **set_blend_mode**(value: [BlendMode](class_light2d.md#enum-light2d-blendmode))
- [BlendMode](class_light2d.md#enum-light2d-blendmode) **get_blend_mode**()

The Light2D's blend mode.

---


<a id="class-light2d-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_light2d.md#class-light2d-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The Light2D's [Color](class_color.md#class-color).

---


<a id="class-light2d-property-editor-only"></a>

[bool](class_bool.md#class-bool) **editor_only** = `false` [🔗](class_light2d.md#class-light2d-property-editor-only)

- void **set_editor_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editor_only**()

If `true`, Light2D will only appear when editing the scene.

---


<a id="class-light2d-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `true` [🔗](class_light2d.md#class-light2d-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, Light2D will emit light.

---


<a id="class-light2d-property-energy"></a>

[float](class_float.md#class-float) **energy** = `1.0` [🔗](class_light2d.md#class-light2d-property-energy)

- void **set_energy**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy**()

The Light2D's energy value. The larger the value, the stronger the light.

---


<a id="class-light2d-property-range-item-cull-mask"></a>

[int](class_int.md#class-int) **range_item_cull_mask** = `1` [🔗](class_light2d.md#class-light2d-property-range-item-cull-mask)

- void **set_item_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_cull_mask**()

The layer mask. Only objects with a matching [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask) will be affected by the Light2D. See also [shadow_item_cull_mask](class_light2d.md#class-light2d-property-shadow-item-cull-mask), which affects which objects can cast shadows.

**Note:** [range_item_cull_mask](class_light2d.md#class-light2d-property-range-item-cull-mask) is ignored by [DirectionalLight2D](class_directionallight2d.md#class-directionallight2d), which will always light a 2D node regardless of the 2D node's [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask).

---


<a id="class-light2d-property-range-layer-max"></a>

[int](class_int.md#class-int) **range_layer_max** = `0` [🔗](class_light2d.md#class-light2d-property-range-layer-max)

- void **set_layer_range_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layer_range_max**()

Maximum layer value of objects that are affected by the Light2D.

---


<a id="class-light2d-property-range-layer-min"></a>

[int](class_int.md#class-int) **range_layer_min** = `0` [🔗](class_light2d.md#class-light2d-property-range-layer-min)

- void **set_layer_range_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layer_range_min**()

Minimum layer value of objects that are affected by the Light2D.

---


<a id="class-light2d-property-range-z-max"></a>

[int](class_int.md#class-int) **range_z_max** = `1024` [🔗](class_light2d.md#class-light2d-property-range-z-max)

- void **set_z_range_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_range_max**()

Maximum `z` value of objects that are affected by the Light2D.

---


<a id="class-light2d-property-range-z-min"></a>

[int](class_int.md#class-int) **range_z_min** = `-1024` [🔗](class_light2d.md#class-light2d-property-range-z-min)

- void **set_z_range_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_range_min**()

Minimum `z` value of objects that are affected by the Light2D.

---


<a id="class-light2d-property-shadow-color"></a>

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0)` [🔗](class_light2d.md#class-light2d-property-shadow-color)

- void **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

[Color](class_color.md#class-color) of shadows cast by the Light2D.

---


<a id="class-light2d-property-shadow-enabled"></a>

[bool](class_bool.md#class-bool) **shadow_enabled** = `false` [🔗](class_light2d.md#class-light2d-property-shadow-enabled)

- void **set_shadow_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shadow_enabled**()

If `true`, the Light2D will cast shadows.

---


<a id="class-light2d-property-shadow-filter"></a>

[ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) **shadow_filter** = `0` [🔗](class_light2d.md#class-light2d-property-shadow-filter)

- void **set_shadow_filter**(value: [ShadowFilter](class_light2d.md#enum-light2d-shadowfilter))
- [ShadowFilter](class_light2d.md#enum-light2d-shadowfilter) **get_shadow_filter**()

Shadow filter type.

---


<a id="class-light2d-property-shadow-filter-smooth"></a>

[float](class_float.md#class-float) **shadow_filter_smooth** = `0.0` [🔗](class_light2d.md#class-light2d-property-shadow-filter-smooth)

- void **set_shadow_smooth**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_shadow_smooth**()

Smoothing value for shadows. Higher values will result in softer shadows, at the cost of visible streaks that can appear in shadow rendering. [shadow_filter_smooth](class_light2d.md#class-light2d-property-shadow-filter-smooth) only has an effect if [shadow_filter](class_light2d.md#class-light2d-property-shadow-filter) is [SHADOW_FILTER_PCF5](class_light2d.md#class-light2d-constant-shadow-filter-pcf5) or [SHADOW_FILTER_PCF13](class_light2d.md#class-light2d-constant-shadow-filter-pcf13).

---


<a id="class-light2d-property-shadow-item-cull-mask"></a>

[int](class_int.md#class-int) **shadow_item_cull_mask** = `1` [🔗](class_light2d.md#class-light2d-property-shadow-item-cull-mask)

- void **set_item_shadow_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_shadow_cull_mask**()

The shadow mask. Used with [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) to cast shadows. Only occluders with a matching [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask) will cast shadows. See also [range_item_cull_mask](class_light2d.md#class-light2d-property-range-item-cull-mask), which affects which objects can *receive* the light.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-light2d-method-get-height"></a>

[float](class_float.md#class-float) **get_height**() const [🔗](class_light2d.md#class-light2d-method-get-height)

Returns the light's height, which is used in 2D normal mapping. See [PointLight2D.height](class_pointlight2d.md#class-pointlight2d-property-height) and [DirectionalLight2D.height](class_directionallight2d.md#class-directionallight2d-property-height).

---


<a id="class-light2d-method-set-height"></a>

void **set_height**(height: [float](class_float.md#class-float)) [🔗](class_light2d.md#class-light2d-method-set-height)

Sets the light's height, which is used in 2D normal mapping. See [PointLight2D.height](class_pointlight2d.md#class-pointlight2d-property-height) and [DirectionalLight2D.height](class_directionallight2d.md#class-directionallight2d-property-height).
