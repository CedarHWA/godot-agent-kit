> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrframesynthesisextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrframesynthesisextension"></a>

<a id="class-openxrframesynthesisextension"></a>

# OpenXRFrameSynthesisExtension

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

The OpenXR Frame synthesis extension allows for advanced reprojection at low(er) framerates.

<a id="description"></a>

## Description

This class implements the [OpenXR Frame synthesis extension](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_frame_synthesis). When enabled in the project settings and supported by the XR runtime in use, frame synthesis uses advanced reprojection techniques to inject additional frames so that your XR experience hits the full frame rate of the device.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [enabled](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-property-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [relax_frame_interval](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-property-relax-frame-interval) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_available](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-method-is-available)() const |
| void | [skip_next_frame](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-method-skip-next-frame)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrframesynthesisextension-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `false` [🔗](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

Enable frame synthesis. When `true` motion vector and depth data is provided to the XR runtime.

---


<a id="class-openxrframesynthesisextension-property-relax-frame-interval"></a>

[bool](class_bool.md#class-bool) **relax_frame_interval** = `false` [🔗](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-property-relax-frame-interval)

- void **set_relax_frame_interval**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_relax_frame_interval**()

If `true` this informs the XR runtime we will be providing frames at a greatly reduced rate. Enable this when you expect your application to run at low framerates and wish to inject multiple reprojected frames.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrframesynthesisextension-method-is-available"></a>

[bool](class_bool.md#class-bool) **is_available**() const [🔗](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-method-is-available)

Returns `true` if frame synthesis is enabled in the project settings and the current XR runtime supports frame synthesis. The value returned will only be valid once OpenXR has been initialized.

---


<a id="class-openxrframesynthesisextension-method-skip-next-frame"></a>

void **skip_next_frame**() [🔗](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension-method-skip-next-frame)

Queues the next frame to be skipped when supplying motion vector and depth data. Call this after teleporting your player or a similar action has moved the player to prevent incorrect reprojection results due to this movement.
