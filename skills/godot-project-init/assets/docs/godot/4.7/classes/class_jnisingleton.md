> Source: https://docs.godotengine.org/en/4.7/classes/class_jnisingleton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="jnisingleton"></a>

<a id="class-jnisingleton"></a>

# JNISingleton

**Inherits:** [Object](class_object.md#class-object)

Singleton that connects the engine with Android plugins to interface with native Android code.

<a id="description"></a>

## Description

The JNISingleton is implemented only in the Android export. It's used to call methods and connect signals from an Android plugin written in Java or Kotlin. Methods and signals can be called and connected to the JNISingleton as if it is a Node. See [Java Native Interface - Wikipedia](https://en.wikipedia.org/wiki/Java_Native_Interface) for more information.

<a id="tutorials"></a>

## Tutorials

- [Creating Android plugins](../tutorials/platform/android/android_plugin.md#doc-android-plugin)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [has_java_method](class_jnisingleton.md#class-jnisingleton-method-has-java-method)(method: [StringName](class_stringname.md#class-stringname)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-jnisingleton-method-has-java-method"></a>

[bool](class_bool.md#class-bool) **has_java_method**(method: [StringName](class_stringname.md#class-stringname)) const [🔗](class_jnisingleton.md#class-jnisingleton-method-has-java-method)

Returns `true` if the given `method` name exists in the JNISingleton's Java methods.
