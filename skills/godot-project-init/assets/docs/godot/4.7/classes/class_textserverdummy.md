> Source: https://docs.godotengine.org/en/4.7/classes/class_textserverdummy.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="textserverdummy"></a>

<a id="class-textserverdummy"></a>

# TextServerDummy

**Inherits:** [TextServerExtension](class_textserverextension.md#class-textserverextension) **<** [TextServer](class_textserver.md#class-textserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A dummy text server that can't render text or manage fonts.

<a id="description"></a>

## Description

A dummy [TextServer](class_textserver.md#class-textserver) interface that doesn't do anything. Useful for freeing up memory when rendering text is not needed, as text servers are resource-intensive. It can also be used for performance comparisons in complex GUIs to check the impact of text rendering.

A dummy text server is always available at the start of a project. Here's how to access it:

```gdscript
var dummy_text_server = TextServerManager.find_interface("Dummy")
if dummy_text_server != null:
    TextServerManager.set_primary_interface(dummy_text_server)
    # If the other text servers are unneeded, they can be removed:
    for i in TextServerManager.get_interface_count():
        var text_server = TextServerManager.get_interface(i)
        if text_server != dummy_text_server:
            TextServerManager.remove_interface(text_server)
```

The command line argument `--text-driver Dummy` (case-sensitive) can be used to force the "Dummy" [TextServer](class_textserver.md#class-textserver) on any project.
