> Source: https://docs.godotengine.org/en/4.7/classes/class_javaclass.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="javaclass"></a>

<a id="class-javaclass"></a>

# JavaClass

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a class from the Java Native Interface.

<a id="description"></a>

## Description

Represents a class from the Java Native Interface. It is returned from [JavaClassWrapper.wrap()](class_javaclasswrapper.md#class-javaclasswrapper-method-wrap).

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class-javascriptobject).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_java_class_name](class_javaclass.md#class-javaclass-method-get-java-class-name)() const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [get_java_method_list](class_javaclass.md#class-javaclass-method-get-java-method-list)() const |
| [JavaClass](class_javaclass.md#class-javaclass) | [get_java_parent_class](class_javaclass.md#class-javaclass-method-get-java-parent-class)() const |
| [bool](class_bool.md#class-bool) | [has_java_method](class_javaclass.md#class-javaclass-method-has-java-method)(method: [StringName](class_stringname.md#class-stringname)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-javaclass-method-get-java-class-name"></a>

[String](class_string.md#class-string) **get_java_class_name**() const [🔗](class_javaclass.md#class-javaclass-method-get-java-class-name)

Returns the Java class name.

---


<a id="class-javaclass-method-get-java-method-list"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_java_method_list**() const [🔗](class_javaclass.md#class-javaclass-method-get-java-method-list)

Returns the object's Java methods and their signatures as an [Array](class_array.md#class-array) of dictionaries, in the same format as [Object.get_method_list()](class_object.md#class-object-method-get-method-list).

---


<a id="class-javaclass-method-get-java-parent-class"></a>

[JavaClass](class_javaclass.md#class-javaclass) **get_java_parent_class**() const [🔗](class_javaclass.md#class-javaclass-method-get-java-parent-class)

Returns a **JavaClass** representing the Java parent class of this class.

---


<a id="class-javaclass-method-has-java-method"></a>

[bool](class_bool.md#class-bool) **has_java_method**(method: [StringName](class_stringname.md#class-stringname)) const [🔗](class_javaclass.md#class-javaclass-method-has-java-method)

Returns `true` if the given `method` name exists in the object's Java methods.
