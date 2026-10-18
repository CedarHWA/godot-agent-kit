> Source: https://docs.godotengine.org/en/4.7/classes/class_editorproperty.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorproperty"></a>

<a id="class-editorproperty"></a>

# EditorProperty

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class-editorinspector).

<a id="description"></a>

## Description

A custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class-editorinspector). It is added via [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [checkable](class_editorproperty.md#class-editorproperty-property-checkable) | `false` |
| [bool](class_bool.md#class-bool) | [checked](class_editorproperty.md#class-editorproperty-property-checked) | `false` |
| [bool](class_bool.md#class-bool) | [deletable](class_editorproperty.md#class-editorproperty-property-deletable) | `false` |
| [bool](class_bool.md#class-bool) | [draw_background](class_editorproperty.md#class-editorproperty-property-draw-background) | `true` |
| [bool](class_bool.md#class-bool) | [draw_label](class_editorproperty.md#class-editorproperty-property-draw-label) | `true` |
| [bool](class_bool.md#class-bool) | [draw_warning](class_editorproperty.md#class-editorproperty-property-draw-warning) | `false` |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `3` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool) | [keying](class_editorproperty.md#class-editorproperty-property-keying) | `false` |
| [String](class_string.md#class-string) | [label](class_editorproperty.md#class-editorproperty-property-label) | `""` |
| [float](class_float.md#class-float) | [name_split_ratio](class_editorproperty.md#class-editorproperty-property-name-split-ratio) | `0.5` |
| [bool](class_bool.md#class-bool) | [read_only](class_editorproperty.md#class-editorproperty-property-read-only) | `false` |
| [bool](class_bool.md#class-bool) | [selectable](class_editorproperty.md#class-editorproperty-property-selectable) | `true` |
| [bool](class_bool.md#class-bool) | [use_folding](class_editorproperty.md#class-editorproperty-property-use-folding) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_set_read_only](class_editorproperty.md#class-editorproperty-private-method-set-read-only)(read_only: [bool](class_bool.md#class-bool)) virtual |
| void | [_update_property](class_editorproperty.md#class-editorproperty-private-method-update-property)() virtual |
| void | [add_focusable](class_editorproperty.md#class-editorproperty-method-add-focusable)(control: [Control](class_control.md#class-control)) |
| void | [deselect](class_editorproperty.md#class-editorproperty-method-deselect)() |
| void | [emit_changed](class_editorproperty.md#class-editorproperty-method-emit-changed)(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname) = &"", changing: [bool](class_bool.md#class-bool) = false) |
| [Object](class_object.md#class-object) | [get_edited_object](class_editorproperty.md#class-editorproperty-method-get-edited-object)() |
| [StringName](class_stringname.md#class-stringname) | [get_edited_property](class_editorproperty.md#class-editorproperty-method-get-edited-property)() const |
| [bool](class_bool.md#class-bool) | [is_selected](class_editorproperty.md#class-editorproperty-method-is-selected)() const |
| void | [select](class_editorproperty.md#class-editorproperty-method-select)(focusable: [int](class_int.md#class-int) = -1) |
| void | [set_bottom_editor](class_editorproperty.md#class-editorproperty-method-set-bottom-editor)(editor: [Control](class_control.md#class-control)) |
| void | [set_label_reference](class_editorproperty.md#class-editorproperty-method-set-label-reference)(control: [Control](class_control.md#class-control)) |
| void | [set_object_and_property](class_editorproperty.md#class-editorproperty-method-set-object-and-property)(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname)) |
| void | [update_property](class_editorproperty.md#class-editorproperty-method-update-property)() |

---


<a id="signals"></a>

## Signals

<a id="class-editorproperty-signal-multiple-properties-changed"></a>

**multiple_properties_changed**(properties: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), value: [Array](class_array.md#class-array)) [🔗](class_editorproperty.md#class-editorproperty-signal-multiple-properties-changed)

Emit it if you want multiple properties modified at the same time. Do not use if added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class-editorinspectorplugin-private-method-parse-property).

---


<a id="class-editorproperty-signal-object-id-selected"></a>

**object_id_selected**(property: [StringName](class_stringname.md#class-stringname), id: [int](class_int.md#class-int)) [🔗](class_editorproperty.md#class-editorproperty-signal-object-id-selected)

Used by sub-inspectors. Emit it if what was selected was an Object ID.

---


<a id="class-editorproperty-signal-property-can-revert-changed"></a>

**property_can_revert_changed**(property: [StringName](class_stringname.md#class-stringname), can_revert: [bool](class_bool.md#class-bool)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-can-revert-changed)

Emitted when the revertability (i.e., whether it has a non-default value and thus is displayed with a revert icon) of a property has changed.

---


<a id="class-editorproperty-signal-property-changed"></a>

**property_changed**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname), changing: [bool](class_bool.md#class-bool)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-changed)

Do not emit this manually, use the [emit_changed()](class_editorproperty.md#class-editorproperty-method-emit-changed) method instead.

---


<a id="class-editorproperty-signal-property-checked"></a>

**property_checked**(property: [StringName](class_stringname.md#class-stringname), checked: [bool](class_bool.md#class-bool)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-checked)

Emitted when a property was checked. Used internally.

---


<a id="class-editorproperty-signal-property-deleted"></a>

**property_deleted**(property: [StringName](class_stringname.md#class-stringname)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-deleted)

Emitted when a property was deleted. Used internally.

---


<a id="class-editorproperty-signal-property-favorited"></a>

**property_favorited**(property: [StringName](class_stringname.md#class-stringname), favorited: [bool](class_bool.md#class-bool)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-favorited)

Emit it if you want to mark a property as favorited, making it appear at the top of the inspector.

---


<a id="class-editorproperty-signal-property-keyed"></a>

**property_keyed**(property: [StringName](class_stringname.md#class-stringname)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-keyed)

Emit it if you want to add this value as an animation key (check for keying being enabled first).

---


<a id="class-editorproperty-signal-property-keyed-with-value"></a>

**property_keyed_with_value**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-keyed-with-value)

Emit it if you want to key a property with a single value.

---


<a id="class-editorproperty-signal-property-overridden"></a>

**property_overridden**() [🔗](class_editorproperty.md#class-editorproperty-signal-property-overridden)

Emitted when a setting override for the current project is requested.

---


<a id="class-editorproperty-signal-property-pinned"></a>

**property_pinned**(property: [StringName](class_stringname.md#class-stringname), pinned: [bool](class_bool.md#class-bool)) [🔗](class_editorproperty.md#class-editorproperty-signal-property-pinned)

Emit it if you want to mark (or unmark) the value of a property for being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just instantiated and can come from an ancestor scene in the inheritance/instantiation chain, a script or a builtin class.

---


<a id="class-editorproperty-signal-resource-selected"></a>

**resource_selected**(path: [String](class_string.md#class-string), resource: [Resource](class_resource.md#class-resource)) [🔗](class_editorproperty.md#class-editorproperty-signal-resource-selected)

If you want a sub-resource to be edited, emit this signal with the resource.

---


<a id="class-editorproperty-signal-selected"></a>

**selected**(path: [String](class_string.md#class-string), focusable_idx: [int](class_int.md#class-int)) [🔗](class_editorproperty.md#class-editorproperty-signal-selected)

Emitted when selected. Used internally.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editorproperty-property-checkable"></a>

[bool](class_bool.md#class-bool) **checkable** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-checkable)

- void **set_checkable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_checkable**()

Used by the inspector, set to `true` when the property is checkable.

---


<a id="class-editorproperty-property-checked"></a>

[bool](class_bool.md#class-bool) **checked** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-checked)

- void **set_checked**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_checked**()

Used by the inspector, set to `true` when the property is checked.

---


<a id="class-editorproperty-property-deletable"></a>

[bool](class_bool.md#class-bool) **deletable** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-deletable)

- void **set_deletable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deletable**()

Used by the inspector, set to `true` when the property can be deleted by the user.

---


<a id="class-editorproperty-property-draw-background"></a>

[bool](class_bool.md#class-bool) **draw_background** = `true` [🔗](class_editorproperty.md#class-editorproperty-property-draw-background)

- void **set_draw_background**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_background**()

Used by the inspector, set to `true` when the property background is drawn.

---


<a id="class-editorproperty-property-draw-label"></a>

[bool](class_bool.md#class-bool) **draw_label** = `true` [🔗](class_editorproperty.md#class-editorproperty-property-draw-label)

- void **set_draw_label**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_label**()

Used by the inspector, set to `true` when the property label is drawn.

---


<a id="class-editorproperty-property-draw-warning"></a>

[bool](class_bool.md#class-bool) **draw_warning** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-draw-warning)

- void **set_draw_warning**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_warning**()

Used by the inspector, set to `true` when the property is drawn with the editor theme's warning color. This is used for editable children's properties.

---


<a id="class-editorproperty-property-keying"></a>

[bool](class_bool.md#class-bool) **keying** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-keying)

- void **set_keying**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_keying**()

Used by the inspector, set to `true` when the property can add keys for animation.

---


<a id="class-editorproperty-property-label"></a>

[String](class_string.md#class-string) **label** = `""` [🔗](class_editorproperty.md#class-editorproperty-property-label)

- void **set_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_label**()

Set this property to change the label (if you want to show one).

---


<a id="class-editorproperty-property-name-split-ratio"></a>

[float](class_float.md#class-float) **name_split_ratio** = `0.5` [🔗](class_editorproperty.md#class-editorproperty-property-name-split-ratio)

- void **set_name_split_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_name_split_ratio**()

Space distribution ratio between the label and the editing field.

---


<a id="class-editorproperty-property-read-only"></a>

[bool](class_bool.md#class-bool) **read_only** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-read-only)

- void **set_read_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_read_only**()

Used by the inspector, set to `true` when the property is read-only.

---


<a id="class-editorproperty-property-selectable"></a>

[bool](class_bool.md#class-bool) **selectable** = `true` [🔗](class_editorproperty.md#class-editorproperty-property-selectable)

- void **set_selectable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selectable**()

Used by the inspector, set to `true` when the property is selectable.

---


<a id="class-editorproperty-property-use-folding"></a>

[bool](class_bool.md#class-bool) **use_folding** = `false` [🔗](class_editorproperty.md#class-editorproperty-property-use-folding)

- void **set_use_folding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_folding**()

Used by the inspector, set to `true` when the property is using folding.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorproperty-private-method-set-read-only"></a>

void **_set_read_only**(read_only: [bool](class_bool.md#class-bool)) virtual [🔗](class_editorproperty.md#class-editorproperty-private-method-set-read-only)

Called when the read-only status of the property is changed. It may be used to change custom controls into a read-only or modifiable state.

---


<a id="class-editorproperty-private-method-update-property"></a>

void **_update_property**() virtual [🔗](class_editorproperty.md#class-editorproperty-private-method-update-property)

When this virtual function is called, you must update your editor.

---


<a id="class-editorproperty-method-add-focusable"></a>

void **add_focusable**(control: [Control](class_control.md#class-control)) [🔗](class_editorproperty.md#class-editorproperty-method-add-focusable)

If any of the controls added can gain keyboard focus, add it here. This ensures that focus will be restored if the inspector is refreshed.

---


<a id="class-editorproperty-method-deselect"></a>

void **deselect**() [🔗](class_editorproperty.md#class-editorproperty-method-deselect)

Draw property as not selected. Used by the inspector.

---


<a id="class-editorproperty-method-emit-changed"></a>

void **emit_changed**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname) = &"", changing: [bool](class_bool.md#class-bool) = false) [🔗](class_editorproperty.md#class-editorproperty-method-emit-changed)

If one or several properties have changed, this must be called. `field` is used in case your editor can modify fields separately (as an example, Vector3.x). The `changing` argument avoids the editor requesting this property to be refreshed (leave as `false` if unsure).

---


<a id="class-editorproperty-method-get-edited-object"></a>

[Object](class_object.md#class-object) **get_edited_object**() [🔗](class_editorproperty.md#class-editorproperty-method-get-edited-object)

Returns the edited object.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()](class_editorproperty.md#class-editorproperty-private-method-update-property) and [_set_read_only()](class_editorproperty.md#class-editorproperty-private-method-set-read-only), this value is *guaranteed* to be non-`null`.

---


<a id="class-editorproperty-method-get-edited-property"></a>

[StringName](class_stringname.md#class-stringname) **get_edited_property**() const [🔗](class_editorproperty.md#class-editorproperty-method-get-edited-property)

Returns the edited property. If your editor is for a single property (added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class-editorinspectorplugin-private-method-parse-property)), then this will return the property.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()](class_editorproperty.md#class-editorproperty-private-method-update-property) and [_set_read_only()](class_editorproperty.md#class-editorproperty-private-method-set-read-only), this value is *guaranteed* to be non-`null`.

---


<a id="class-editorproperty-method-is-selected"></a>

[bool](class_bool.md#class-bool) **is_selected**() const [🔗](class_editorproperty.md#class-editorproperty-method-is-selected)

Returns `true` if property is drawn as selected. Used by the inspector.

---


<a id="class-editorproperty-method-select"></a>

void **select**(focusable: [int](class_int.md#class-int) = -1) [🔗](class_editorproperty.md#class-editorproperty-method-select)

Draw property as selected. Used by the inspector.

---


<a id="class-editorproperty-method-set-bottom-editor"></a>

void **set_bottom_editor**(editor: [Control](class_control.md#class-control)) [🔗](class_editorproperty.md#class-editorproperty-method-set-bottom-editor)

Puts the `editor` control below the property label. The control must be previously added using [Node.add_child()](class_node.md#class-node-method-add-child).

---


<a id="class-editorproperty-method-set-label-reference"></a>

void **set_label_reference**(control: [Control](class_control.md#class-control)) [🔗](class_editorproperty.md#class-editorproperty-method-set-label-reference)

Used by the inspector, set to a control that will be used as a reference to calculate the size of the label.

---


<a id="class-editorproperty-method-set-object-and-property"></a>

void **set_object_and_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname)) [🔗](class_editorproperty.md#class-editorproperty-method-set-object-and-property)

Assigns object and property to edit.

---


<a id="class-editorproperty-method-update-property"></a>

void **update_property**() [🔗](class_editorproperty.md#class-editorproperty-method-update-property)

Forces a refresh of the property display.
