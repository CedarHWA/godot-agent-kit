> Source: https://docs.godotengine.org/en/4.7/classes/class_range.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="range"></a>

<a id="class-range"></a>

# Range

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorSpinSlider](class_editorspinslider.md#class-editorspinslider), [ProgressBar](class_progressbar.md#class-progressbar), [ScrollBar](class_scrollbar.md#class-scrollbar), [Slider](class_slider.md#class-slider), [SpinBox](class_spinbox.md#class-spinbox), [TextureProgressBar](class_textureprogressbar.md#class-textureprogressbar)

Abstract base class for controls that represent a number within a range.

<a id="description"></a>

## Description

Range is an abstract base class for controls that represent a number within a range, using a configured [step](class_range.md#class-range-property-step) and [page](class_range.md#class-range-property-page) size. See e.g. [ScrollBar](class_scrollbar.md#class-scrollbar) and [Slider](class_slider.md#class-slider) for examples of higher-level nodes using Range.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_greater](class_range.md#class-range-property-allow-greater) | `false` |
| [bool](class_bool.md#class-bool) | [allow_lesser](class_range.md#class-range-property-allow-lesser) | `false` |
| [bool](class_bool.md#class-bool) | [exp_edit](class_range.md#class-range-property-exp-edit) | `false` |
| [float](class_float.md#class-float) | [max_value](class_range.md#class-range-property-max-value) | `100.0` |
| [float](class_float.md#class-float) | [min_value](class_range.md#class-range-property-min-value) | `0.0` |
| [float](class_float.md#class-float) | [page](class_range.md#class-range-property-page) | `0.0` |
| [float](class_float.md#class-float) | [ratio](class_range.md#class-range-property-ratio) |  |
| [bool](class_bool.md#class-bool) | [rounded](class_range.md#class-range-property-rounded) | `false` |
| BitField[[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_vertical | `0` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [float](class_float.md#class-float) | [step](class_range.md#class-range-property-step) | `0.01` |
| [float](class_float.md#class-float) | [value](class_range.md#class-range-property-value) | `0.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_value_changed](class_range.md#class-range-private-method-value-changed)(new_value: [float](class_float.md#class-float)) virtual |
| void | [set_value_no_signal](class_range.md#class-range-method-set-value-no-signal)(value: [float](class_float.md#class-float)) |
| void | [share](class_range.md#class-range-method-share)(with: [Node](class_node.md#class-node)) |
| void | [unshare](class_range.md#class-range-method-unshare)() |

---


<a id="signals"></a>

## Signals

<a id="class-range-signal-changed"></a>

**changed**() [🔗](class_range.md#class-range-signal-changed)

Emitted when [min_value](class_range.md#class-range-property-min-value), [max_value](class_range.md#class-range-property-max-value), [page](class_range.md#class-range-property-page), or [step](class_range.md#class-range-property-step) change.

---


<a id="class-range-signal-value-changed"></a>

**value_changed**(value: [float](class_float.md#class-float)) [🔗](class_range.md#class-range-signal-value-changed)

Emitted when [value](class_range.md#class-range-property-value) changes. When used on a [Slider](class_slider.md#class-slider), this is called continuously while dragging (potentially every frame). If you are performing an expensive operation in a function connected to [value_changed](class_range.md#class-range-signal-value-changed), consider using a *debouncing* [Timer](class_timer.md#class-timer) to call the function less often.

**Note:** Unlike signals such as [LineEdit.text_changed](class_lineedit.md#class-lineedit-signal-text-changed), [value_changed](class_range.md#class-range-signal-value-changed) is also emitted when `value` is set directly via code.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-range-property-allow-greater"></a>

[bool](class_bool.md#class-bool) **allow_greater** = `false` [🔗](class_range.md#class-range-property-allow-greater)

- void **set_allow_greater**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_greater_allowed**()

If `true`, [value](class_range.md#class-range-property-value) may be greater than [max_value](class_range.md#class-range-property-max-value).

---


<a id="class-range-property-allow-lesser"></a>

[bool](class_bool.md#class-bool) **allow_lesser** = `false` [🔗](class_range.md#class-range-property-allow-lesser)

- void **set_allow_lesser**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_lesser_allowed**()

If `true`, [value](class_range.md#class-range-property-value) may be less than [min_value](class_range.md#class-range-property-min-value).

---


<a id="class-range-property-exp-edit"></a>

[bool](class_bool.md#class-bool) **exp_edit** = `false` [🔗](class_range.md#class-range-property-exp-edit)

- void **set_exp_ratio**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ratio_exp**()

If `true`, and [min_value](class_range.md#class-range-property-min-value) is greater or equal to `0`, [value](class_range.md#class-range-property-value) will be represented exponentially rather than linearly.

---


<a id="class-range-property-max-value"></a>

[float](class_float.md#class-float) **max_value** = `100.0` [🔗](class_range.md#class-range-property-max-value)

- void **set_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max**()

Maximum value. Range is clamped if [value](class_range.md#class-range-property-value) is greater than [max_value](class_range.md#class-range-property-max-value).

---


<a id="class-range-property-min-value"></a>

[float](class_float.md#class-float) **min_value** = `0.0` [🔗](class_range.md#class-range-property-min-value)

- void **set_min**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min**()

Minimum value. Range is clamped if [value](class_range.md#class-range-property-value) is less than [min_value](class_range.md#class-range-property-min-value).

---


<a id="class-range-property-page"></a>

[float](class_float.md#class-float) **page** = `0.0` [🔗](class_range.md#class-range-property-page)

- void **set_page**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_page**()

Page size. Used mainly for [ScrollBar](class_scrollbar.md#class-scrollbar). A [ScrollBar](class_scrollbar.md#class-scrollbar)'s grabber length is the [ScrollBar](class_scrollbar.md#class-scrollbar)'s size multiplied by [page](class_range.md#class-range-property-page) over the difference between [min_value](class_range.md#class-range-property-min-value) and [max_value](class_range.md#class-range-property-max-value).

---


<a id="class-range-property-ratio"></a>

[float](class_float.md#class-float) **ratio** [🔗](class_range.md#class-range-property-ratio)

- void **set_as_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_as_ratio**()

The value mapped between 0 and 1.

---


<a id="class-range-property-rounded"></a>

[bool](class_bool.md#class-bool) **rounded** = `false` [🔗](class_range.md#class-range-property-rounded)

- void **set_use_rounded_values**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_rounded_values**()

If `true`, [value](class_range.md#class-range-property-value) will always be rounded to the nearest integer.

---


<a id="class-range-property-step"></a>

[float](class_float.md#class-float) **step** = `0.01` [🔗](class_range.md#class-range-property-step)

- void **set_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_step**()

If greater than `0.0`, [value](class_range.md#class-range-property-value) will always be rounded to a multiple of this property's value above [min_value](class_range.md#class-range-property-min-value). For example, if [min_value](class_range.md#class-range-property-min-value) is `0.1` and step is `0.2`, then [value](class_range.md#class-range-property-value) is limited to `0.1`, `0.3`, `0.5`, and so on. If [rounded](class_range.md#class-range-property-rounded) is also `true`, [value](class_range.md#class-range-property-value) will first be rounded to a multiple of this property's value, then rounded to the nearest integer.

---


<a id="class-range-property-value"></a>

[float](class_float.md#class-float) **value** = `0.0` [🔗](class_range.md#class-range-property-value)

- void **set_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_value**()

Range's current value. Changing this property (even via code) will trigger [value_changed](class_range.md#class-range-signal-value-changed) signal. Use [set_value_no_signal()](class_range.md#class-range-method-set-value-no-signal) if you want to avoid it.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-range-private-method-value-changed"></a>

void **_value_changed**(new_value: [float](class_float.md#class-float)) virtual [🔗](class_range.md#class-range-private-method-value-changed)

Called when the **Range**'s value is changed (following the same conditions as [value_changed](class_range.md#class-range-signal-value-changed)).

---


<a id="class-range-method-set-value-no-signal"></a>

void **set_value_no_signal**(value: [float](class_float.md#class-float)) [🔗](class_range.md#class-range-method-set-value-no-signal)

Sets the **Range**'s current value to the specified `value`, without emitting the [value_changed](class_range.md#class-range-signal-value-changed) signal.

---


<a id="class-range-method-share"></a>

void **share**(with: [Node](class_node.md#class-node)) [🔗](class_range.md#class-range-method-share)

Binds two **Range**s together along with any ranges previously grouped with either of them. When any of range's member variables change, it will share the new value with all other ranges in its group.

---


<a id="class-range-method-unshare"></a>

void **unshare**() [🔗](class_range.md#class-range-method-unshare)

Stops the **Range** from sharing its member variables with any other.
