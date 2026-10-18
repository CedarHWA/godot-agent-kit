> Source: https://docs.godotengine.org/en/4.7/classes/class_gdscript.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdscript"></a>

<a id="class-gdscript"></a>

# GDScript

**Inherits:** [Script](class_script.md#class-script) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A script implemented in the GDScript programming language.

<a id="description"></a>

## Description

A script implemented in the GDScript programming language, saved with the `.gd` extension. The script extends the functionality of all objects that instantiate it.

Calling [new()](class_gdscript.md#class-gdscript-method-new) creates a new instance of the script. [Object.set_script()](class_object.md#class-object-method-set-script) extends an existing object, if that object's class matches one of the script's base classes.

If you are looking for GDScript's built-in functions, see [@GDScript](class_@gdscript.md#class-gdscript) instead.

<a id="tutorials"></a>

## Tutorials

- [GDScript documentation index](../tutorials/scripting/gdscript/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [new](class_gdscript.md#class-gdscript-method-new)(...) vararg |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdscript-method-new"></a>

[Variant](class_variant.md#class-variant) **new**(...) vararg [🔗](class_gdscript.md#class-gdscript-method-new)

Returns a new instance of the script.

```gdscript
var MyClass = load("myclass.gd")
var instance = MyClass.new()
print(instance.get_script() == MyClass) # Prints true
```
