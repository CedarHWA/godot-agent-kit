> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreammicrophone.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreammicrophone"></a>

<a id="class-audiostreammicrophone"></a>

# AudioStreamMicrophone

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plays real-time audio input data.

<a id="description"></a>

## Description

When used directly in an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) node, **AudioStreamMicrophone** plays back microphone input in real-time. This can be used in conjunction with [AudioEffectCapture](class_audioeffectcapture.md#class-audioeffectcapture) to process the data or save it.

**Note:** [ProjectSettings.audio/driver/enable_input](class_projectsettings.md#class-projectsettings-property-audio-driver-enable-input) must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Recording with microphone](../tutorials/audio/recording_with_microphone.md)
- [Audio Mic Record Demo](https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record)
