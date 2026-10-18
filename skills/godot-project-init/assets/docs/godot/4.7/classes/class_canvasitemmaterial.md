> Source: https://docs.godotengine.org/en/4.7/classes/class_canvasitemmaterial.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="canvasitemmaterial"></a>

<a id="class-canvasitemmaterial"></a>

# CanvasItemMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material for [CanvasItem](class_canvasitem.md#class-canvasitem)s.

<a id="description"></a>

## Description

**CanvasItemMaterial**s provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) to more fully customize a material's interactions with a [CanvasItem](class_canvasitem.md#class-canvasitem).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) | [blend_mode](class_canvasitemmaterial.md#class-canvasitemmaterial-property-blend-mode) | `0` |
| [LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) | [light_mode](class_canvasitemmaterial.md#class-canvasitemmaterial-property-light-mode) | `0` |
| [int](class_int.md#class-int) | [particles_anim_h_frames](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-h-frames) |  |
| [bool](class_bool.md#class-bool) | [particles_anim_loop](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-loop) |  |
| [int](class_int.md#class-int) | [particles_anim_v_frames](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-v-frames) |  |
| [bool](class_bool.md#class-bool) | [particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation) | `false` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-canvasitemmaterial-blendmode"></a>

enum **BlendMode**: [🔗](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode)

<a id="class-canvasitemmaterial-constant-blend-mode-mix"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

<a id="class-canvasitemmaterial-constant-blend-mode-add"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **BLEND_MODE_ADD** = `1`

Additive blending mode.

<a id="class-canvasitemmaterial-constant-blend-mode-sub"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

<a id="class-canvasitemmaterial-constant-blend-mode-mul"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

<a id="class-canvasitemmaterial-constant-blend-mode-premult-alpha"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **BLEND_MODE_PREMULT_ALPHA** = `4`

Mix blending mode. Colors are assumed to be premultiplied by the alpha (opacity) value.

---


<a id="enum-canvasitemmaterial-lightmode"></a>

enum **LightMode**: [🔗](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode)

<a id="class-canvasitemmaterial-constant-light-mode-normal"></a>

[LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) **LIGHT_MODE_NORMAL** = `0`

Render the material using both light and non-light sensitive material properties.

<a id="class-canvasitemmaterial-constant-light-mode-unshaded"></a>

[LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) **LIGHT_MODE_UNSHADED** = `1`

Render the material as if there were no light.

<a id="class-canvasitemmaterial-constant-light-mode-light-only"></a>

[LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) **LIGHT_MODE_LIGHT_ONLY** = `2`

Render the material as if there were only light.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-canvasitemmaterial-property-blend-mode"></a>

[BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **blend_mode** = `0` [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-blend-mode)

- void **set_blend_mode**(value: [BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode))
- [BlendMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-blendmode) **get_blend_mode**()

The manner in which a material's rendering is applied to underlying textures.

---


<a id="class-canvasitemmaterial-property-light-mode"></a>

[LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) **light_mode** = `0` [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-light-mode)

- void **set_light_mode**(value: [LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode))
- [LightMode](class_canvasitemmaterial.md#enum-canvasitemmaterial-lightmode) **get_light_mode**()

The manner in which material reacts to lighting.

---


<a id="class-canvasitemmaterial-property-particles-anim-h-frames"></a>

[int](class_int.md#class-int) **particles_anim_h_frames** [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-h-frames)

- void **set_particles_anim_h_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_particles_anim_h_frames**()

The number of columns in the spritesheet assigned as [Texture2D](class_texture2d.md#class-texture2d) for a [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d).

**Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation) is `true`.

---


<a id="class-canvasitemmaterial-property-particles-anim-loop"></a>

[bool](class_bool.md#class-bool) **particles_anim_loop** [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-loop)

- void **set_particles_anim_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particles_anim_loop**()

If `true`, the particles animation will loop.

**Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation) is `true`.

---


<a id="class-canvasitemmaterial-property-particles-anim-v-frames"></a>

[int](class_int.md#class-int) **particles_anim_v_frames** [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-v-frames)

- void **set_particles_anim_v_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_particles_anim_v_frames**()

The number of rows in the spritesheet assigned as [Texture2D](class_texture2d.md#class-texture2d) for a [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d).

**Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation) is `true`.

---


<a id="class-canvasitemmaterial-property-particles-animation"></a>

[bool](class_bool.md#class-bool) **particles_animation** = `false` [🔗](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation)

- void **set_particles_animation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particles_animation**()

If `true`, enable spritesheet-based animation features when assigned to [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) and [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d) nodes. The [ParticleProcessMaterial.anim_speed_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-max) or [CPUParticles2D.anim_speed_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-max) should also be set to a positive value for the animation to play.

This property (and other `particles_anim_*` properties that depend on it) has no effect on other types of nodes.
