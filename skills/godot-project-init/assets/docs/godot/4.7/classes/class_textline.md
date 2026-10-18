> Source: https://docs.godotengine.org/en/4.7/classes/class_textline.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="textline"></a>

<a id="class-textline"></a>

# TextLine

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a line of text.

<a id="description"></a>

## Description

Abstraction over [TextServer](class_textserver.md#class-textserver) for handling a single line of text.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | [alignment](class_textline.md#class-textline-property-alignment) | `0` |
| [Direction](class_textserver.md#enum-textserver-direction) | [direction](class_textline.md#class-textline-property-direction) | `0` |
| [String](class_string.md#class-string) | [ellipsis_char](class_textline.md#class-textline-property-ellipsis-char) | `"…"` |
| BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] | [flags](class_textline.md#class-textline-property-flags) | `3` |
| [Orientation](class_textserver.md#enum-textserver-orientation) | [orientation](class_textline.md#class-textline-property-orientation) | `0` |
| [bool](class_bool.md#class-bool) | [preserve_control](class_textline.md#class-textline-property-preserve-control) | `false` |
| [bool](class_bool.md#class-bool) | [preserve_invalid](class_textline.md#class-textline-property-preserve-invalid) | `true` |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) | [text_overrun_behavior](class_textline.md#class-textline-property-text-overrun-behavior) | `3` |
| [float](class_float.md#class-float) | [width](class_textline.md#class-textline-property-width) | `-1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [add_object](class_textline.md#class-textline-method-add-object)(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0) |
| [bool](class_bool.md#class-bool) | [add_string](class_textline.md#class-textline-method-add-string)(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null) |
| void | [clear](class_textline.md#class-textline-method-clear)() |
| void | [draw](class_textline.md#class-textline-method-draw)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_outline](class_textline.md#class-textline-method-draw-outline)(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| [TextLine](class_textline.md#class-textline) | [duplicate](class_textline.md#class-textline-method-duplicate)() const |
| [Direction](class_textserver.md#enum-textserver-direction) | [get_inferred_direction](class_textline.md#class-textline-method-get-inferred-direction)() const |
| [float](class_float.md#class-float) | [get_line_ascent](class_textline.md#class-textline-method-get-line-ascent)() const |
| [float](class_float.md#class-float) | [get_line_descent](class_textline.md#class-textline-method-get-line-descent)() const |
| [float](class_float.md#class-float) | [get_line_underline_position](class_textline.md#class-textline-method-get-line-underline-position)() const |
| [float](class_float.md#class-float) | [get_line_underline_thickness](class_textline.md#class-textline-method-get-line-underline-thickness)() const |
| [float](class_float.md#class-float) | [get_line_width](class_textline.md#class-textline-method-get-line-width)() const |
| [Rect2](class_rect2.md#class-rect2) | [get_object_rect](class_textline.md#class-textline-method-get-object-rect)(key: [Variant](class_variant.md#class-variant)) const |
| [Array](class_array.md#class-array) | [get_objects](class_textline.md#class-textline-method-get-objects)() const |
| [RID](class_rid.md#class-rid) | [get_rid](class_textline.md#class-textline-method-get-rid)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_size](class_textline.md#class-textline-method-get-size)() const |
| [bool](class_bool.md#class-bool) | [has_object](class_textline.md#class-textline-method-has-object)(key: [Variant](class_variant.md#class-variant)) const |
| [int](class_int.md#class-int) | [hit_test](class_textline.md#class-textline-method-hit-test)(coords: [float](class_float.md#class-float)) const |
| [bool](class_bool.md#class-bool) | [resize_object](class_textline.md#class-textline-method-resize-object)(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0) |
| void | [set_bidi_override](class_textline.md#class-textline-method-set-bidi-override)(override: [Array](class_array.md#class-array)) |
| void | [tab_align](class_textline.md#class-textline-method-tab-align)(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-textline-property-alignment"></a>

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0` [🔗](class_textline.md#class-textline-property-alignment)

- void **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Sets text alignment within the line as if the line was horizontal.

---


<a id="class-textline-property-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **direction** = `0` [🔗](class_textline.md#class-textline-property-direction)

- void **set_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_direction**()

Text writing direction.

---


<a id="class-textline-property-ellipsis-char"></a>

[String](class_string.md#class-string) **ellipsis_char** = `"…"` [🔗](class_textline.md#class-textline-property-ellipsis-char)

- void **set_ellipsis_char**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ellipsis_char**()

Ellipsis character used for text clipping.

---


<a id="class-textline-property-flags"></a>

BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **flags** = `3` [🔗](class_textline.md#class-textline-property-flags)

- void **set_flags**(value: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_flags**()

Line alignment rules. For more info see [TextServer](class_textserver.md#class-textserver).

---


<a id="class-textline-property-orientation"></a>

[Orientation](class_textserver.md#enum-textserver-orientation) **orientation** = `0` [🔗](class_textline.md#class-textline-property-orientation)

- void **set_orientation**(value: [Orientation](class_textserver.md#enum-textserver-orientation))
- [Orientation](class_textserver.md#enum-textserver-orientation) **get_orientation**()

Text orientation.

---


<a id="class-textline-property-preserve-control"></a>

[bool](class_bool.md#class-bool) **preserve_control** = `false` [🔗](class_textline.md#class-textline-property-preserve-control)

- void **set_preserve_control**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_control**()

If set to `true` text will display control characters.

---


<a id="class-textline-property-preserve-invalid"></a>

[bool](class_bool.md#class-bool) **preserve_invalid** = `true` [🔗](class_textline.md#class-textline-property-preserve-invalid)

- void **set_preserve_invalid**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_invalid**()

If set to `true` text will display invalid characters.

---


<a id="class-textline-property-text-overrun-behavior"></a>

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `3` [🔗](class_textline.md#class-textline-property-text-overrun-behavior)

- void **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the text line's set width.

---


<a id="class-textline-property-width"></a>

[float](class_float.md#class-float) **width** = `-1.0` [🔗](class_textline.md#class-textline-property-width)

- void **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Text line width.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-textline-method-add-object"></a>

[bool](class_bool.md#class-bool) **add_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0) [🔗](class_textline.md#class-textline-method-add-object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---


<a id="class-textline-method-add-string"></a>

[bool](class_bool.md#class-bool) **add_string**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null) [🔗](class_textline.md#class-textline-method-add-string)

Adds text span and font to draw it.

---


<a id="class-textline-method-clear"></a>

void **clear**() [🔗](class_textline.md#class-textline-method-clear)

Clears text line (removes text and inline objects).

---


<a id="class-textline-method-draw"></a>

void **draw**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textline.md#class-textline-method-draw)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textline-method-draw-outline"></a>

void **draw_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_textline.md#class-textline-method-draw-outline)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textline-method-duplicate"></a>

[TextLine](class_textline.md#class-textline) **duplicate**() const [🔗](class_textline.md#class-textline-method-duplicate)

Duplicates this **TextLine**.

---


<a id="class-textline-method-get-inferred-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **get_inferred_direction**() const [🔗](class_textline.md#class-textline-method-get-inferred-direction)

Returns the text writing direction inferred by the BiDi algorithm.

---


<a id="class-textline-method-get-line-ascent"></a>

[float](class_float.md#class-float) **get_line_ascent**() const [🔗](class_textline.md#class-textline-method-get-line-ascent)

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---


<a id="class-textline-method-get-line-descent"></a>

[float](class_float.md#class-float) **get_line_descent**() const [🔗](class_textline.md#class-textline-method-get-line-descent)

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---


<a id="class-textline-method-get-line-underline-position"></a>

[float](class_float.md#class-float) **get_line_underline_position**() const [🔗](class_textline.md#class-textline-method-get-line-underline-position)

Returns pixel offset of the underline below the baseline.

---


<a id="class-textline-method-get-line-underline-thickness"></a>

[float](class_float.md#class-float) **get_line_underline_thickness**() const [🔗](class_textline.md#class-textline-method-get-line-underline-thickness)

Returns thickness of the underline.

---


<a id="class-textline-method-get-line-width"></a>

[float](class_float.md#class-float) **get_line_width**() const [🔗](class_textline.md#class-textline-method-get-line-width)

Returns width (for horizontal layout) or height (for vertical) of the text.

---


<a id="class-textline-method-get-object-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_object_rect**(key: [Variant](class_variant.md#class-variant)) const [🔗](class_textline.md#class-textline-method-get-object-rect)

Returns bounding rectangle of the inline object.

---


<a id="class-textline-method-get-objects"></a>

[Array](class_array.md#class-array) **get_objects**() const [🔗](class_textline.md#class-textline-method-get-objects)

Returns array of inline objects.

---


<a id="class-textline-method-get-rid"></a>

[RID](class_rid.md#class-rid) **get_rid**() const [🔗](class_textline.md#class-textline-method-get-rid)

Returns TextServer buffer RID.

---


<a id="class-textline-method-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_size**() const [🔗](class_textline.md#class-textline-method-get-size)

Returns size of the bounding box of the text.

---


<a id="class-textline-method-has-object"></a>

[bool](class_bool.md#class-bool) **has_object**(key: [Variant](class_variant.md#class-variant)) const [🔗](class_textline.md#class-textline-method-has-object)

Returns `true` if an object with `key` is embedded in this line.

---


<a id="class-textline-method-hit-test"></a>

[int](class_int.md#class-int) **hit_test**(coords: [float](class_float.md#class-float)) const [🔗](class_textline.md#class-textline-method-hit-test)

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---


<a id="class-textline-method-resize-object"></a>

[bool](class_bool.md#class-bool) **resize_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0) [🔗](class_textline.md#class-textline-method-resize-object)

Sets new size and alignment of embedded object.

---


<a id="class-textline-method-set-bidi-override"></a>

void **set_bidi_override**(override: [Array](class_array.md#class-array)) [🔗](class_textline.md#class-textline-method-set-bidi-override)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---


<a id="class-textline-method-tab-align"></a>

void **tab_align**(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_textline.md#class-textline-method-tab-align)

Aligns text to the given tab-stops.
