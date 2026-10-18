> Source: https://docs.godotengine.org/en/4.7/classes/class_javaobject.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="javaobject"></a>

<a id="class-javaobject"></a>

# JavaObject

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents an object from the Java Native Interface.

<a id="description"></a>

## Description

Represents an object from the Java Native Interface. It can be returned from Java methods called on [JavaClass](class_javaclass.md#class-javaclass) or other **JavaObject**s. See [JavaClassWrapper](class_javaclasswrapper.md#class-javaclasswrapper) for an example.

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class-javascriptobject).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [JavaClass](class_javaclass.md#class-javaclass) | [get_java_class](class_javaobject.md#class-javaobject-method-get-java-class)() const |
| [bool](class_bool.md#class-bool) | [has_java_method](class_javaobject.md#class-javaobject-method-has-java-method)(method: [StringName](class_stringname.md#class-stringname)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-javaobject-method-get-java-class"></a>

[JavaClass](class_javaclass.md#class-javaclass) **get_java_class**() const [🔗](class_javaobject.md#class-javaobject-method-get-java-class)

Returns the [JavaClass](class_javaclass.md#class-javaclass) that this object is an instance of.

---


<a id="class-javaobject-method-has-java-method"></a>

[bool](class_bool.md#class-bool) **has_java_method**(method: [StringName](class_stringname.md#class-stringname)) const [🔗](class_javaobject.md#class-javaobject-method-has-java-method)

Returns `true` if the given `method` name exists in the object's Java methods.
