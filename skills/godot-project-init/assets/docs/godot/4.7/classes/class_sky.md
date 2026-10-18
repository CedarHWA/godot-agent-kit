> Source: https://docs.godotengine.org/en/4.7/classes/class_sky.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="sky"></a>

<a id="class-sky"></a>

# Sky

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Defines a 3D environment's background by using a [Material](class_material.md#class-material).

<a id="description"></a>

## Description

The **Sky** class uses a [Material](class_material.md#class-material) to render a 3D environment's background and the light it emits by updating the reflection/radiance cubemaps.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ProcessMode](class_sky.md#enum-sky-processmode) | [process_mode](class_sky.md#class-sky-property-process-mode) | `0` |
| [RadianceSize](class_sky.md#enum-sky-radiancesize) | [radiance_size](class_sky.md#class-sky-property-radiance-size) | `3` |
| [Material](class_material.md#class-material) | [sky_material](class_sky.md#class-sky-property-sky-material) |  |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-sky-radiancesize"></a>

enum **RadianceSize**: [🔗](class_sky.md#enum-sky-radiancesize)

<a id="class-sky-constant-radiance-size-32"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_32** = `0`

Radiance texture size is 32×32 pixels.

<a id="class-sky-constant-radiance-size-64"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_64** = `1`

Radiance texture size is 64×64 pixels.

<a id="class-sky-constant-radiance-size-128"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_128** = `2`

Radiance texture size is 128×128 pixels.

<a id="class-sky-constant-radiance-size-256"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_256** = `3`

Radiance texture size is 256×256 pixels.

<a id="class-sky-constant-radiance-size-512"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_512** = `4`

Radiance texture size is 512×512 pixels.

<a id="class-sky-constant-radiance-size-1024"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_1024** = `5`

Radiance texture size is 1024×1024 pixels.

<a id="class-sky-constant-radiance-size-2048"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_2048** = `6`

Radiance texture size is 2048×2048 pixels.

<a id="class-sky-constant-radiance-size-max"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **RADIANCE_SIZE_MAX** = `7`

Represents the size of the [RadianceSize](class_sky.md#enum-sky-radiancesize) enum.

---


<a id="enum-sky-processmode"></a>

enum **ProcessMode**: [🔗](class_sky.md#enum-sky-processmode)

<a id="class-sky-constant-process-mode-automatic"></a>

[ProcessMode](class_sky.md#enum-sky-processmode) **PROCESS_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky shader. If your shader uses `TIME` or `POSITION`, this will use [PROCESS_MODE_REALTIME](class_sky.md#class-sky-constant-process-mode-realtime). If your shader uses any of the `LIGHT_*` variables or any custom uniforms, this uses [PROCESS_MODE_INCREMENTAL](class_sky.md#class-sky-constant-process-mode-incremental). Otherwise, this defaults to [PROCESS_MODE_QUALITY](class_sky.md#class-sky-constant-process-mode-quality).

<a id="class-sky-constant-process-mode-quality"></a>

[ProcessMode](class_sky.md#enum-sky-processmode) **PROCESS_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality than [PROCESS_MODE_REALTIME](class_sky.md#class-sky-constant-process-mode-realtime) but takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasing [ProjectSettings.rendering/reflections/sky_reflections/ggx_samples](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-ggx-samples).

<a id="class-sky-constant-process-mode-incremental"></a>

[ProcessMode](class_sky.md#enum-sky-processmode) **PROCESS_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance map as [PROCESS_MODE_QUALITY](class_sky.md#class-sky-constant-process-mode-quality), but updates over several frames. The number of frames is determined by [ProjectSettings.rendering/reflections/sky_reflections/roughness_layers](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-roughness-layers). Use this when you need highest quality radiance maps, but have a sky that updates slowly.

<a id="class-sky-constant-process-mode-realtime"></a>

[ProcessMode](class_sky.md#enum-sky-processmode) **PROCESS_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning on [ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-fast-filter-high-quality).

**Note:** The fast filtering algorithm is limited to 256×256 cubemaps, so [radiance_size](class_sky.md#class-sky-property-radiance-size) must be set to [RADIANCE_SIZE_256](class_sky.md#class-sky-constant-radiance-size-256). Otherwise, a warning is printed and the overridden radiance size is ignored.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-sky-property-process-mode"></a>

[ProcessMode](class_sky.md#enum-sky-processmode) **process_mode** = `0` [🔗](class_sky.md#class-sky-property-process-mode)

- void **set_process_mode**(value: [ProcessMode](class_sky.md#enum-sky-processmode))
- [ProcessMode](class_sky.md#enum-sky-processmode) **get_process_mode**()

The method for generating the radiance map from the sky. The radiance map is a cubemap with increasingly blurry versions of the sky corresponding to different levels of roughness. Radiance maps can be expensive to calculate.

---


<a id="class-sky-property-radiance-size"></a>

[RadianceSize](class_sky.md#enum-sky-radiancesize) **radiance_size** = `3` [🔗](class_sky.md#class-sky-property-radiance-size)

- void **set_radiance_size**(value: [RadianceSize](class_sky.md#enum-sky-radiancesize))
- [RadianceSize](class_sky.md#enum-sky-radiancesize) **get_radiance_size**()

The **Sky**'s radiance map size. The higher the radiance map size, the more detailed the lighting from the **Sky** will be.

**Note:** Some hardware will have trouble with higher radiance sizes, especially [RADIANCE_SIZE_512](class_sky.md#class-sky-constant-radiance-size-512) and above. Only use such high values on high-end hardware.

---


<a id="class-sky-property-sky-material"></a>

[Material](class_material.md#class-material) **sky_material** [🔗](class_sky.md#class-sky-property-sky-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

[Material](class_material.md#class-material) used to draw the background. Can be [PanoramaSkyMaterial](class_panoramaskymaterial.md#class-panoramaskymaterial), [ProceduralSkyMaterial](class_proceduralskymaterial.md#class-proceduralskymaterial), [PhysicalSkyMaterial](class_physicalskymaterial.md#class-physicalskymaterial), or even a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) if you want to use your own custom shader.
