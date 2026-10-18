> Source: https://docs.godotengine.org/en/4.7/classes/class_weakref.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="weakref"></a>

<a id="class-weakref"></a>

# WeakRef

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds an [Object](class_object.md#class-object). If the object is [RefCounted](class_refcounted.md#class-refcounted), it doesn't update the reference count.

<a id="description"></a>

## Description

A weakref can hold a [RefCounted](class_refcounted.md#class-refcounted) without contributing to the reference counter. A weakref can be created from an [Object](class_object.md#class-object) using [@GlobalScope.weakref()](class_@globalscope.md#class-globalscope-method-weakref). If this object is not a reference, weakref still works, however, it does not have any effect on the object. Weakrefs are useful in cases where multiple classes have variables that refer to each other. Without weakrefs, using these classes could lead to memory leaks, since both references keep each other from being released. Making part of the variables a weakref can prevent this cyclic dependency, and allows the references to be released.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_ref](class_weakref.md#class-weakref-method-get-ref)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-weakref-method-get-ref"></a>

[Variant](class_variant.md#class-variant) **get_ref**() const [🔗](class_weakref.md#class-weakref-method-get-ref)

Returns the [Object](class_object.md#class-object) this weakref is referring to. Returns `null` if that object no longer exists.
