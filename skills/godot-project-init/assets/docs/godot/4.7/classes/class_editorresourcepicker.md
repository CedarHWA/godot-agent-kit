> Source: https://docs.godotengine.org/en/4.7/classes/class_editorresourcepicker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorresourcepicker"></a>

<a id="class-editorresourcepicker"></a>

# EditorResourcePicker

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorScriptPicker](class_editorscriptpicker.md#class-editorscriptpicker)

Godot editor's control for selecting [Resource](class_resource.md#class-resource) type properties.

<a id="description"></a>

## Description

This [Control](class_control.md#class-control) node is used in the editor's Inspector dock to allow editing of [Resource](class_resource.md#class-resource) type properties. It provides options for creating, loading, saving and converting resources. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) to recreate the same behavior.

**Note:** This [Control](class_control.md#class-control) does not include any editor for the resource, as editing is controlled by the Inspector dock itself or sub-Inspectors.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [base_type](class_editorresourcepicker.md#class-editorresourcepicker-property-base-type) | `""` |
| [bool](class_bool.md#class-bool) | [editable](class_editorresourcepicker.md#class-editorresourcepicker-property-editable) | `true` |
| [Resource](class_resource.md#class-resource) | [edited_resource](class_editorresourcepicker.md#class-editorresourcepicker-property-edited-resource) |  |
| [bool](class_bool.md#class-bool) | [toggle_mode](class_editorresourcepicker.md#class-editorresourcepicker-property-toggle-mode) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_handle_menu_selected](class_editorresourcepicker.md#class-editorresourcepicker-private-method-handle-menu-selected)(id: [int](class_int.md#class-int)) virtual |
| void | [_set_create_options](class_editorresourcepicker.md#class-editorresourcepicker-private-method-set-create-options)(menu_node: [Object](class_object.md#class-object)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_allowed_types](class_editorresourcepicker.md#class-editorresourcepicker-method-get-allowed-types)() const |
| void | [set_toggle_pressed](class_editorresourcepicker.md#class-editorresourcepicker-method-set-toggle-pressed)(pressed: [bool](class_bool.md#class-bool)) |

---


<a id="signals"></a>

## Signals

<a id="class-editorresourcepicker-signal-resource-changed"></a>

**resource_changed**(resource: [Resource](class_resource.md#class-resource)) [🔗](class_editorresourcepicker.md#class-editorresourcepicker-signal-resource-changed)

Emitted when the value of the edited resource was changed.

---


<a id="class-editorresourcepicker-signal-resource-selected"></a>

**resource_selected**(resource: [Resource](class_resource.md#class-resource), inspect: [bool](class_bool.md#class-bool)) [🔗](class_editorresourcepicker.md#class-editorresourcepicker-signal-resource-selected)

Emitted when the resource value was set and user clicked to edit it. When `inspect` is `true`, the signal was caused by the context menu "Edit" or "Inspect" option.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editorresourcepicker-property-base-type"></a>

[String](class_string.md#class-string) **base_type** = `""` [🔗](class_editorresourcepicker.md#class-editorresourcepicker-property-base-type)

- void **set_base_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_base_type**()

The base type of allowed resource types. Can be a comma-separated list of several options.

---


<a id="class-editorresourcepicker-property-editable"></a>

[bool](class_bool.md#class-bool) **editable** = `true` [🔗](class_editorresourcepicker.md#class-editorresourcepicker-property-editable)

- void **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `true`, the value can be selected and edited.

---


<a id="class-editorresourcepicker-property-edited-resource"></a>

[Resource](class_resource.md#class-resource) **edited_resource** [🔗](class_editorresourcepicker.md#class-editorresourcepicker-property-edited-resource)

- void **set_edited_resource**(value: [Resource](class_resource.md#class-resource))
- [Resource](class_resource.md#class-resource) **get_edited_resource**()

The edited resource value.

---


<a id="class-editorresourcepicker-property-toggle-mode"></a>

[bool](class_bool.md#class-bool) **toggle_mode** = `false` [🔗](class_editorresourcepicker.md#class-editorresourcepicker-property-toggle-mode)

- void **set_toggle_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_toggle_mode**()

If `true`, the main button with the resource preview works in the toggle mode. Use [set_toggle_pressed()](class_editorresourcepicker.md#class-editorresourcepicker-method-set-toggle-pressed) to manually set the state.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorresourcepicker-private-method-handle-menu-selected"></a>

[bool](class_bool.md#class-bool) **_handle_menu_selected**(id: [int](class_int.md#class-int)) virtual [🔗](class_editorresourcepicker.md#class-editorresourcepicker-private-method-handle-menu-selected)

This virtual method can be implemented to handle context menu items not handled by default. See [_set_create_options()](class_editorresourcepicker.md#class-editorresourcepicker-private-method-set-create-options).

---


<a id="class-editorresourcepicker-private-method-set-create-options"></a>

void **_set_create_options**(menu_node: [Object](class_object.md#class-object)) virtual [🔗](class_editorresourcepicker.md#class-editorresourcepicker-private-method-set-create-options)

This virtual method is called when updating the context menu of an [editable](class_editorresourcepicker.md#class-editorresourcepicker-property-editable) **EditorResourcePicker**. Implement this method to override the "New" items section with your own options. `menu_node` is a reference to the [PopupMenu](class_popupmenu.md#class-popupmenu) node.

**Note:** Implement [_handle_menu_selected()](class_editorresourcepicker.md#class-editorresourcepicker-private-method-handle-menu-selected) to handle these custom items.

**Note:** Relevant built-in options ("Load", "Copy", "Paste", etc.) are automatically added to the `menu_node` afterwards, using their hard-coded IDs starting from `0`. Custom options need to use non-colliding IDs to be handled properly. Using `id = 100 + custom_option_index` is safe (this is what the default items in the "New" section use).

---


<a id="class-editorresourcepicker-method-get-allowed-types"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_allowed_types**() const [🔗](class_editorresourcepicker.md#class-editorresourcepicker-method-get-allowed-types)

Returns a list of all allowed types and subtypes corresponding to the [base_type](class_editorresourcepicker.md#class-editorresourcepicker-property-base-type). If the [base_type](class_editorresourcepicker.md#class-editorresourcepicker-property-base-type) is empty, an empty list is returned.

---


<a id="class-editorresourcepicker-method-set-toggle-pressed"></a>

void **set_toggle_pressed**(pressed: [bool](class_bool.md#class-bool)) [🔗](class_editorresourcepicker.md#class-editorresourcepicker-method-set-toggle-pressed)

Sets the toggle mode state for the main button. Works only if [toggle_mode](class_editorresourcepicker.md#class-editorresourcepicker-property-toggle-mode) is set to `true`.
