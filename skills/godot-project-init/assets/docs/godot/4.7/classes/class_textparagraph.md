> Source: https://docs.godotengine.org/en/4.7/classes/class_textparagraph.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="textparagraph"></a>

<a id="class-textparagraph"></a>

# TextParagraph

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a paragraph of text.

<a id="description"></a>

## Description

Abstraction over [TextServer](class_textserver.md#class-textserver) for handling a single paragraph of text.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | [alignment](class_textparagraph.md#class-textparagraph-property-alignment) | `0` |
| BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] | [break_flags](class_textparagraph.md#class-textparagraph-property-break-flags) | `3` |
| [String](class_string.md#class-string) | [custom_punctuation](class_textparagraph.md#class-textparagraph-property-custom-punctuation) | `""` |
| [Direction](class_textserver.md#enum-textserver-direction) | [direction](class_textparagraph.md#class-textparagraph-property-direction) | `0` |
| [String](class_string.md#class-string) | [ellipsis_char](class_textparagraph.md#class-textparagraph-property-ellipsis-char) | `"…"` |
| BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] | [justification_flags](class_textparagraph.md#class-textparagraph-property-justification-flags) | `163` |
| [float](class_float.md#class-float) | [line_spacing](class_textparagraph.md#class-textparagraph-property-line-spacing) | `0.0` |
| [int](class_int.md#class-int) | [max_lines_visible](class_textparagraph.md#class-textparagraph-property-max-lines-visible) | `-1` |
| [Orientation](class_textserver.md#enum-textserver-orientation) | [orientation](class_textparagraph.md#class-textparagraph-property-orientation) | `0` |
| [bool](class_bool.md#class-bool) | [preserve_control](class_textparagraph.md#class-textparagraph-property-preserve-control) | `false` |
| [bool](class_bool.md#class-bool) | [preserve_invalid](class_textparagraph.md#class-textparagraph-property-preserve-invalid) | `true` |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) | [text_overrun_behavior](class_textparagraph.md#class-textparagraph-property-text-overrun-behavior) | `0` |
| [float](class_float.md#class-float) | [width](class_textparagraph.md#class-textparagraph-property-width) | `-1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [add_object](class_textparagraph.md#class-textparagraph-method-add-object)(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0) |
| [bool](class_bool.md#class-bool) | [add_string](class_textparagraph.md#class-textparagraph-method-add-string)(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null) |
| void | [clear](class_textparagraph.md#class-textparagraph-method-clear)() |
| void | [clear_dropcap](class_textparagraph.md#class-textparagraph-method-clear-dropcap)() |
| void | [draw](class_textparagraph.md#class-textparagraph-method-draw)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_dropcap](class_textparagraph.md#class-textparagraph-method-draw-dropcap)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_dropcap_outline](class_textparagraph.md#class-textparagraph-method-draw-dropcap-outline)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_line](class_textparagraph.md#class-textparagraph-method-draw-line)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_line_outline](class_textparagraph.md#class-textparagraph-method-draw-line-outline)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_outline](class_textparagraph.md#class-textparagraph-method-draw-outline)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| [TextParagraph](class_textparagraph.md#class-textparagraph) | [duplicate](class_textparagraph.md#class-textparagraph-method-duplicate)() const |
| [int](class_int.md#class-int) | [get_dropcap_lines](class_textparagraph.md#class-textparagraph-method-get-dropcap-lines)() const |
| [RID](class_rid.md#class-rid) | [get_dropcap_rid](class_textparagraph.md#class-textparagraph-method-get-dropcap-rid)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_dropcap_size](class_textparagraph.md#class-textparagraph-method-get-dropcap-size)() const |
| [Direction](class_textserver.md#enum-textserver-direction) | [get_inferred_direction](class_textparagraph.md#class-textparagraph-method-get-inferred-direction)() const |
| [float](class_float.md#class-float) | [get_line_ascent](class_textparagraph.md#class-textparagraph-method-get-line-ascent)(line: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_line_count](class_textparagraph.md#class-textparagraph-method-get-line-count)() const |
| [float](class_float.md#class-float) | [get_line_descent](class_textparagraph.md#class-textparagraph-method-get-line-descent)(line: [int](class_int.md#class-int)) const |
| [Rect2](class_rect2.md#class-rect2) | [get_line_object_rect](class_textparagraph.md#class-textparagraph-method-get-line-object-rect)(line: [int](class_int.md#class-int), key: [Variant](class_variant.md#class-variant)) const |
| [Array](class_array.md#class-array) | [get_line_objects](class_textparagraph.md#class-textparagraph-method-get-line-objects)(line: [int](class_int.md#class-int)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_line_range](class_textparagraph.md#class-textparagraph-method-get-line-range)(line: [int](class_int.md#class-int)) const |
| [RID](class_rid.md#class-rid) | [get_line_rid](class_textparagraph.md#class-textparagraph-method-get-line-rid)(line: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_line_size](class_textparagraph.md#class-textparagraph-method-get-line-size)(line: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_line_underline_position](class_textparagraph.md#class-textparagraph-method-get-line-underline-position)(line: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_line_underline_thickness](class_textparagraph.md#class-textparagraph-method-get-line-underline-thickness)(line: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_line_width](class_textparagraph.md#class-textparagraph-method-get-line-width)(line: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_non_wrapped_size](class_textparagraph.md#class-textparagraph-method-get-non-wrapped-size)() const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_range](class_textparagraph.md#class-textparagraph-method-get-range)() const |
| [RID](class_rid.md#class-rid) | [get_rid](class_textparagraph.md#class-textparagraph-method-get-rid)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_size](class_textparagraph.md#class-textparagraph-method-get-size)() const |
| [bool](class_bool.md#class-bool) | [has_object](class_textparagraph.md#class-textparagraph-method-has-object)(key: [Variant](class_variant.md#class-variant)) const |
| [int](class_int.md#class-int) | [hit_test](class_textparagraph.md#class-textparagraph-method-hit-test)(coords: [Vector2](class_vector2.md#class-vector2)) const |
| [bool](class_bool.md#class-bool) | [resize_object](class_textparagraph.md#class-textparagraph-method-resize-object)(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0) |
| void | [set_bidi_override](class_textparagraph.md#class-textparagraph-method-set-bidi-override)(override: [Array](class_array.md#class-array)) |
| [bool](class_bool.md#class-bool) | [set_dropcap](class_textparagraph.md#class-textparagraph-method-set-dropcap)(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class-string) = "") |
| void | [tab_align](class_textparagraph.md#class-textparagraph-method-tab-align)(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-textparagraph-property-alignment"></a>

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0` [🔗](class_textparagraph.md#class-textparagraph-property-alignment)

- void **set_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_alignment**()

Paragraph horizontal alignment.

---


<a id="class-textparagraph-property-break-flags"></a>

BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **break_flags** = `3` [🔗](class_textparagraph.md#class-textparagraph-property-break-flags)

- void **set_break_flags**(value: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_break_flags**()

Line breaking rules. For more info see [TextServer](class_textserver.md#class-textserver).

---


<a id="class-textparagraph-property-custom-punctuation"></a>

[String](class_string.md#class-string) **custom_punctuation** = `""` [🔗](class_textparagraph.md#class-textparagraph-property-custom-punctuation)

- void **set_custom_punctuation**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_custom_punctuation**()

Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---


<a id="class-textparagraph-property-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **direction** = `0` [🔗](class_textparagraph.md#class-textparagraph-property-direction)

- void **set_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_direction**()

Text writing direction.

---


<a id="class-textparagraph-property-ellipsis-char"></a>

[String](class_string.md#class-string) **ellipsis_char** = `"…"` [🔗](class_textparagraph.md#class-textparagraph-property-ellipsis-char)

- void **set_ellipsis_char**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ellipsis_char**()

Ellipsis character used for text clipping.

---


<a id="class-textparagraph-property-justification-flags"></a>

BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163` [🔗](class_textparagraph.md#class-textparagraph-property-justification-flags)

- void **set_justification_flags**(value: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---


<a id="class-textparagraph-property-line-spacing"></a>

[float](class_float.md#class-float) **line_spacing** = `0.0` [🔗](class_textparagraph.md#class-textparagraph-property-line-spacing)

- void **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---


<a id="class-textparagraph-property-max-lines-visible"></a>

[int](class_int.md#class-int) **max_lines_visible** = `-1` [🔗](class_textparagraph.md#class-textparagraph-property-max-lines-visible)

- void **set_max_lines_visible**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_lines_visible**()

Limits the lines of text shown.

---


<a id="class-textparagraph-property-orientation"></a>

[Orientation](class_textserver.md#enum-textserver-orientation) **orientation** = `0` [🔗](class_textparagraph.md#class-textparagraph-property-orientation)

- void **set_orientation**(value: [Orientation](class_textserver.md#enum-textserver-orientation))
- [Orientation](class_textserver.md#enum-textserver-orientation) **get_orientation**()

Text orientation.

---


<a id="class-textparagraph-property-preserve-control"></a>

[bool](class_bool.md#class-bool) **preserve_control** = `false` [🔗](class_textparagraph.md#class-textparagraph-property-preserve-control)

- void **set_preserve_control**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_control**()

If set to `true` text will display control characters.

---


<a id="class-textparagraph-property-preserve-invalid"></a>

[bool](class_bool.md#class-bool) **preserve_invalid** = `true` [🔗](class_textparagraph.md#class-textparagraph-property-preserve-invalid)

- void **set_preserve_invalid**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_invalid**()

If set to `true` text will display invalid characters.

---


<a id="class-textparagraph-property-text-overrun-behavior"></a>

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `0` [🔗](class_textparagraph.md#class-textparagraph-property-text-overrun-behavior)

- void **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the paragraph's set width.

---


<a id="class-textparagraph-property-width"></a>

[float](class_float.md#class-float) **width** = `-1.0` [🔗](class_textparagraph.md#class-textparagraph-property-width)

- void **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Paragraph width.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-textparagraph-method-add-object"></a>

[bool](class_bool.md#class-bool) **add_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0) [🔗](class_textparagraph.md#class-textparagraph-method-add-object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---


<a id="class-textparagraph-method-add-string"></a>

[bool](class_bool.md#class-bool) **add_string**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null) [🔗](class_textparagraph.md#class-textparagraph-method-add-string)

Adds text span and font to draw it.

---


<a id="class-textparagraph-method-clear"></a>

void **clear**() [🔗](class_textparagraph.md#class-textparagraph-method-clear)

Clears text paragraph (removes text and inline objects).

---


<a id="class-textparagraph-method-clear-dropcap"></a>

void **clear_dropcap**() [🔗](class_textparagraph.md#class-textparagraph-method-clear-dropcap)

Removes dropcap.

---


<a id="class-textparagraph-method-draw"></a>

void **draw**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw)

Draw all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-draw-dropcap"></a>

void **draw_dropcap**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw-dropcap)

Draw drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-draw-dropcap-outline"></a>

void **draw_dropcap_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw-dropcap-outline)

Draw drop cap outline into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-draw-line"></a>

void **draw_line**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw-line)

Draw single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-draw-line-outline"></a>

void **draw_line_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw-line-outline)

Draw outline of the single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-draw-outline"></a>

void **draw_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textparagraph.md#class-textparagraph-method-draw-outline)

Draw outlines of all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textparagraph-method-duplicate"></a>

[TextParagraph](class_textparagraph.md#class-textparagraph) **duplicate**() const [🔗](class_textparagraph.md#class-textparagraph-method-duplicate)

Duplicates this **TextParagraph**.

---


<a id="class-textparagraph-method-get-dropcap-lines"></a>

[int](class_int.md#class-int) **get_dropcap_lines**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-dropcap-lines)

Returns number of lines used by dropcap.

---


<a id="class-textparagraph-method-get-dropcap-rid"></a>

[RID](class_rid.md#class-rid) **get_dropcap_rid**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-dropcap-rid)

Returns drop cap text buffer RID.

---


<a id="class-textparagraph-method-get-dropcap-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_dropcap_size**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-dropcap-size)

Returns drop cap bounding box size.

---


<a id="class-textparagraph-method-get-inferred-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **get_inferred_direction**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-inferred-direction)

Returns the text writing direction inferred by the BiDi algorithm.

---


<a id="class-textparagraph-method-get-line-ascent"></a>

[float](class_float.md#class-float) **get_line_ascent**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-ascent)

Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---


<a id="class-textparagraph-method-get-line-count"></a>

[int](class_int.md#class-int) **get_line_count**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-count)

Returns number of lines in the paragraph.

---


<a id="class-textparagraph-method-get-line-descent"></a>

[float](class_float.md#class-float) **get_line_descent**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-descent)

Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---


<a id="class-textparagraph-method-get-line-object-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_line_object_rect**(line: [int](class_int.md#class-int), key: [Variant](class_variant.md#class-variant)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-object-rect)

Returns bounding rectangle of the inline object.

---


<a id="class-textparagraph-method-get-line-objects"></a>

[Array](class_array.md#class-array) **get_line_objects**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-objects)

Returns array of inline objects in the line.

---


<a id="class-textparagraph-method-get-line-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_line_range**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-range)

Returns character range of the line.

---


<a id="class-textparagraph-method-get-line-rid"></a>

[RID](class_rid.md#class-rid) **get_line_rid**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-rid)

Returns TextServer line buffer RID.

---


<a id="class-textparagraph-method-get-line-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_line_size**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-size)

Returns size of the bounding box of the line of text. Returned size is rounded up.

---


<a id="class-textparagraph-method-get-line-underline-position"></a>

[float](class_float.md#class-float) **get_line_underline_position**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-underline-position)

Returns pixel offset of the underline below the baseline.

---


<a id="class-textparagraph-method-get-line-underline-thickness"></a>

[float](class_float.md#class-float) **get_line_underline_thickness**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-underline-thickness)

Returns thickness of the underline.

---


<a id="class-textparagraph-method-get-line-width"></a>

[float](class_float.md#class-float) **get_line_width**(line: [int](class_int.md#class-int)) const [🔗](class_textparagraph.md#class-textparagraph-method-get-line-width)

Returns width (for horizontal layout) or height (for vertical) of the line of text.

---


<a id="class-textparagraph-method-get-non-wrapped-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_non_wrapped_size**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-non-wrapped-size)

Returns the size of the bounding box of the paragraph, without line breaks.

---


<a id="class-textparagraph-method-get-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_range**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-range)

Returns the character range of the paragraph.

---


<a id="class-textparagraph-method-get-rid"></a>

[RID](class_rid.md#class-rid) **get_rid**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-rid)

Returns TextServer full string buffer RID.

---


<a id="class-textparagraph-method-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_size**() const [🔗](class_textparagraph.md#class-textparagraph-method-get-size)

Returns the size of the bounding box of the paragraph.

---


<a id="class-textparagraph-method-has-object"></a>

[bool](class_bool.md#class-bool) **has_object**(key: [Variant](class_variant.md#class-variant)) const [🔗](class_textparagraph.md#class-textparagraph-method-has-object)

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---


<a id="class-textparagraph-method-hit-test"></a>

[int](class_int.md#class-int) **hit_test**(coords: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_textparagraph.md#class-textparagraph-method-hit-test)

Returns caret character offset at the specified coordinates. This function always returns a valid position.

---


<a id="class-textparagraph-method-resize-object"></a>

[bool](class_bool.md#class-bool) **resize_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0) [🔗](class_textparagraph.md#class-textparagraph-method-resize-object)

Sets new size and alignment of embedded object.

---


<a id="class-textparagraph-method-set-bidi-override"></a>

void **set_bidi_override**(override: [Array](class_array.md#class-array)) [🔗](class_textparagraph.md#class-textparagraph-method-set-bidi-override)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---


<a id="class-textparagraph-method-set-dropcap"></a>

[bool](class_bool.md#class-bool) **set_dropcap**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class-string) = "") [🔗](class_textparagraph.md#class-textparagraph-method-set-dropcap)

Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

---


<a id="class-textparagraph-method-tab-align"></a>

void **tab_align**(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_textparagraph.md#class-textparagraph-method-tab-align)

Aligns paragraph to the given tab-stops.
