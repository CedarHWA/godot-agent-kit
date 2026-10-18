> Source: https://docs.godotengine.org/en/4.7/classes/class_translationserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="translationserver"></a>

<a id="class-translationserver"></a>

# TranslationServer

**Inherits:** [Object](class_object.md#class-object)

The server responsible for language translations.

<a id="description"></a>

## Description

The translation server is the API backend that manages all language translations.

Translations are stored in [TranslationDomain](class_translationdomain.md#class-translationdomain)s, which can be accessed by name. The most commonly used translation domain is the main translation domain. It always exists and can be accessed using an empty [StringName](class_stringname.md#class-stringname). The translation server provides wrapper methods for accessing the main translation domain directly, without having to fetch the translation domain first. Custom translation domains are mainly for advanced usages like editor plugins. Names starting with `godot.` are reserved for engine internals.

<a id="tutorials"></a>

## Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)
- [Locales](../tutorials/i18n/locales.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [pseudolocalization_enabled](class_translationserver.md#class-translationserver-property-pseudolocalization-enabled) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_translation](class_translationserver.md#class-translationserver-method-add-translation)(translation: [Translation](class_translation.md#class-translation)) |
| void | [clear](class_translationserver.md#class-translationserver-method-clear)() |
| [int](class_int.md#class-int) | [compare_locales](class_translationserver.md#class-translationserver-method-compare-locales)(locale_a: [String](class_string.md#class-string), locale_b: [String](class_string.md#class-string)) const |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | [find_translations](class_translationserver.md#class-translationserver-method-find-translations)(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const |
| [String](class_string.md#class-string) | [format_number](class_translationserver.md#class-translationserver-method-format-number)(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_all_countries](class_translationserver.md#class-translationserver-method-get-all-countries)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_all_languages](class_translationserver.md#class-translationserver-method-get-all-languages)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_all_scripts](class_translationserver.md#class-translationserver-method-get-all-scripts)() const |
| [String](class_string.md#class-string) | [get_country_name](class_translationserver.md#class-translationserver-method-get-country-name)(country: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_language_name](class_translationserver.md#class-translationserver-method-get-language-name)(language: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_loaded_locales](class_translationserver.md#class-translationserver-method-get-loaded-locales)() const |
| [String](class_string.md#class-string) | [get_locale](class_translationserver.md#class-translationserver-method-get-locale)() const |
| [String](class_string.md#class-string) | [get_locale_name](class_translationserver.md#class-translationserver-method-get-locale-name)(locale: [String](class_string.md#class-string)) const |
| [TranslationDomain](class_translationdomain.md#class-translationdomain) | [get_or_add_domain](class_translationserver.md#class-translationserver-method-get-or-add-domain)(domain: [StringName](class_stringname.md#class-stringname)) |
| [String](class_string.md#class-string) | [get_percent_sign](class_translationserver.md#class-translationserver-method-get-percent-sign)(locale: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_plural_rules](class_translationserver.md#class-translationserver-method-get-plural-rules)(locale: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_script_name](class_translationserver.md#class-translationserver-method-get-script-name)(script: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_tool_locale](class_translationserver.md#class-translationserver-method-get-tool-locale)() |
| [Translation](class_translation.md#class-translation) | [get_translation_object](class_translationserver.md#class-translationserver-method-get-translation-object)(locale: [String](class_string.md#class-string)) |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | [get_translations](class_translationserver.md#class-translationserver-method-get-translations)() const |
| [bool](class_bool.md#class-bool) | [has_domain](class_translationserver.md#class-translationserver-method-has-domain)(domain: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_translation](class_translationserver.md#class-translationserver-method-has-translation)(translation: [Translation](class_translation.md#class-translation)) const |
| [bool](class_bool.md#class-bool) | [has_translation_for_locale](class_translationserver.md#class-translationserver-method-has-translation-for-locale)(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const |
| [String](class_string.md#class-string) | [parse_number](class_translationserver.md#class-translationserver-method-parse-number)(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string)) const |
| [StringName](class_stringname.md#class-stringname) | [pseudolocalize](class_translationserver.md#class-translationserver-method-pseudolocalize)(message: [StringName](class_stringname.md#class-stringname)) const |
| void | [reload_pseudolocalization](class_translationserver.md#class-translationserver-method-reload-pseudolocalization)() |
| void | [remove_domain](class_translationserver.md#class-translationserver-method-remove-domain)(domain: [StringName](class_stringname.md#class-stringname)) |
| void | [remove_translation](class_translationserver.md#class-translationserver-method-remove-translation)(translation: [Translation](class_translation.md#class-translation)) |
| void | [set_locale](class_translationserver.md#class-translationserver-method-set-locale)(locale: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [standardize_locale](class_translationserver.md#class-translationserver-method-standardize-locale)(locale: [String](class_string.md#class-string), add_defaults: [bool](class_bool.md#class-bool) = false) const |
| [StringName](class_stringname.md#class-stringname) | [translate](class_translationserver.md#class-translationserver-method-translate)(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const |
| [StringName](class_stringname.md#class-stringname) | [translate_plural](class_translationserver.md#class-translationserver-method-translate-plural)(message: [StringName](class_stringname.md#class-stringname), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-translationserver-property-pseudolocalization-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_enabled** = `false` [🔗](class_translationserver.md#class-translationserver-property-pseudolocalization-enabled)

- void **set_pseudolocalization_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_enabled**()

If `true`, enables the use of pseudolocalization on the main translation domain. See [ProjectSettings.internationalization/pseudolocalization/use_pseudolocalization](class_projectsettings.md#class-projectsettings-property-internationalization-pseudolocalization-use-pseudolocalization) for details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-translationserver-method-add-translation"></a>

void **add_translation**(translation: [Translation](class_translation.md#class-translation)) [🔗](class_translationserver.md#class-translationserver-method-add-translation)

Adds a translation to the main translation domain.

---


<a id="class-translationserver-method-clear"></a>

void **clear**() [🔗](class_translationserver.md#class-translationserver-method-clear)

Removes all translations from the main translation domain.

---


<a id="class-translationserver-method-compare-locales"></a>

[int](class_int.md#class-int) **compare_locales**(locale_a: [String](class_string.md#class-string), locale_b: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-compare-locales)

Compares two locales and returns a similarity score between `0` (no match) and `10` (full match).

---


<a id="class-translationserver-method-find-translations"></a>

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **find_translations**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const [🔗](class_translationserver.md#class-translationserver-method-find-translations)

Returns the [Translation](class_translation.md#class-translation) instances in the main translation domain that match `locale` (see [compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---


<a id="class-translationserver-method-format-number"></a>

[String](class_string.md#class-string) **format_number**(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-format-number)

Converts a number from Western Arabic (0..9) to the numeral system used in the given `locale`.

---


<a id="class-translationserver-method-get-all-countries"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_countries**() const [🔗](class_translationserver.md#class-translationserver-method-get-all-countries)

Returns an array of known country codes.

---


<a id="class-translationserver-method-get-all-languages"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_languages**() const [🔗](class_translationserver.md#class-translationserver-method-get-all-languages)

Returns array of known language codes.

---


<a id="class-translationserver-method-get-all-scripts"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_scripts**() const [🔗](class_translationserver.md#class-translationserver-method-get-all-scripts)

Returns an array of known script codes.

---


<a id="class-translationserver-method-get-country-name"></a>

[String](class_string.md#class-string) **get_country_name**(country: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-country-name)

Returns a readable country name for the `country` code.

---


<a id="class-translationserver-method-get-language-name"></a>

[String](class_string.md#class-string) **get_language_name**(language: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-language-name)

Returns a readable language name for the `language` code.

---


<a id="class-translationserver-method-get-loaded-locales"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_loaded_locales**() const [🔗](class_translationserver.md#class-translationserver-method-get-loaded-locales)

Returns an array of all loaded locales of the project.

---


<a id="class-translationserver-method-get-locale"></a>

[String](class_string.md#class-string) **get_locale**() const [🔗](class_translationserver.md#class-translationserver-method-get-locale)

Returns the current locale of the project.

See also [OS.get_locale()](class_os.md#class-os-method-get-locale) and [OS.get_locale_language()](class_os.md#class-os-method-get-locale-language) to query the locale of the user system.

---


<a id="class-translationserver-method-get-locale-name"></a>

[String](class_string.md#class-string) **get_locale_name**(locale: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-locale-name)

Returns a locale's language and its variant (e.g. `"en_US"` would return `"English (United States)"`).

---


<a id="class-translationserver-method-get-or-add-domain"></a>

[TranslationDomain](class_translationdomain.md#class-translationdomain) **get_or_add_domain**(domain: [StringName](class_stringname.md#class-stringname)) [🔗](class_translationserver.md#class-translationserver-method-get-or-add-domain)

Returns the translation domain with the specified name. An empty translation domain will be created and added if it does not exist.

---


<a id="class-translationserver-method-get-percent-sign"></a>

[String](class_string.md#class-string) **get_percent_sign**(locale: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-percent-sign)

Returns the percent sign used in the given `locale`.

---


<a id="class-translationserver-method-get-plural-rules"></a>

[String](class_string.md#class-string) **get_plural_rules**(locale: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-plural-rules)

Returns the default plural rules for the `locale`.

---


<a id="class-translationserver-method-get-script-name"></a>

[String](class_string.md#class-string) **get_script_name**(script: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-get-script-name)

Returns a readable script name for the `script` code.

---


<a id="class-translationserver-method-get-tool-locale"></a>

[String](class_string.md#class-string) **get_tool_locale**() [🔗](class_translationserver.md#class-translationserver-method-get-tool-locale)

Returns the current locale of the editor.

**Note:** When called from an exported project returns the same value as [get_locale()](class_translationserver.md#class-translationserver-method-get-locale).

---


<a id="class-translationserver-method-get-translation-object"></a>

[Translation](class_translation.md#class-translation) **get_translation_object**(locale: [String](class_string.md#class-string)) [🔗](class_translationserver.md#class-translationserver-method-get-translation-object)

**Deprecated:** Use [find_translations()](class_translationserver.md#class-translationserver-method-find-translations) instead.

Returns the [Translation](class_translation.md#class-translation) instance that best matches `locale` in the main translation domain. Returns `null` if there are no matches.

---


<a id="class-translationserver-method-get-translations"></a>

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **get_translations**() const [🔗](class_translationserver.md#class-translationserver-method-get-translations)

Returns all available [Translation](class_translation.md#class-translation) instances in the main translation domain as added by [add_translation()](class_translationserver.md#class-translationserver-method-add-translation).

---


<a id="class-translationserver-method-has-domain"></a>

[bool](class_bool.md#class-bool) **has_domain**(domain: [StringName](class_stringname.md#class-stringname)) const [🔗](class_translationserver.md#class-translationserver-method-has-domain)

Returns `true` if a translation domain with the specified name exists.

---


<a id="class-translationserver-method-has-translation"></a>

[bool](class_bool.md#class-bool) **has_translation**(translation: [Translation](class_translation.md#class-translation)) const [🔗](class_translationserver.md#class-translationserver-method-has-translation)

Returns `true` if the main translation domain contains the given `translation`.

---


<a id="class-translationserver-method-has-translation-for-locale"></a>

[bool](class_bool.md#class-bool) **has_translation_for_locale**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const [🔗](class_translationserver.md#class-translationserver-method-has-translation-for-locale)

Returns `true` if there are any [Translation](class_translation.md#class-translation) instances in the main translation domain that match `locale` (see [compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---


<a id="class-translationserver-method-parse-number"></a>

[String](class_string.md#class-string) **parse_number**(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string)) const [🔗](class_translationserver.md#class-translationserver-method-parse-number)

Converts `number` from the numeral system used in the given `locale` to Western Arabic (0..9).

---


<a id="class-translationserver-method-pseudolocalize"></a>

[StringName](class_stringname.md#class-stringname) **pseudolocalize**(message: [StringName](class_stringname.md#class-stringname)) const [🔗](class_translationserver.md#class-translationserver-method-pseudolocalize)

Returns the pseudolocalized string based on the `message` passed in.

**Note:** This method always uses the main translation domain.

---


<a id="class-translationserver-method-reload-pseudolocalization"></a>

void **reload_pseudolocalization**() [🔗](class_translationserver.md#class-translationserver-method-reload-pseudolocalization)

Reparses the pseudolocalization options and reloads the translation for the main translation domain.

---


<a id="class-translationserver-method-remove-domain"></a>

void **remove_domain**(domain: [StringName](class_stringname.md#class-stringname)) [🔗](class_translationserver.md#class-translationserver-method-remove-domain)

Removes the translation domain with the specified name.

**Note:** Trying to remove the main translation domain is an error.

---


<a id="class-translationserver-method-remove-translation"></a>

void **remove_translation**(translation: [Translation](class_translation.md#class-translation)) [🔗](class_translationserver.md#class-translationserver-method-remove-translation)

Removes the given translation from the main translation domain.

---


<a id="class-translationserver-method-set-locale"></a>

void **set_locale**(locale: [String](class_string.md#class-string)) [🔗](class_translationserver.md#class-translationserver-method-set-locale)

Sets the locale of the project. The `locale` string will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

If translations have been loaded beforehand for the new locale, they will be applied.

---


<a id="class-translationserver-method-standardize-locale"></a>

[String](class_string.md#class-string) **standardize_locale**(locale: [String](class_string.md#class-string), add_defaults: [bool](class_bool.md#class-bool) = false) const [🔗](class_translationserver.md#class-translationserver-method-standardize-locale)

Returns a `locale` string standardized to match known locales (e.g. `en-US` would be matched to `en_US`). If `add_defaults` is `true`, the locale may have a default script or country added.

---


<a id="class-translationserver-method-translate"></a>

[StringName](class_stringname.md#class-stringname) **translate**(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translationserver.md#class-translationserver-method-translate)

Returns the current locale's translation for the given message and context.

**Note:** This method always uses the main translation domain.

---


<a id="class-translationserver-method-translate-plural"></a>

[StringName](class_stringname.md#class-stringname) **translate_plural**(message: [StringName](class_stringname.md#class-stringname), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translationserver.md#class-translationserver-method-translate-plural)

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

**Note:** This method always uses the main translation domain.
