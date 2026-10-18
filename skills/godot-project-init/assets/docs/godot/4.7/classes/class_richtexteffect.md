> Source: https://docs.godotengine.org/en/4.7/classes/class_richtexteffect.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="richtexteffect"></a>

<a id="class-richtexteffect"></a>

# RichTextEffect

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A custom effect for a [RichTextLabel](class_richtextlabel.md#class-richtextlabel).

<a id="description"></a>

## Description

A custom effect for a [RichTextLabel](class_richtextlabel.md#class-richtextlabel), which can be loaded in the [RichTextLabel](class_richtextlabel.md#class-richtextlabel) inspector or using [RichTextLabel.install_effect()](class_richtextlabel.md#class-richtextlabel-method-install-effect).

**Note:** For a **RichTextEffect** to be usable, a BBCode tag must be defined as a member variable called `bbcode` in the script.

```gdscript
# The RichTextEffect will be usable like this: `[example]Some text[/example]`
var bbcode = "example"
```

```csharp
// The RichTextEffect will be usable like this: `[example]Some text[/example]`
string bbcode = "example";
```

**Note:** As soon as a [RichTextLabel](class_richtextlabel.md#class-richtextlabel) contains at least one **RichTextEffect**, it will continuously process the effect unless the project is paused. This may impact battery life negatively.

<a id="tutorials"></a>

## Tutorials

- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_process_custom_fx](class_richtexteffect.md#class-richtexteffect-private-method-process-custom-fx)(char_fx: [CharFXTransform](class_charfxtransform.md#class-charfxtransform)) virtual const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-richtexteffect-private-method-process-custom-fx"></a>

[bool](class_bool.md#class-bool) **_process_custom_fx**(char_fx: [CharFXTransform](class_charfxtransform.md#class-charfxtransform)) virtual const [🔗](class_richtexteffect.md#class-richtexteffect-private-method-process-custom-fx)

Override this method to modify properties in `char_fx`. The method must return `true` if the character could be transformed successfully. If the method returns `false`, it will skip transformation to avoid displaying broken text.
