> Source: https://docs.godotengine.org/en/4.7/classes/class_cameraserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="cameraserver"></a>

<a id="class-cameraserver"></a>

# CameraServer

**Inherits:** [Object](class_object.md#class-object)

Server keeping track of different cameras accessible in Godot.

<a id="description"></a>

## Description

The **CameraServer** keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no [CameraFeed](class_camerafeed.md#class-camerafeed)s will be available. To get a [CameraFeed](class_camerafeed.md#class-camerafeed) on iOS, enable [EditorExportPlatformIOS.modules/camera](class_editorexportplatformios.md#class-editorexportplatformios-property-modules-camera).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [monitoring_feeds](class_cameraserver.md#class-cameraserver-property-monitoring-feeds) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_feed](class_cameraserver.md#class-cameraserver-method-add-feed)(feed: [CameraFeed](class_camerafeed.md#class-camerafeed)) |
| [Array](class_array.md#class-array)[[CameraFeed](class_camerafeed.md#class-camerafeed)] | [feeds](class_cameraserver.md#class-cameraserver-method-feeds)() |
| [CameraFeed](class_camerafeed.md#class-camerafeed) | [get_feed](class_cameraserver.md#class-cameraserver-method-get-feed)(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_feed_count](class_cameraserver.md#class-cameraserver-method-get-feed-count)() |
| void | [remove_feed](class_cameraserver.md#class-cameraserver-method-remove-feed)(feed: [CameraFeed](class_camerafeed.md#class-camerafeed)) |

---


<a id="signals"></a>

## Signals

<a id="class-cameraserver-signal-camera-feed-added"></a>

**camera_feed_added**(id: [int](class_int.md#class-int)) [🔗](class_cameraserver.md#class-cameraserver-signal-camera-feed-added)

Emitted when a [CameraFeed](class_camerafeed.md#class-camerafeed) is added (e.g. a webcam is plugged in).

---


<a id="class-cameraserver-signal-camera-feed-removed"></a>

**camera_feed_removed**(id: [int](class_int.md#class-int)) [🔗](class_cameraserver.md#class-cameraserver-signal-camera-feed-removed)

Emitted when a [CameraFeed](class_camerafeed.md#class-camerafeed) is removed (e.g. a webcam is unplugged).

---


<a id="class-cameraserver-signal-camera-feeds-updated"></a>

**camera_feeds_updated**() [🔗](class_cameraserver.md#class-cameraserver-signal-camera-feeds-updated)

Emitted when camera feeds are updated.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-cameraserver-feedimage"></a>

enum **FeedImage**: [🔗](class_cameraserver.md#enum-cameraserver-feedimage)

<a id="class-cameraserver-constant-feed-rgba-image"></a>

[FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **FEED_RGBA_IMAGE** = `0`

The RGBA camera image.

<a id="class-cameraserver-constant-feed-ycbcr-image"></a>

[FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **FEED_YCBCR_IMAGE** = `0`

The [YCbCr](https://en.wikipedia.org/wiki/YCbCr) camera image.

<a id="class-cameraserver-constant-feed-y-image"></a>

[FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **FEED_Y_IMAGE** = `0`

The Y component camera image.

<a id="class-cameraserver-constant-feed-cbcr-image"></a>

[FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-cameraserver-property-monitoring-feeds"></a>

[bool](class_bool.md#class-bool) **monitoring_feeds** = `false` [🔗](class_cameraserver.md#class-cameraserver-property-monitoring-feeds)

- void **set_monitoring_feeds**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_monitoring_feeds**()

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you're actively accessing the camera.

**Note:** After setting it to `true`, you can receive updated camera feeds through the [camera_feeds_updated](class_cameraserver.md#class-cameraserver-signal-camera-feeds-updated) signal.

```gdscript
func _ready():
    CameraServer.camera_feeds_updated.connect(_on_camera_feeds_updated)
    CameraServer.monitoring_feeds = true

func _on_camera_feeds_updated():
    var feeds = CameraServer.feeds()
```

```csharp
public override void _Ready()
{
    CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated;
    CameraServer.MonitoringFeeds = true;
}

void OnCameraFeedsUpdated()
{
    var feeds = CameraServer.Feeds();
}
```

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-cameraserver-method-add-feed"></a>

void **add_feed**(feed: [CameraFeed](class_camerafeed.md#class-camerafeed)) [🔗](class_cameraserver.md#class-cameraserver-method-add-feed)

Adds the camera `feed` to the camera server.

---


<a id="class-cameraserver-method-feeds"></a>

[Array](class_array.md#class-array)[[CameraFeed](class_camerafeed.md#class-camerafeed)] **feeds**() [🔗](class_cameraserver.md#class-cameraserver-method-feeds)

Returns an array of [CameraFeed](class_camerafeed.md#class-camerafeed)s.

---


<a id="class-cameraserver-method-get-feed"></a>

[CameraFeed](class_camerafeed.md#class-camerafeed) **get_feed**(index: [int](class_int.md#class-int)) [🔗](class_cameraserver.md#class-cameraserver-method-get-feed)

Returns the [CameraFeed](class_camerafeed.md#class-camerafeed) corresponding to the camera with the given `index`.

---


<a id="class-cameraserver-method-get-feed-count"></a>

[int](class_int.md#class-int) **get_feed_count**() [🔗](class_cameraserver.md#class-cameraserver-method-get-feed-count)

Returns the number of [CameraFeed](class_camerafeed.md#class-camerafeed)s registered.

---


<a id="class-cameraserver-method-remove-feed"></a>

void **remove_feed**(feed: [CameraFeed](class_camerafeed.md#class-camerafeed)) [🔗](class_cameraserver.md#class-cameraserver-method-remove-feed)

Removes the specified camera `feed`.
