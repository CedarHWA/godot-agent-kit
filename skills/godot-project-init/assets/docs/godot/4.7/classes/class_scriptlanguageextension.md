> Source: https://docs.godotengine.org/en/4.7/classes/class_scriptlanguageextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scriptlanguageextension"></a>

<a id="class-scriptlanguageextension"></a>

# ScriptLanguageExtension

**Inherits:** [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_add_global_constant](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-add-global-constant)(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_add_named_global_constant](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-add-named-global-constant)(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual required |
| [String](class_string.md#class-string) | [_auto_indent_code](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-auto-indent-code)(code: [String](class_string.md#class-string), from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int)) virtual required const |
| [bool](class_bool.md#class-bool) | [_can_inherit_from_file](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-can-inherit-from-file)() virtual required const |
| [bool](class_bool.md#class-bool) | [_can_make_function](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-can-make-function)() virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_complete_code](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-complete-code)(code: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object)) virtual required const |
| [Object](class_object.md#class-object) | [_create_script](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-create-script)() virtual const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_debug_get_current_stack_info](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-current-stack-info)() virtual required |
| [String](class_string.md#class-string) | [_debug_get_error](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-error)() virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_debug_get_globals](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-globals)(max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required |
| [int](class_int.md#class-int) | [_debug_get_stack_level_count](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-count)() virtual required const |
| [String](class_string.md#class-string) | [_debug_get_stack_level_function](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-function)(level: [int](class_int.md#class-int)) virtual required const |
| `void*` | [_debug_get_stack_level_instance](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-instance)(level: [int](class_int.md#class-int)) virtual required |
| [int](class_int.md#class-int) | [_debug_get_stack_level_line](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-line)(level: [int](class_int.md#class-int)) virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_debug_get_stack_level_locals](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-locals)(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required |
| [Dictionary](class_dictionary.md#class-dictionary) | [_debug_get_stack_level_members](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-members)(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required |
| [String](class_string.md#class-string) | [_debug_get_stack_level_source](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-source)(level: [int](class_int.md#class-int)) virtual required const |
| [String](class_string.md#class-string) | [_debug_parse_stack_level_expression](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-parse-stack-level-expression)(level: [int](class_int.md#class-int), expression: [String](class_string.md#class-string), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required |
| [int](class_int.md#class-int) | [_find_function](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-find-function)(function: [String](class_string.md#class-string), code: [String](class_string.md#class-string)) virtual required const |
| void | [_finish](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-finish)() virtual required |
| void | [_frame](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-frame)() virtual required |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_built_in_templates](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-built-in-templates)(object: [StringName](class_stringname.md#class-stringname)) virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_comment_delimiters](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-comment-delimiters)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_doc_comment_delimiters](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-doc-comment-delimiters)() virtual const |
| [String](class_string.md#class-string) | [_get_extension](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-extension)() virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_global_class_name](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-global-class-name)(path: [String](class_string.md#class-string)) virtual required const |
| [String](class_string.md#class-string) | [_get_name](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-name)() virtual required const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_public_annotations](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-annotations)() virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_public_constants](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-constants)() virtual required const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_public_functions](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-functions)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_recognized_extensions](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-recognized-extensions)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_reserved_words](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-reserved-words)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_string_delimiters](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-string-delimiters)() virtual required const |
| [String](class_string.md#class-string) | [_get_type](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-type)() virtual required const |
| [bool](class_bool.md#class-bool) | [_handles_global_class_type](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-handles-global-class-type)(type: [String](class_string.md#class-string)) virtual required const |
| [bool](class_bool.md#class-bool) | [_has_named_classes](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-has-named-classes)() virtual const |
| void | [_init](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-init)() virtual required |
| [bool](class_bool.md#class-bool) | [_is_control_flow_keyword](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-is-control-flow-keyword)(keyword: [String](class_string.md#class-string)) virtual required const |
| [bool](class_bool.md#class-bool) | [_is_using_templates](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-is-using-templates)() virtual required |
| [Dictionary](class_dictionary.md#class-dictionary) | [_lookup_code](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-lookup-code)(code: [String](class_string.md#class-string), symbol: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object)) virtual required const |
| [String](class_string.md#class-string) | [_make_function](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-make-function)(class_name: [String](class_string.md#class-string), function_name: [String](class_string.md#class-string), function_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual required const |
| [Script](class_script.md#class-script) | [_make_template](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-make-template)(template: [String](class_string.md#class-string), class_name: [String](class_string.md#class-string), base_class_name: [String](class_string.md#class-string)) virtual required const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_open_in_external_editor](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-open-in-external-editor)(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_overrides_external_editor](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-overrides-external-editor)() virtual required |
| [ScriptNameCasing](class_scriptlanguage.md#enum-scriptlanguage-scriptnamecasing) | [_preferred_file_name_casing](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-preferred-file-name-casing)() virtual const |
| [int](class_int.md#class-int) | [_profiling_get_accumulated_data](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-get-accumulated-data)(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int)) virtual required |
| [int](class_int.md#class-int) | [_profiling_get_frame_data](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-get-frame-data)(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int)) virtual required |
| void | [_profiling_set_save_native_calls](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-set-save-native-calls)(enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_profiling_start](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-start)() virtual required |
| void | [_profiling_stop](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-stop)() virtual required |
| void | [_reload_all_scripts](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-all-scripts)() virtual required |
| void | [_reload_scripts](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-scripts)(scripts: [Array](class_array.md#class-array), soft_reload: [bool](class_bool.md#class-bool)) virtual required |
| void | [_reload_tool_script](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-tool-script)(script: [Script](class_script.md#class-script), soft_reload: [bool](class_bool.md#class-bool)) virtual required |
| void | [_remove_named_global_constant](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-remove-named-global-constant)(name: [StringName](class_stringname.md#class-stringname)) virtual required |
| [bool](class_bool.md#class-bool) | [_supports_builtin_mode](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-supports-builtin-mode)() virtual required const |
| [bool](class_bool.md#class-bool) | [_supports_documentation](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-supports-documentation)() virtual required const |
| void | [_thread_enter](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-thread-enter)() virtual required |
| void | [_thread_exit](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-thread-exit)() virtual required |
| [Dictionary](class_dictionary.md#class-dictionary) | [_validate](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-validate)(script: [String](class_string.md#class-string), path: [String](class_string.md#class-string), validate_functions: [bool](class_bool.md#class-bool), validate_errors: [bool](class_bool.md#class-bool), validate_warnings: [bool](class_bool.md#class-bool), validate_safe_lines: [bool](class_bool.md#class-bool)) virtual required const |
| [String](class_string.md#class-string) | [_validate_path](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-validate-path)(path: [String](class_string.md#class-string)) virtual required const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-scriptlanguageextension-lookupresulttype"></a>

enum **LookupResultType**: [🔗](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype)

<a id="class-scriptlanguageextension-constant-lookup-result-script-location"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_SCRIPT_LOCATION** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-constant"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_CONSTANT** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-property"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_PROPERTY** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-method"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_METHOD** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-signal"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_SIGNAL** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-enum"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_ENUM** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-class-tbd-globalscope"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE** = `7`

**Deprecated:** This constant may be changed or removed in future versions.

<a id="class-scriptlanguageextension-constant-lookup-result-class-annotation"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_CLASS_ANNOTATION** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-local-constant"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_LOCAL_CONSTANT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-local-variable"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_LOCAL_VARIABLE** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-lookup-result-max"></a>

[LookupResultType](class_scriptlanguageextension.md#enum-scriptlanguageextension-lookupresulttype) **LOOKUP_RESULT_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="enum-scriptlanguageextension-codecompletionlocation"></a>

enum **CodeCompletionLocation**: [🔗](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionlocation)

<a id="class-scriptlanguageextension-constant-location-local"></a>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionlocation) **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

<a id="class-scriptlanguageextension-constant-location-parent-mask"></a>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionlocation) **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

<a id="class-scriptlanguageextension-constant-location-other-user-code"></a>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionlocation) **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

<a id="class-scriptlanguageextension-constant-location-other"></a>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionlocation) **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

---


<a id="enum-scriptlanguageextension-codecompletionkind"></a>

enum **CodeCompletionKind**: [🔗](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind)

<a id="class-scriptlanguageextension-constant-code-completion-kind-class"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_CLASS** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-function"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_FUNCTION** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-signal"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_SIGNAL** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-variable"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_VARIABLE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-member"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_MEMBER** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-enum"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_ENUM** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-constant"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_CONSTANT** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-node-path"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_NODE_PATH** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-file-path"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_FILE_PATH** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-plain-text"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_PLAIN_TEXT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-keyword"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_KEYWORD** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-scriptlanguageextension-constant-code-completion-kind-max"></a>

[CodeCompletionKind](class_scriptlanguageextension.md#enum-scriptlanguageextension-codecompletionkind) **CODE_COMPLETION_KIND_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scriptlanguageextension-private-method-add-global-constant"></a>

void **_add_global_constant**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-add-global-constant)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-add-named-global-constant"></a>

void **_add_named_global_constant**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-add-named-global-constant)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-auto-indent-code"></a>

[String](class_string.md#class-string) **_auto_indent_code**(code: [String](class_string.md#class-string), from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-auto-indent-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-can-inherit-from-file"></a>

[bool](class_bool.md#class-bool) **_can_inherit_from_file**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-can-inherit-from-file)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-can-make-function"></a>

[bool](class_bool.md#class-bool) **_can_make_function**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-can-make-function)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-complete-code"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_complete_code**(code: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-complete-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-create-script"></a>

[Object](class_object.md#class-object) **_create_script**() virtual const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-create-script)

**Deprecated:** This method is not called by the engine.

---


<a id="class-scriptlanguageextension-private-method-debug-get-current-stack-info"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_debug_get_current_stack_info**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-current-stack-info)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-error"></a>

[String](class_string.md#class-string) **_debug_get_error**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-error)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-globals"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_debug_get_globals**(max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-globals)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-count"></a>

[int](class_int.md#class-int) **_debug_get_stack_level_count**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-function"></a>

[String](class_string.md#class-string) **_debug_get_stack_level_function**(level: [int](class_int.md#class-int)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-function)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-instance"></a>

`void*` **_debug_get_stack_level_instance**(level: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-instance)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-line"></a>

[int](class_int.md#class-int) **_debug_get_stack_level_line**(level: [int](class_int.md#class-int)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-line)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-locals"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_debug_get_stack_level_locals**(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-locals)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-members"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_debug_get_stack_level_members**(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-members)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-debug-get-stack-level-source"></a>

[String](class_string.md#class-string) **_debug_get_stack_level_source**(level: [int](class_int.md#class-int)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-get-stack-level-source)

Returns the source associated with a given debug stack position.

---


<a id="class-scriptlanguageextension-private-method-debug-parse-stack-level-expression"></a>

[String](class_string.md#class-string) **_debug_parse_stack_level_expression**(level: [int](class_int.md#class-int), expression: [String](class_string.md#class-string), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-debug-parse-stack-level-expression)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-find-function"></a>

[int](class_int.md#class-int) **_find_function**(function: [String](class_string.md#class-string), code: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-find-function)

Returns the line where the function is defined in the code, or `-1` if the function is not present.

---


<a id="class-scriptlanguageextension-private-method-finish"></a>

void **_finish**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-finish)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-frame"></a>

void **_frame**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-frame)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-built-in-templates"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_built_in_templates**(object: [StringName](class_stringname.md#class-stringname)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-built-in-templates)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-comment-delimiters"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_comment_delimiters**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-comment-delimiters)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-doc-comment-delimiters"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_doc_comment_delimiters**() virtual const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-doc-comment-delimiters)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-extension"></a>

[String](class_string.md#class-string) **_get_extension**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-extension)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-global-class-name"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_global_class_name**(path: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-global-class-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-name"></a>

[String](class_string.md#class-string) **_get_name**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-public-annotations"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_public_annotations**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-annotations)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-public-constants"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_public_constants**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-constants)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-public-functions"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_public_functions**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-public-functions)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-recognized-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_recognized_extensions**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-recognized-extensions)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-reserved-words"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_reserved_words**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-reserved-words)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-string-delimiters"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_string_delimiters**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-string-delimiters)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-get-type"></a>

[String](class_string.md#class-string) **_get_type**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-get-type)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-handles-global-class-type"></a>

[bool](class_bool.md#class-bool) **_handles_global_class_type**(type: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-handles-global-class-type)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-has-named-classes"></a>

[bool](class_bool.md#class-bool) **_has_named_classes**() virtual const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-has-named-classes)

**Deprecated:** This method is not called by the engine.

---


<a id="class-scriptlanguageextension-private-method-init"></a>

void **_init**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-init)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-is-control-flow-keyword"></a>

[bool](class_bool.md#class-bool) **_is_control_flow_keyword**(keyword: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-is-control-flow-keyword)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-is-using-templates"></a>

[bool](class_bool.md#class-bool) **_is_using_templates**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-is-using-templates)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-lookup-code"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_lookup_code**(code: [String](class_string.md#class-string), symbol: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-lookup-code)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-make-function"></a>

[String](class_string.md#class-string) **_make_function**(class_name: [String](class_string.md#class-string), function_name: [String](class_string.md#class-string), function_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-make-function)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-make-template"></a>

[Script](class_script.md#class-script) **_make_template**(template: [String](class_string.md#class-string), class_name: [String](class_string.md#class-string), base_class_name: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-make-template)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-open-in-external-editor"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_open_in_external_editor**(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-open-in-external-editor)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-overrides-external-editor"></a>

[bool](class_bool.md#class-bool) **_overrides_external_editor**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-overrides-external-editor)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-preferred-file-name-casing"></a>

[ScriptNameCasing](class_scriptlanguage.md#enum-scriptlanguage-scriptnamecasing) **_preferred_file_name_casing**() virtual const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-preferred-file-name-casing)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-profiling-get-accumulated-data"></a>

[int](class_int.md#class-int) **_profiling_get_accumulated_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-get-accumulated-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-profiling-get-frame-data"></a>

[int](class_int.md#class-int) **_profiling_get_frame_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-get-frame-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-profiling-set-save-native-calls"></a>

void **_profiling_set_save_native_calls**(enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-set-save-native-calls)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-profiling-start"></a>

void **_profiling_start**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-start)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-profiling-stop"></a>

void **_profiling_stop**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-profiling-stop)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-reload-all-scripts"></a>

void **_reload_all_scripts**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-all-scripts)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-reload-scripts"></a>

void **_reload_scripts**(scripts: [Array](class_array.md#class-array), soft_reload: [bool](class_bool.md#class-bool)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-scripts)

Reloads all `scripts` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

---


<a id="class-scriptlanguageextension-private-method-reload-tool-script"></a>

void **_reload_tool_script**(script: [Script](class_script.md#class-script), soft_reload: [bool](class_bool.md#class-bool)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-reload-tool-script)

Reloads the given `script` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

---


<a id="class-scriptlanguageextension-private-method-remove-named-global-constant"></a>

void **_remove_named_global_constant**(name: [StringName](class_stringname.md#class-stringname)) virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-remove-named-global-constant)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-supports-builtin-mode"></a>

[bool](class_bool.md#class-bool) **_supports_builtin_mode**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-supports-builtin-mode)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-supports-documentation"></a>

[bool](class_bool.md#class-bool) **_supports_documentation**() virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-supports-documentation)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-thread-enter"></a>

void **_thread_enter**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-thread-enter)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-thread-exit"></a>

void **_thread_exit**() virtual required [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-thread-exit)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-validate"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_validate**(script: [String](class_string.md#class-string), path: [String](class_string.md#class-string), validate_functions: [bool](class_bool.md#class-bool), validate_errors: [bool](class_bool.md#class-bool), validate_warnings: [bool](class_bool.md#class-bool), validate_safe_lines: [bool](class_bool.md#class-bool)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-validate)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-scriptlanguageextension-private-method-validate-path"></a>

[String](class_string.md#class-string) **_validate_path**(path: [String](class_string.md#class-string)) virtual required const [🔗](class_scriptlanguageextension.md#class-scriptlanguageextension-private-method-validate-path)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
