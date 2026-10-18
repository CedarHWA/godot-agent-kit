> Source: https://docs.godotengine.org/en/4.7/classes/class_videostream.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="videostream"></a>

<a id="class-videostream"></a>

# VideoStream

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VideoStreamTheora](class_videostreamtheora.md#class-videostreamtheora)

Base resource for video streams.

<a id="description"></a>

## Description

Base resource type for all video streams. Classes that derive from **VideoStream** can all be used as resource types to play back videos in [VideoStreamPlayer](class_videostreamplayer.md#class-videostreamplayer).

<a id="tutorials"></a>

## Tutorials

- [Playing videos](../tutorials/animation/playing_videos.md)
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [file](class_videostream.md#class-videostream-property-file) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [VideoStreamPlayback](class_videostreamplayback.md#class-videostreamplayback) | [_instantiate_playback](class_videostream.md#class-videostream-private-method-instantiate-playback)() virtual required |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-videostream-property-file"></a>

[String](class_string.md#class-string) **file** = `""` [🔗](class_videostream.md#class-videostream-property-file)

- void **set_file**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_file**()

The video file path or URI that this **VideoStream** resource handles.

For [VideoStreamTheora](class_videostreamtheora.md#class-videostreamtheora), this filename should be an Ogg Theora video file with the `.ogv` extension.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-videostream-private-method-instantiate-playback"></a>

[VideoStreamPlayback](class_videostreamplayback.md#class-videostreamplayback) **_instantiate_playback**() virtual required [🔗](class_videostream.md#class-videostream-private-method-instantiate-playback)

Called when the video starts playing, to initialize and return a subclass of [VideoStreamPlayback](class_videostreamplayback.md#class-videostreamplayback).
