> Source: https://docs.godotengine.org/en/4.7/classes/class_camerafeed.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="camerafeed"></a>

<a id="class-camerafeed"></a>

# CameraFeed

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A camera feed gives you access to a single physical camera attached to your device.

<a id="description"></a>

## Description

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also [CameraServer](class_cameraserver.md#class-cameraserver).

**Note:** Many cameras will return YCbCr images which are split into two textures and need to be combined in a shader. Godot does this automatically for you if you set the environment to show the camera image in the background.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no **CameraFeed**s will be available. To get a **CameraFeed** on iOS, enable [EditorExportPlatformIOS.modules/camera](class_editorexportplatformios.md#class-editorexportplatformios-property-modules-camera).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [feed_is_active](class_camerafeed.md#class-camerafeed-property-feed-is-active) | `false` |
| [Transform2D](class_transform2d.md#class-transform2d) | [feed_transform](class_camerafeed.md#class-camerafeed-property-feed-transform) | `Transform2D(1, 0, 0, -1, 0, 1)` |
| [Array](class_array.md#class-array) | [formats](class_camerafeed.md#class-camerafeed-property-formats) | `[]` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_activate_feed](class_camerafeed.md#class-camerafeed-private-method-activate-feed)() virtual |
| void | [_deactivate_feed](class_camerafeed.md#class-camerafeed-private-method-deactivate-feed)() virtual |
| [Array](class_array.md#class-array) | [_get_formats](class_camerafeed.md#class-camerafeed-private-method-get-formats)() virtual const |
| [bool](class_bool.md#class-bool) | [_set_format](class_camerafeed.md#class-camerafeed-private-method-set-format)(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary)) virtual |
| [FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) | [get_datatype](class_camerafeed.md#class-camerafeed-method-get-datatype)() const |
| [int](class_int.md#class-int) | [get_id](class_camerafeed.md#class-camerafeed-method-get-id)() const |
| [String](class_string.md#class-string) | [get_name](class_camerafeed.md#class-camerafeed-method-get-name)() const |
| [FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition) | [get_position](class_camerafeed.md#class-camerafeed-method-get-position)() const |
| [int](class_int.md#class-int) | [get_texture_tex_id](class_camerafeed.md#class-camerafeed-method-get-texture-tex-id)(feed_image_type: [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage)) |
| void | [set_external](class_camerafeed.md#class-camerafeed-method-set-external)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [set_format](class_camerafeed.md#class-camerafeed-method-set-format)(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [set_name](class_camerafeed.md#class-camerafeed-method-set-name)(name: [String](class_string.md#class-string)) |
| void | [set_position](class_camerafeed.md#class-camerafeed-method-set-position)(position: [FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition)) |
| void | [set_rgb_image](class_camerafeed.md#class-camerafeed-method-set-rgb-image)(rgb_image: [Image](class_image.md#class-image)) |
| void | [set_ycbcr_image](class_camerafeed.md#class-camerafeed-method-set-ycbcr-image)(ycbcr_image: [Image](class_image.md#class-image)) |
| void | [set_ycbcr_images](class_camerafeed.md#class-camerafeed-method-set-ycbcr-images)(y_image: [Image](class_image.md#class-image), cbcr_image: [Image](class_image.md#class-image)) |

---


<a id="signals"></a>

## Signals

<a id="class-camerafeed-signal-format-changed"></a>

**format_changed**() [🔗](class_camerafeed.md#class-camerafeed-signal-format-changed)

Emitted when the format has changed.

---


<a id="class-camerafeed-signal-frame-changed"></a>

**frame_changed**() [🔗](class_camerafeed.md#class-camerafeed-signal-frame-changed)

Emitted when a new frame is available.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-camerafeed-feeddatatype"></a>

enum **FeedDataType**: [🔗](class_camerafeed.md#enum-camerafeed-feeddatatype)

<a id="class-camerafeed-constant-feed-noimage"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **FEED_NOIMAGE** = `0`

No image set for the feed.

<a id="class-camerafeed-constant-feed-rgb"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **FEED_RGB** = `1`

Feed supplies RGB images.

<a id="class-camerafeed-constant-feed-ycbcr"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.

<a id="class-camerafeed-constant-feed-ycbcr-sep"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and converted to RGB.

<a id="class-camerafeed-constant-feed-external"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **FEED_EXTERNAL** = `4`

Feed supplies external image.

---


<a id="enum-camerafeed-feedposition"></a>

enum **FeedPosition**: [🔗](class_camerafeed.md#enum-camerafeed-feedposition)

<a id="class-camerafeed-constant-feed-unspecified"></a>

[FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition) **FEED_UNSPECIFIED** = `0`

Unspecified position.

<a id="class-camerafeed-constant-feed-front"></a>

[FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition) **FEED_FRONT** = `1`

Camera is mounted at the front of the device.

<a id="class-camerafeed-constant-feed-back"></a>

[FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition) **FEED_BACK** = `2`

Camera is mounted at the back of the device.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-camerafeed-property-feed-is-active"></a>

[bool](class_bool.md#class-bool) **feed_is_active** = `false` [🔗](class_camerafeed.md#class-camerafeed-property-feed-is-active)

- void **set_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_active**()

If `true`, the feed is active.

---


<a id="class-camerafeed-property-feed-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)` [🔗](class_camerafeed.md#class-camerafeed-property-feed-transform)

- void **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The transform applied to the camera's image.

---


<a id="class-camerafeed-property-formats"></a>

[Array](class_array.md#class-array) **formats** = `[]` [🔗](class_camerafeed.md#class-camerafeed-property-formats)

- [Array](class_array.md#class-array) **get_formats**()

Formats supported by the feed. Each entry is a [Dictionary](class_dictionary.md#class-dictionary) describing format parameters.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-camerafeed-private-method-activate-feed"></a>

[bool](class_bool.md#class-bool) **_activate_feed**() virtual [🔗](class_camerafeed.md#class-camerafeed-private-method-activate-feed)

Called when the camera feed is activated.

---


<a id="class-camerafeed-private-method-deactivate-feed"></a>

void **_deactivate_feed**() virtual [🔗](class_camerafeed.md#class-camerafeed-private-method-deactivate-feed)

Called when the camera feed is deactivated.

---


<a id="class-camerafeed-private-method-get-formats"></a>

[Array](class_array.md#class-array) **_get_formats**() virtual const [🔗](class_camerafeed.md#class-camerafeed-private-method-get-formats)

Override this method to define supported formats of the camera feed.

---


<a id="class-camerafeed-private-method-set-format"></a>

[bool](class_bool.md#class-bool) **_set_format**(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary)) virtual [🔗](class_camerafeed.md#class-camerafeed-private-method-set-format)

Override this method to set the format of the camera feed.

---


<a id="class-camerafeed-method-get-datatype"></a>

[FeedDataType](class_camerafeed.md#enum-camerafeed-feeddatatype) **get_datatype**() const [🔗](class_camerafeed.md#class-camerafeed-method-get-datatype)

Returns feed image data type.

---


<a id="class-camerafeed-method-get-id"></a>

[int](class_int.md#class-int) **get_id**() const [🔗](class_camerafeed.md#class-camerafeed-method-get-id)

Returns the unique ID for this feed.

---


<a id="class-camerafeed-method-get-name"></a>

[String](class_string.md#class-string) **get_name**() const [🔗](class_camerafeed.md#class-camerafeed-method-get-name)

Returns the camera's name.

---


<a id="class-camerafeed-method-get-position"></a>

[FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition) **get_position**() const [🔗](class_camerafeed.md#class-camerafeed-method-get-position)

Returns the position of camera on the device.

---


<a id="class-camerafeed-method-get-texture-tex-id"></a>

[int](class_int.md#class-int) **get_texture_tex_id**(feed_image_type: [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage)) [🔗](class_camerafeed.md#class-camerafeed-method-get-texture-tex-id)

Returns the texture backend ID (usable by some external libraries that need a handle to a texture to write data).

---


<a id="class-camerafeed-method-set-external"></a>

void **set_external**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int)) [🔗](class_camerafeed.md#class-camerafeed-method-set-external)

Sets the feed as external feed provided by another library.

---


<a id="class-camerafeed-method-set-format"></a>

[bool](class_bool.md#class-bool) **set_format**(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_camerafeed.md#class-camerafeed-method-set-format)

Sets the feed format parameters for the given `index` in the [formats](class_camerafeed.md#class-camerafeed-property-formats) array. Returns `true` on success. By default, the YUYV encoded stream is transformed to [FEED_RGB](class_camerafeed.md#class-camerafeed-constant-feed-rgb). The YUYV encoded stream output format can be changed by setting `parameters`'s `output` entry to one of the following:

- `"separate"` will result in [FEED_YCBCR_SEP](class_camerafeed.md#class-camerafeed-constant-feed-ycbcr-sep);
- `"grayscale"` will result in desaturated [FEED_RGB](class_camerafeed.md#class-camerafeed-constant-feed-rgb);
- `"copy"` will result in [FEED_YCBCR](class_camerafeed.md#class-camerafeed-constant-feed-ycbcr).

---


<a id="class-camerafeed-method-set-name"></a>

void **set_name**(name: [String](class_string.md#class-string)) [🔗](class_camerafeed.md#class-camerafeed-method-set-name)

Sets the camera's name.

---


<a id="class-camerafeed-method-set-position"></a>

void **set_position**(position: [FeedPosition](class_camerafeed.md#enum-camerafeed-feedposition)) [🔗](class_camerafeed.md#class-camerafeed-method-set-position)

Sets the position of this camera.

---


<a id="class-camerafeed-method-set-rgb-image"></a>

void **set_rgb_image**(rgb_image: [Image](class_image.md#class-image)) [🔗](class_camerafeed.md#class-camerafeed-method-set-rgb-image)

Sets RGB image for this feed.

---


<a id="class-camerafeed-method-set-ycbcr-image"></a>

void **set_ycbcr_image**(ycbcr_image: [Image](class_image.md#class-image)) [🔗](class_camerafeed.md#class-camerafeed-method-set-ycbcr-image)

Sets YCbCr image for this feed.

---


<a id="class-camerafeed-method-set-ycbcr-images"></a>

void **set_ycbcr_images**(y_image: [Image](class_image.md#class-image), cbcr_image: [Image](class_image.md#class-image)) [🔗](class_camerafeed.md#class-camerafeed-method-set-ycbcr-images)

Sets Y and CbCr images for this feed.
