> Source: https://docs.godotengine.org/en/4.7/classes/class_theme.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="theme"></a>

<a id="class-theme"></a>

# Theme

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource used for styling/skinning [Control](class_control.md#class-control)s and [Window](class_window.md#class-window)s.

<a id="description"></a>

## Description

A resource used for styling/skinning [Control](class_control.md#class-control) and [Window](class_window.md#class-window) nodes. While individual controls can be styled using their local theme overrides (see [Control.add_theme_color_override()](class_control.md#class-control-method-add-theme-color-override)), theme resources allow you to store and apply the same settings across all controls sharing the same type (e.g. style all [Button](class_button.md#class-button)s the same). One theme resource can be used for the entire project, but you can also set a separate theme resource to a branch of control nodes. A theme resource assigned to a control applies to the control itself, as well as all of its direct and indirect children (as long as a chain of controls is uninterrupted).

Use [ProjectSettings.gui/theme/custom](class_projectsettings.md#class-projectsettings-property-gui-theme-custom) to set up a project-scope theme that will be available to every control in your project.

Use [Control.theme](class_control.md#class-control-property-theme) of any control node to set up a theme that will be available to that control and all of its direct and indirect children.

<a id="tutorials"></a>

## Tutorials

- [GUI skinning](../tutorials/ui/gui_skinning.md)
- [Using the theme editor](../tutorials/ui/gui_using_theme_editor.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [default_base_scale](class_theme.md#class-theme-property-default-base-scale) | `0.0` |
| [Font](class_font.md#class-font) | [default_font](class_theme.md#class-theme-property-default-font) |  |
| [int](class_int.md#class-int) | [default_font_size](class_theme.md#class-theme-property-default-font-size) | `-1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_type](class_theme.md#class-theme-method-add-type)(theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear](class_theme.md#class-theme-method-clear)() |
| void | [clear_color](class_theme.md#class-theme-method-clear-color)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_constant](class_theme.md#class-theme-method-clear-constant)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_font](class_theme.md#class-theme-method-clear-font)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_font_size](class_theme.md#class-theme-method-clear-font-size)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_icon](class_theme.md#class-theme-method-clear-icon)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_stylebox](class_theme.md#class-theme-method-clear-stylebox)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_theme_item](class_theme.md#class-theme-method-clear-theme-item)(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_type_variation](class_theme.md#class-theme-method-clear-type-variation)(theme_type: [StringName](class_stringname.md#class-stringname)) |
| [Color](class_color.md#class-color) | [get_color](class_theme.md#class-theme-method-get-color)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_color_list](class_theme.md#class-theme-method-get-color-list)(theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_color_type_list](class_theme.md#class-theme-method-get-color-type-list)() const |
| [int](class_int.md#class-int) | [get_constant](class_theme.md#class-theme-method-get-constant)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_constant_list](class_theme.md#class-theme-method-get-constant-list)(theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_constant_type_list](class_theme.md#class-theme-method-get-constant-type-list)() const |
| [Font](class_font.md#class-font) | [get_font](class_theme.md#class-theme-method-get-font)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_font_list](class_theme.md#class-theme-method-get-font-list)(theme_type: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [get_font_size](class_theme.md#class-theme-method-get-font-size)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_font_size_list](class_theme.md#class-theme-method-get-font-size-list)(theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_font_size_type_list](class_theme.md#class-theme-method-get-font-size-type-list)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_font_type_list](class_theme.md#class-theme-method-get-font-type-list)() const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_icon](class_theme.md#class-theme-method-get-icon)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_icon_list](class_theme.md#class-theme-method-get-icon-list)(theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_icon_type_list](class_theme.md#class-theme-method-get-icon-type-list)() const |
| [StyleBox](class_stylebox.md#class-stylebox) | [get_stylebox](class_theme.md#class-theme-method-get-stylebox)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_stylebox_list](class_theme.md#class-theme-method-get-stylebox-list)(theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_stylebox_type_list](class_theme.md#class-theme-method-get-stylebox-type-list)() const |
| [Variant](class_variant.md#class-variant) | [get_theme_item](class_theme.md#class-theme-method-get-theme-item)(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_theme_item_list](class_theme.md#class-theme-method-get-theme-item-list)(data_type: [DataType](class_theme.md#enum-theme-datatype), theme_type: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_theme_item_type_list](class_theme.md#class-theme-method-get-theme-item-type-list)(data_type: [DataType](class_theme.md#enum-theme-datatype)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_type_list](class_theme.md#class-theme-method-get-type-list)() const |
| [StringName](class_stringname.md#class-stringname) | [get_type_variation_base](class_theme.md#class-theme-method-get-type-variation-base)(theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_type_variation_list](class_theme.md#class-theme-method-get-type-variation-list)(base_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_color](class_theme.md#class-theme-method-has-color)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_constant](class_theme.md#class-theme-method-has-constant)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_default_base_scale](class_theme.md#class-theme-method-has-default-base-scale)() const |
| [bool](class_bool.md#class-bool) | [has_default_font](class_theme.md#class-theme-method-has-default-font)() const |
| [bool](class_bool.md#class-bool) | [has_default_font_size](class_theme.md#class-theme-method-has-default-font-size)() const |
| [bool](class_bool.md#class-bool) | [has_font](class_theme.md#class-theme-method-has-font)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_font_size](class_theme.md#class-theme-method-has-font-size)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_icon](class_theme.md#class-theme-method-has-icon)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_stylebox](class_theme.md#class-theme-method-has-stylebox)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_theme_item](class_theme.md#class-theme-method-has-theme-item)(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_type_variation](class_theme.md#class-theme-method-is-type-variation)(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname)) const |
| void | [merge_with](class_theme.md#class-theme-method-merge-with)(other: [Theme](class_theme.md#class-theme)) |
| void | [remove_type](class_theme.md#class-theme-method-remove-type)(theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_color](class_theme.md#class-theme-method-rename-color)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_constant](class_theme.md#class-theme-method-rename-constant)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_font](class_theme.md#class-theme-method-rename-font)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_font_size](class_theme.md#class-theme-method-rename-font-size)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_icon](class_theme.md#class-theme-method-rename-icon)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_stylebox](class_theme.md#class-theme-method-rename-stylebox)(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_theme_item](class_theme.md#class-theme-method-rename-theme-item)(data_type: [DataType](class_theme.md#enum-theme-datatype), old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_type](class_theme.md#class-theme-method-rename-type)(old_theme_type: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
| void | [set_color](class_theme.md#class-theme-method-set-color)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color)) |
| void | [set_constant](class_theme.md#class-theme-method-set-constant)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), constant: [int](class_int.md#class-int)) |
| void | [set_font](class_theme.md#class-theme-method-set-font)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font: [Font](class_font.md#class-font)) |
| void | [set_font_size](class_theme.md#class-theme-method-set-font-size)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font_size: [int](class_int.md#class-int)) |
| void | [set_icon](class_theme.md#class-theme-method-set-icon)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_stylebox](class_theme.md#class-theme-method-set-stylebox)(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [StyleBox](class_stylebox.md#class-stylebox)) |
| void | [set_theme_item](class_theme.md#class-theme-method-set-theme-item)(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |
| void | [set_type_variation](class_theme.md#class-theme-method-set-type-variation)(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-theme-datatype"></a>

enum **DataType**: [🔗](class_theme.md#enum-theme-datatype)

<a id="class-theme-constant-data-type-color"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_COLOR** = `0`

Theme's [Color](class_color.md#class-color) item type.

<a id="class-theme-constant-data-type-constant"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_CONSTANT** = `1`

Theme's constant item type.

<a id="class-theme-constant-data-type-font"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_FONT** = `2`

Theme's [Font](class_font.md#class-font) item type.

<a id="class-theme-constant-data-type-font-size"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_FONT_SIZE** = `3`

Theme's font size item type.

<a id="class-theme-constant-data-type-icon"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_ICON** = `4`

Theme's icon [Texture2D](class_texture2d.md#class-texture2d) item type.

<a id="class-theme-constant-data-type-stylebox"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_STYLEBOX** = `5`

Theme's [StyleBox](class_stylebox.md#class-stylebox) item type.

<a id="class-theme-constant-data-type-max"></a>

[DataType](class_theme.md#enum-theme-datatype) **DATA_TYPE_MAX** = `6`

Maximum value for the DataType enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-theme-property-default-base-scale"></a>

[float](class_float.md#class-float) **default_base_scale** = `0.0` [🔗](class_theme.md#class-theme-property-default-base-scale)

- void **set_default_base_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_default_base_scale**()

The default base scale factor of this theme resource. Used by some controls to scale their visual properties based on the global scale factor. If this value is set to `0.0`, the global scale factor is used (see [ThemeDB.fallback_base_scale](class_themedb.md#class-themedb-property-fallback-base-scale)).

Use [has_default_base_scale()](class_theme.md#class-theme-method-has-default-base-scale) to check if this value is valid.

---


<a id="class-theme-property-default-font"></a>

[Font](class_font.md#class-font) **default_font** [🔗](class_theme.md#class-theme-property-default-font)

- void **set_default_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_default_font**()

The default font of this theme resource. Used as the default value when trying to fetch a font resource that doesn't exist in this theme or is in invalid state. If the default font is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font](class_themedb.md#class-themedb-property-fallback-font)).

Use [has_default_font()](class_theme.md#class-theme-method-has-default-font) to check if this value is valid.

---


<a id="class-theme-property-default-font-size"></a>

[int](class_int.md#class-int) **default_font_size** = `-1` [🔗](class_theme.md#class-theme-property-default-font-size)

- void **set_default_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_default_font_size**()

The default font size of this theme resource. Used as the default value when trying to fetch a font size value that doesn't exist in this theme or is in invalid state. If the default font size is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font_size](class_themedb.md#class-themedb-property-fallback-font-size)).

Values below `1` are invalid and can be used to unset the property. Use [has_default_font_size()](class_theme.md#class-theme-method-has-default-font-size) to check if this value is valid.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-theme-method-add-type"></a>

void **add_type**(theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-add-type)

Adds an empty theme type for every valid data type.

**Note:** Empty types are not saved with the theme. This method only exists to perform in-memory changes to the resource. Use available `set_*` methods to add theme items.

---


<a id="class-theme-method-clear"></a>

void **clear**() [🔗](class_theme.md#class-theme-method-clear)

Removes all the theme properties defined on the theme resource.

---


<a id="class-theme-method-clear-color"></a>

void **clear_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-color)

Removes the [Color](class_color.md#class-color) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_color()](class_theme.md#class-theme-method-has-color) to check for existence.

---


<a id="class-theme-method-clear-constant"></a>

void **clear_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-constant)

Removes the constant property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_constant()](class_theme.md#class-theme-method-has-constant) to check for existence.

---


<a id="class-theme-method-clear-font"></a>

void **clear_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-font)

Removes the [Font](class_font.md#class-font) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_font()](class_theme.md#class-theme-method-has-font) to check for existence.

---


<a id="class-theme-method-clear-font-size"></a>

void **clear_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-font-size)

Removes the font size property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_font_size()](class_theme.md#class-theme-method-has-font-size) to check for existence.

---


<a id="class-theme-method-clear-icon"></a>

void **clear_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-icon)

Removes the icon property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_icon()](class_theme.md#class-theme-method-has-icon) to check for existence.

---


<a id="class-theme-method-clear-stylebox"></a>

void **clear_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-stylebox)

Removes the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_stylebox()](class_theme.md#class-theme-method-has-stylebox) to check for existence.

---


<a id="class-theme-method-clear-theme-item"></a>

void **clear_theme_item**(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-theme-item)

Removes the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_theme_item()](class_theme.md#class-theme-method-has-theme-item) to check for existence.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-clear-type-variation"></a>

void **clear_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-clear-type-variation)

Unmarks `theme_type` as being a variation of another theme type. See [set_type_variation()](class_theme.md#class-theme-method-set-type-variation).

---


<a id="class-theme-method-get-color"></a>

[Color](class_color.md#class-color) **get_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-color)

Returns the [Color](class_color.md#class-color) property defined by `name` and `theme_type`, if it exists.

Returns the default color value if the property doesn't exist. Use [has_color()](class_theme.md#class-theme-method-has-color) to check for existence.

---


<a id="class-theme-method-get-color-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_color_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-color-list)

Returns a list of names for [Color](class_color.md#class-color) properties defined with `theme_type`. Use [get_color_type_list()](class_theme.md#class-theme-method-get-color-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-color-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_color_type_list**() const [🔗](class_theme.md#class-theme-method-get-color-type-list)

Returns a list of all unique theme type names for [Color](class_color.md#class-color) properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-constant"></a>

[int](class_int.md#class-int) **get_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-constant)

Returns the constant property defined by `name` and `theme_type`, if it exists.

Returns `0` if the property doesn't exist. Use [has_constant()](class_theme.md#class-theme-method-has-constant) to check for existence.

---


<a id="class-theme-method-get-constant-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_constant_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-constant-list)

Returns a list of names for constant properties defined with `theme_type`. Use [get_constant_type_list()](class_theme.md#class-theme-method-get-constant-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-constant-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_constant_type_list**() const [🔗](class_theme.md#class-theme-method-get-constant-type-list)

Returns a list of all unique theme type names for constant properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-font"></a>

[Font](class_font.md#class-font) **get_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-font)

Returns the [Font](class_font.md#class-font) property defined by `name` and `theme_type`, if it exists.

Returns the default theme font if the property doesn't exist and the default theme font is set up (see [default_font](class_theme.md#class-theme-property-default-font)). Use [has_font()](class_theme.md#class-theme-method-has-font) to check for existence of the property and [has_default_font()](class_theme.md#class-theme-method-has-default-font) to check for existence of the default theme font.

Returns the engine fallback font value, if neither exist (see [ThemeDB.fallback_font](class_themedb.md#class-themedb-property-fallback-font)).

---


<a id="class-theme-method-get-font-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-font-list)

Returns a list of names for [Font](class_font.md#class-font) properties defined with `theme_type`. Use [get_font_type_list()](class_theme.md#class-theme-method-get-font-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-font-size"></a>

[int](class_int.md#class-int) **get_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-font-size)

Returns the font size property defined by `name` and `theme_type`, if it exists.

Returns the default theme font size if the property doesn't exist and the default theme font size is set up (see [default_font_size](class_theme.md#class-theme-property-default-font-size)). Use [has_font_size()](class_theme.md#class-theme-method-has-font-size) to check for existence of the property and [has_default_font_size()](class_theme.md#class-theme-method-has-default-font-size) to check for existence of the default theme font.

Returns the engine fallback font size value, if neither exist (see [ThemeDB.fallback_font_size](class_themedb.md#class-themedb-property-fallback-font-size)).

---


<a id="class-theme-method-get-font-size-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_size_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-font-size-list)

Returns a list of names for font size properties defined with `theme_type`. Use [get_font_size_type_list()](class_theme.md#class-theme-method-get-font-size-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-font-size-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_size_type_list**() const [🔗](class_theme.md#class-theme-method-get-font-size-type-list)

Returns a list of all unique theme type names for font size properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-font-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_type_list**() const [🔗](class_theme.md#class-theme-method-get-font-type-list)

Returns a list of all unique theme type names for [Font](class_font.md#class-font) properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-icon)

Returns the icon property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback icon value if the property doesn't exist (see [ThemeDB.fallback_icon](class_themedb.md#class-themedb-property-fallback-icon)). Use [has_icon()](class_theme.md#class-theme-method-has-icon) to check for existence.

---


<a id="class-theme-method-get-icon-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_icon_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-icon-list)

Returns a list of names for icon properties defined with `theme_type`. Use [get_icon_type_list()](class_theme.md#class-theme-method-get-icon-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-icon-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_icon_type_list**() const [🔗](class_theme.md#class-theme-method-get-icon-type-list)

Returns a list of all unique theme type names for icon properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-stylebox"></a>

[StyleBox](class_stylebox.md#class-stylebox) **get_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-stylebox)

Returns the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback stylebox value if the property doesn't exist (see [ThemeDB.fallback_stylebox](class_themedb.md#class-themedb-property-fallback-stylebox)). Use [has_stylebox()](class_theme.md#class-theme-method-has-stylebox) to check for existence.

---


<a id="class-theme-method-get-stylebox-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_stylebox_list**(theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-stylebox-list)

Returns a list of names for [StyleBox](class_stylebox.md#class-stylebox) properties defined with `theme_type`. Use [get_stylebox_type_list()](class_theme.md#class-theme-method-get-stylebox-type-list) to get a list of possible theme type names.

---


<a id="class-theme-method-get-stylebox-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_stylebox_type_list**() const [🔗](class_theme.md#class-theme-method-get-stylebox-type-list)

Returns a list of all unique theme type names for [StyleBox](class_stylebox.md#class-stylebox) properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

---


<a id="class-theme-method-get-theme-item"></a>

[Variant](class_variant.md#class-variant) **get_theme_item**(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-theme-item)

Returns the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Returns the engine fallback value if the property doesn't exist (see [ThemeDB](class_themedb.md#class-themedb)). Use [has_theme_item()](class_theme.md#class-theme-method-has-theme-item) to check for existence.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-get-theme-item-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_theme_item_list**(data_type: [DataType](class_theme.md#enum-theme-datatype), theme_type: [String](class_string.md#class-string)) const [🔗](class_theme.md#class-theme-method-get-theme-item-list)

Returns a list of names for properties of `data_type` defined with `theme_type`. Use [get_theme_item_type_list()](class_theme.md#class-theme-method-get-theme-item-type-list) to get a list of possible theme type names.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-get-theme-item-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_theme_item_type_list**(data_type: [DataType](class_theme.md#enum-theme-datatype)) const [🔗](class_theme.md#class-theme-method-get-theme-item-type-list)

Returns a list of all unique theme type names for `data_type` properties. Use [get_type_list()](class_theme.md#class-theme-method-get-type-list) to get a list of all unique theme types.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-get-type-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_type_list**() const [🔗](class_theme.md#class-theme-method-get-type-list)

Returns a list of all unique theme type names. Use the appropriate `get_*_type_list` method to get a list of unique theme types for a single data type.

---


<a id="class-theme-method-get-type-variation-base"></a>

[StringName](class_stringname.md#class-stringname) **get_type_variation_base**(theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-type-variation-base)

Returns the name of the base theme type if `theme_type` is a valid variation type. Returns an empty string otherwise.

---


<a id="class-theme-method-get-type-variation-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_type_variation_list**(base_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-get-type-variation-list)

Returns a list of all type variations for the given `base_type`.

---


<a id="class-theme-method-has-color"></a>

[bool](class_bool.md#class-bool) **has_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-color)

Returns `true` if the [Color](class_color.md#class-color) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_color()](class_theme.md#class-theme-method-set-color) to define it.

---


<a id="class-theme-method-has-constant"></a>

[bool](class_bool.md#class-bool) **has_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-constant)

Returns `true` if the constant property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_constant()](class_theme.md#class-theme-method-set-constant) to define it.

---


<a id="class-theme-method-has-default-base-scale"></a>

[bool](class_bool.md#class-bool) **has_default_base_scale**() const [🔗](class_theme.md#class-theme-method-has-default-base-scale)

Returns `true` if [default_base_scale](class_theme.md#class-theme-property-default-base-scale) has a valid value.

Returns `false` if it doesn't. The value must be greater than `0.0` to be considered valid.

---


<a id="class-theme-method-has-default-font"></a>

[bool](class_bool.md#class-bool) **has_default_font**() const [🔗](class_theme.md#class-theme-method-has-default-font)

Returns `true` if [default_font](class_theme.md#class-theme-property-default-font) has a valid value.

Returns `false` if it doesn't.

---


<a id="class-theme-method-has-default-font-size"></a>

[bool](class_bool.md#class-bool) **has_default_font_size**() const [🔗](class_theme.md#class-theme-method-has-default-font-size)

Returns `true` if [default_font_size](class_theme.md#class-theme-property-default-font-size) has a valid value.

Returns `false` if it doesn't. The value must be greater than `0` to be considered valid.

---


<a id="class-theme-method-has-font"></a>

[bool](class_bool.md#class-bool) **has_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-font)

Returns `true` if the [Font](class_font.md#class-font) property defined by `name` and `theme_type` exists, or if the default theme font is set up (see [has_default_font()](class_theme.md#class-theme-method-has-default-font)).

Returns `false` if neither exist. Use [set_font()](class_theme.md#class-theme-method-set-font) to define the property.

---


<a id="class-theme-method-has-font-size"></a>

[bool](class_bool.md#class-bool) **has_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-font-size)

Returns `true` if the font size property defined by `name` and `theme_type` exists, or if the default theme font size is set up (see [has_default_font_size()](class_theme.md#class-theme-method-has-default-font-size)).

Returns `false` if neither exist. Use [set_font_size()](class_theme.md#class-theme-method-set-font-size) to define the property.

---


<a id="class-theme-method-has-icon"></a>

[bool](class_bool.md#class-bool) **has_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-icon)

Returns `true` if the icon property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_icon()](class_theme.md#class-theme-method-set-icon) to define it.

---


<a id="class-theme-method-has-stylebox"></a>

[bool](class_bool.md#class-bool) **has_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-stylebox)

Returns `true` if the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_stylebox()](class_theme.md#class-theme-method-set-stylebox) to define it.

---


<a id="class-theme-method-has-theme-item"></a>

[bool](class_bool.md#class-bool) **has_theme_item**(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-has-theme-item)

Returns `true` if the theme property of `data_type` defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_theme_item()](class_theme.md#class-theme-method-set-theme-item) to define it.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-is-type-variation"></a>

[bool](class_bool.md#class-bool) **is_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname)) const [🔗](class_theme.md#class-theme-method-is-type-variation)

Returns `true` if `theme_type` is marked as a variation of `base_type`.

---


<a id="class-theme-method-merge-with"></a>

void **merge_with**(other: [Theme](class_theme.md#class-theme)) [🔗](class_theme.md#class-theme-method-merge-with)

Adds missing and overrides existing definitions with values from the `other` theme resource.

**Note:** This modifies the current theme. If you want to merge two themes together without modifying either one, create a new empty theme and merge the other two into it one after another.

---


<a id="class-theme-method-remove-type"></a>

void **remove_type**(theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-remove-type)

Removes the theme type, gracefully discarding defined theme items. If the type is a variation, this information is also erased. If the type is a base for type variations, those variations lose their base.

---


<a id="class-theme-method-rename-color"></a>

void **rename_color**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-color)

Renames the [Color](class_color.md#class-color) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_color()](class_theme.md#class-theme-method-has-color) to check for existence, and [clear_color()](class_theme.md#class-theme-method-clear-color) to remove the existing property.

---


<a id="class-theme-method-rename-constant"></a>

void **rename_constant**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-constant)

Renames the constant property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_constant()](class_theme.md#class-theme-method-has-constant) to check for existence, and [clear_constant()](class_theme.md#class-theme-method-clear-constant) to remove the existing property.

---


<a id="class-theme-method-rename-font"></a>

void **rename_font**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-font)

Renames the [Font](class_font.md#class-font) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_font()](class_theme.md#class-theme-method-has-font) to check for existence, and [clear_font()](class_theme.md#class-theme-method-clear-font) to remove the existing property.

---


<a id="class-theme-method-rename-font-size"></a>

void **rename_font_size**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-font-size)

Renames the font size property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_font_size()](class_theme.md#class-theme-method-has-font-size) to check for existence, and [clear_font_size()](class_theme.md#class-theme-method-clear-font-size) to remove the existing property.

---


<a id="class-theme-method-rename-icon"></a>

void **rename_icon**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-icon)

Renames the icon property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_icon()](class_theme.md#class-theme-method-has-icon) to check for existence, and [clear_icon()](class_theme.md#class-theme-method-clear-icon) to remove the existing property.

---


<a id="class-theme-method-rename-stylebox"></a>

void **rename_stylebox**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-stylebox)

Renames the [StyleBox](class_stylebox.md#class-stylebox) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_stylebox()](class_theme.md#class-theme-method-has-stylebox) to check for existence, and [clear_stylebox()](class_theme.md#class-theme-method-clear-stylebox) to remove the existing property.

---


<a id="class-theme-method-rename-theme-item"></a>

void **rename_theme_item**(data_type: [DataType](class_theme.md#enum-theme-datatype), old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-theme-item)

Renames the theme property of `data_type` defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_theme_item()](class_theme.md#class-theme-method-has-theme-item) to check for existence, and [clear_theme_item()](class_theme.md#class-theme-method-clear-theme-item) to remove the existing property.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-rename-type"></a>

void **rename_type**(old_theme_type: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-rename-type)

Renames the theme type `old_theme_type` to `theme_type`, if the old type exists and the new one doesn't exist.

**Note:** Renaming a theme type to an empty name or a variation to a type associated with a built-in class removes type variation connections in a way that cannot be undone by reversing the rename alone.

---


<a id="class-theme-method-set-color"></a>

void **set_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color)) [🔗](class_theme.md#class-theme-method-set-color)

Creates or changes the value of the [Color](class_color.md#class-color) property defined by `name` and `theme_type`. Use [clear_color()](class_theme.md#class-theme-method-clear-color) to remove the property.

---


<a id="class-theme-method-set-constant"></a>

void **set_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), constant: [int](class_int.md#class-int)) [🔗](class_theme.md#class-theme-method-set-constant)

Creates or changes the value of the constant property defined by `name` and `theme_type`. Use [clear_constant()](class_theme.md#class-theme-method-clear-constant) to remove the property.

---


<a id="class-theme-method-set-font"></a>

void **set_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font: [Font](class_font.md#class-font)) [🔗](class_theme.md#class-theme-method-set-font)

Creates or changes the value of the [Font](class_font.md#class-font) property defined by `name` and `theme_type`. Use [clear_font()](class_theme.md#class-theme-method-clear-font) to remove the property.

---


<a id="class-theme-method-set-font-size"></a>

void **set_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font_size: [int](class_int.md#class-int)) [🔗](class_theme.md#class-theme-method-set-font-size)

Creates or changes the value of the font size property defined by `name` and `theme_type`. Use [clear_font_size()](class_theme.md#class-theme-method-clear-font-size) to remove the property.

---


<a id="class-theme-method-set-icon"></a>

void **set_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_theme.md#class-theme-method-set-icon)

Creates or changes the value of the icon property defined by `name` and `theme_type`. Use [clear_icon()](class_theme.md#class-theme-method-clear-icon) to remove the property.

---


<a id="class-theme-method-set-stylebox"></a>

void **set_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [StyleBox](class_stylebox.md#class-stylebox)) [🔗](class_theme.md#class-theme-method-set-stylebox)

Creates or changes the value of the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`. Use [clear_stylebox()](class_theme.md#class-theme-method-clear-stylebox) to remove the property.

---


<a id="class-theme-method-set-theme-item"></a>

void **set_theme_item**(data_type: [DataType](class_theme.md#enum-theme-datatype), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_theme.md#class-theme-method-set-theme-item)

Creates or changes the value of the theme property of `data_type` defined by `name` and `theme_type`. Use [clear_theme_item()](class_theme.md#class-theme-method-clear-theme-item) to remove the property.

Fails if the `value` type is not accepted by `data_type`.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---


<a id="class-theme-method-set-type-variation"></a>

void **set_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname)) [🔗](class_theme.md#class-theme-method-set-type-variation)

Marks `theme_type` as a variation of `base_type`.

This adds `theme_type` as a suggested option for [Control.theme_type_variation](class_control.md#class-control-property-theme-type-variation) on a [Control](class_control.md#class-control) that is of the `base_type` class.

Variations can also be nested, i.e. `base_type` can be another variation. If a chain of variations ends with a `base_type` matching the class of the [Control](class_control.md#class-control), the whole chain is going to be suggested as options.

**Note:** Suggestions only show up if this theme resource is set as the project default theme. See [ProjectSettings.gui/theme/custom](class_projectsettings.md#class-projectsettings-property-gui-theme-custom).
