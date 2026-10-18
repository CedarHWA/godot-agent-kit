> Source: https://docs.godotengine.org/en/4.7/classes/class_scriptextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scriptextension"></a>

<a id="class-scriptextension"></a>

# ScriptExtension

**Inherits:** [Script](class_script.md#class-script) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_can_instantiate](class_scriptextension.md#class-scriptextension-private-method-can-instantiate)() virtual required const |
| [bool](class_bool.md#class-bool) | [_editor_can_reload_from_file](class_scriptextension.md#class-scriptextension-private-method-editor-can-reload-from-file)() virtual required |
| [Script](class_script.md#class-script) | [_get_base_script](class_scriptextension.md#class-scriptextension-private-method-get-base-script)() virtual required const |
| [String](class_string.md#class-string) | [_get_class_icon_path](class_scriptextension.md#class-scriptextension-private-method-get-class-icon-path)() virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_constants](class_scriptextension.md#class-scriptextension-private-method-get-constants)() virtual required const |
| [StringName](class_stringname.md#class-stringname) | [_get_doc_class_name](class_scriptextension.md#class-scriptextension-private-method-get-doc-class-name)() virtual required const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_documentation](class_scriptextension.md#class-scriptextension-private-method-get-documentation)() virtual required const |
| [StringName](class_stringname.md#class-stringname) | [_get_global_name](class_scriptextension.md#class-scriptextension-private-method-get-global-name)() virtual required const |
| [StringName](class_stringname.md#class-stringname) | [_get_instance_base_type](class_scriptextension.md#class-scriptextension-private-method-get-instance-base-type)() virtual required const |
| [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage) | [_get_language](class_scriptextension.md#class-scriptextension-private-method-get-language)() virtual required const |
| [int](class_int.md#class-int) | [_get_member_line](class_scriptextension.md#class-scriptextension-private-method-get-member-line)(member: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | [_get_members](class_scriptextension.md#class-scriptextension-private-method-get-members)() virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_method_info](class_scriptextension.md#class-scriptextension-private-method-get-method-info)(method: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_get_property_default_value](class_scriptextension.md#class-scriptextension-private-method-get-property-default-value)(property: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_get_rpc_config](class_scriptextension.md#class-scriptextension-private-method-get-rpc-config)() virtual required const |
| [Variant](class_variant.md#class-variant) | [_get_script_method_argument_count](class_scriptextension.md#class-scriptextension-private-method-get-script-method-argument-count)(method: [StringName](class_stringname.md#class-stringname)) virtual const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_script_method_list](class_scriptextension.md#class-scriptextension-private-method-get-script-method-list)() virtual required const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_script_property_list](class_scriptextension.md#class-scriptextension-private-method-get-script-property-list)() virtual required const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_script_signal_list](class_scriptextension.md#class-scriptextension-private-method-get-script-signal-list)() virtual required const |
| [String](class_string.md#class-string) | [_get_source_code](class_scriptextension.md#class-scriptextension-private-method-get-source-code)() virtual required const |
| [bool](class_bool.md#class-bool) | [_has_method](class_scriptextension.md#class-scriptextension-private-method-has-method)(method: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [bool](class_bool.md#class-bool) | [_has_property_default_value](class_scriptextension.md#class-scriptextension-private-method-has-property-default-value)(property: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [bool](class_bool.md#class-bool) | [_has_script_signal](class_scriptextension.md#class-scriptextension-private-method-has-script-signal)(signal: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [bool](class_bool.md#class-bool) | [_has_source_code](class_scriptextension.md#class-scriptextension-private-method-has-source-code)() virtual required const |
| [bool](class_bool.md#class-bool) | [_has_static_method](class_scriptextension.md#class-scriptextension-private-method-has-static-method)(method: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [bool](class_bool.md#class-bool) | [_inherits_script](class_scriptextension.md#class-scriptextension-private-method-inherits-script)(script: [Script](class_script.md#class-script)) virtual required const |
| `void*` | [_instance_create](class_scriptextension.md#class-scriptextension-private-method-instance-create)(for_object: [Object](class_object.md#class-object)) virtual required const |
| [bool](class_bool.md#class-bool) | [_instance_has](class_scriptextension.md#class-scriptextension-private-method-instance-has)(object: [Object](class_object.md#class-object)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_abstract](class_scriptextension.md#class-scriptextension-private-method-is-abstract)() virtual const |
| [bool](class_bool.md#class-bool) | [_is_placeholder_fallback_enabled](class_scriptextension.md#class-scriptextension-private-method-is-placeholder-fallback-enabled)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_tool](class_scriptextension.md#class-scriptextension-private-method-is-tool)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_valid](class_scriptextension.md#class-scriptextension-private-method-is-valid)() virtual required const |
| void | [_placeholder_erased](class_scriptextension.md#class-scriptextension-private-method-placeholder-erased)(placeholder: `void*`) virtual |
| `void*` | [_placeholder_instance_create](class_scriptextension.md#class-scriptextension-private-method-placeholder-instance-create)(for_object: [Object](class_object.md#class-object)) virtual required const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_reload](class_scriptextension.md#class-scriptextension-private-method-reload)(keep_state: [bool](class_bool.md#class-bool)) virtual required |
| void | [_set_source_code](class_scriptextension.md#class-scriptextension-private-method-set-source-code)(code: [String](class_string.md#class-string)) virtual required |
| void | [_update_exports](class_scriptextension.md#class-scriptextension-private-method-update-exports)() virtual required |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scriptextension-private-method-can-instantiate"></a>

[bool](class_bool.md#class-bool) **_can_instantiate**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-can-instantiate)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-editor-can-reload-from-file"></a>

[bool](class_bool.md#class-bool) **_editor_can_reload_from_file**() virtual required [🔗](class_scriptextension.md#class-scriptextension-private-method-editor-can-reload-from-file)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-base-script"></a>

[Script](class_script.md#class-script) **_get_base_script**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-base-script)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-class-icon-path"></a>

[String](class_string.md#class-string) **_get_class_icon_path**() virtual const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-class-icon-path)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-constants"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_constants**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-constants)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-doc-class-name"></a>

[StringName](class_stringname.md#class-stringname) **_get_doc_class_name**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-doc-class-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-documentation"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_documentation**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-documentation)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-global-name"></a>

[StringName](class_stringname.md#class-stringname) **_get_global_name**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-global-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-instance-base-type"></a>

[StringName](class_stringname.md#class-stringname) **_get_instance_base_type**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-instance-base-type)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-language"></a>

[ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage) **_get_language**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-language)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-member-line"></a>

[int](class_int.md#class-int) **_get_member_line**(member: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-member-line)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-members"></a>

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **_get_members**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-members)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-method-info"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_method_info**(method: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-method-info)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-property-default-value"></a>

[Variant](class_variant.md#class-variant) **_get_property_default_value**(property: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-property-default-value)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-rpc-config"></a>

[Variant](class_variant.md#class-variant) **_get_rpc_config**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-rpc-config)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-script-method-argument-count"></a>

[Variant](class_variant.md#class-variant) **_get_script_method_argument_count**(method: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-script-method-argument-count)

Return the expected argument count for the given `method`, or `null` if it can't be determined (which will then fall back to the default behavior).

---


<a id="class-scriptextension-private-method-get-script-method-list"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_script_method_list**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-script-method-list)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-script-property-list"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_script_property_list**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-script-property-list)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-script-signal-list"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_script_signal_list**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-script-signal-list)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-get-source-code"></a>

[String](class_string.md#class-string) **_get_source_code**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-get-source-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-has-method"></a>

[bool](class_bool.md#class-bool) **_has_method**(method: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-has-method)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-has-property-default-value"></a>

[bool](class_bool.md#class-bool) **_has_property_default_value**(property: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-has-property-default-value)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-has-script-signal"></a>

[bool](class_bool.md#class-bool) **_has_script_signal**(signal: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-has-script-signal)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-has-source-code"></a>

[bool](class_bool.md#class-bool) **_has_source_code**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-has-source-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-has-static-method"></a>

[bool](class_bool.md#class-bool) **_has_static_method**(method: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-has-static-method)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-inherits-script"></a>

[bool](class_bool.md#class-bool) **_inherits_script**(script: [Script](class_script.md#class-script)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-inherits-script)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-instance-create"></a>

`void*` **_instance_create**(for_object: [Object](class_object.md#class-object)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-instance-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-instance-has"></a>

[bool](class_bool.md#class-bool) **_instance_has**(object: [Object](class_object.md#class-object)) virtual const [🔗](class_scriptextension.md#class-scriptextension-private-method-instance-has)

**Deprecated:** This method is not called by the engine.

---


<a id="class-scriptextension-private-method-is-abstract"></a>

[bool](class_bool.md#class-bool) **_is_abstract**() virtual const [🔗](class_scriptextension.md#class-scriptextension-private-method-is-abstract)

Returns `true` if the script is an abstract script. Abstract scripts cannot be instantiated directly, instead other scripts should inherit them. Abstract scripts will be either unselectable or hidden in the Create New Node dialog (unselectable if there are non-abstract classes inheriting it, otherwise hidden).

---


<a id="class-scriptextension-private-method-is-placeholder-fallback-enabled"></a>

[bool](class_bool.md#class-bool) **_is_placeholder_fallback_enabled**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-is-placeholder-fallback-enabled)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-is-tool"></a>

[bool](class_bool.md#class-bool) **_is_tool**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-is-tool)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-is-valid"></a>

[bool](class_bool.md#class-bool) **_is_valid**() virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-is-valid)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-placeholder-erased"></a>

void **_placeholder_erased**(placeholder: `void*`) virtual [🔗](class_scriptextension.md#class-scriptextension-private-method-placeholder-erased)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-placeholder-instance-create"></a>

`void*` **_placeholder_instance_create**(for_object: [Object](class_object.md#class-object)) virtual required const [🔗](class_scriptextension.md#class-scriptextension-private-method-placeholder-instance-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-reload"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_reload**(keep_state: [bool](class_bool.md#class-bool)) virtual required [🔗](class_scriptextension.md#class-scriptextension-private-method-reload)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-set-source-code"></a>

void **_set_source_code**(code: [String](class_string.md#class-string)) virtual required [🔗](class_scriptextension.md#class-scriptextension-private-method-set-source-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptextension-private-method-update-exports"></a>

void **_update_exports**() virtual required [🔗](class_scriptextension.md#class-scriptextension-private-method-update-exports)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
