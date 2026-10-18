> Source: https://docs.godotengine.org/en/4.7/classes/class_translationdomain.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="translationdomain"></a>

<a id="class-translationdomain"></a>

# TranslationDomain

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A self-contained collection of [Translation](class_translation.md#class-translation) resources.

<a id="description"></a>

## Description

**TranslationDomain** is a self-contained collection of [Translation](class_translation.md#class-translation) resources. Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to use the wrap methods on [TranslationServer](class_translationserver.md#class-translationserver).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [enabled](class_translationdomain.md#class-translationdomain-property-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_accents_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-accents-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_double_vowels_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-double-vowels-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-enabled) | `false` |
| [float](class_float.md#class-float) | [pseudolocalization_expansion_ratio](class_translationdomain.md#class-translationdomain-property-pseudolocalization-expansion-ratio) | `0.0` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_fake_bidi_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-fake-bidi-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_override_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-override-enabled) | `false` |
| [String](class_string.md#class-string) | [pseudolocalization_prefix](class_translationdomain.md#class-translationdomain-property-pseudolocalization-prefix) | `"["` |
| [bool](class_bool.md#class-bool) | [pseudolocalization_skip_placeholders_enabled](class_translationdomain.md#class-translationdomain-property-pseudolocalization-skip-placeholders-enabled) | `true` |
| [String](class_string.md#class-string) | [pseudolocalization_suffix](class_translationdomain.md#class-translationdomain-property-pseudolocalization-suffix) | `"]"` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_translation](class_translationdomain.md#class-translationdomain-method-add-translation)(translation: [Translation](class_translation.md#class-translation)) |
| void | [clear](class_translationdomain.md#class-translationdomain-method-clear)() |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | [find_translations](class_translationdomain.md#class-translationdomain-method-find-translations)(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const |
| [String](class_string.md#class-string) | [get_locale_override](class_translationdomain.md#class-translationdomain-method-get-locale-override)() const |
| [Translation](class_translation.md#class-translation) | [get_translation_object](class_translationdomain.md#class-translationdomain-method-get-translation-object)(locale: [String](class_string.md#class-string)) const |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | [get_translations](class_translationdomain.md#class-translationdomain-method-get-translations)() const |
| [bool](class_bool.md#class-bool) | [has_translation](class_translationdomain.md#class-translationdomain-method-has-translation)(translation: [Translation](class_translation.md#class-translation)) const |
| [bool](class_bool.md#class-bool) | [has_translation_for_locale](class_translationdomain.md#class-translationdomain-method-has-translation-for-locale)(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const |
| [StringName](class_stringname.md#class-stringname) | [pseudolocalize](class_translationdomain.md#class-translationdomain-method-pseudolocalize)(message: [StringName](class_stringname.md#class-stringname)) const |
| void | [remove_translation](class_translationdomain.md#class-translationdomain-method-remove-translation)(translation: [Translation](class_translation.md#class-translation)) |
| void | [set_locale_override](class_translationdomain.md#class-translationdomain-method-set-locale-override)(locale: [String](class_string.md#class-string)) |
| [StringName](class_stringname.md#class-stringname) | [translate](class_translationdomain.md#class-translationdomain-method-translate)(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const |
| [StringName](class_stringname.md#class-stringname) | [translate_plural](class_translationdomain.md#class-translationdomain-method-translate-plural)(message: [StringName](class_stringname.md#class-stringname), message_plural: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-translationdomain-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `true` [🔗](class_translationdomain.md#class-translationdomain-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, translation is enabled. Otherwise, [translate()](class_translationdomain.md#class-translationdomain-method-translate) and [translate_plural()](class_translationdomain.md#class-translationdomain-method-translate-plural) will return the input message unchanged regardless of the current locale.

---


<a id="class-translationdomain-property-pseudolocalization-accents-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_accents_enabled** = `true` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-accents-enabled)

- void **set_pseudolocalization_accents_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_accents_enabled**()

Replace all characters with their accented variants during pseudolocalization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-double-vowels-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_double_vowels_enabled** = `false` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-double-vowels-enabled)

- void **set_pseudolocalization_double_vowels_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_double_vowels_enabled**()

Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_enabled** = `false` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-enabled)

- void **set_pseudolocalization_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_enabled**()

If `true`, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-expansion-ratio"></a>

[float](class_float.md#class-float) **pseudolocalization_expansion_ratio** = `0.0` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-expansion-ratio)

- void **set_pseudolocalization_expansion_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pseudolocalization_expansion_ratio**()

The expansion ratio to use during pseudolocalization. A value of `0.3` is sufficient for most practical purposes, and will increase the length of each string by 30%.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-fake-bidi-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_fake_bidi_enabled** = `false` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-fake-bidi-enabled)

- void **set_pseudolocalization_fake_bidi_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_fake_bidi_enabled**()

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-override-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_override_enabled** = `false` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-override-enabled)

- void **set_pseudolocalization_override_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_override_enabled**()

Replace all characters in the string with `*`. Useful for finding non-localizable strings.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-prefix"></a>

[String](class_string.md#class-string) **pseudolocalization_prefix** = `"["` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-prefix)

- void **set_pseudolocalization_prefix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_pseudolocalization_prefix**()

Prefix that will be prepended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-skip-placeholders-enabled"></a>

[bool](class_bool.md#class-bool) **pseudolocalization_skip_placeholders_enabled** = `true` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-skip-placeholders-enabled)

- void **set_pseudolocalization_skip_placeholders_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_skip_placeholders_enabled**()

Skip placeholders for string formatting like `%s` or `%f` during pseudolocalization. Useful to identify strings which need additional control characters to display correctly.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="class-translationdomain-property-pseudolocalization-suffix"></a>

[String](class_string.md#class-string) **pseudolocalization_suffix** = `"]"` [🔗](class_translationdomain.md#class-translationdomain-property-pseudolocalization-suffix)

- void **set_pseudolocalization_suffix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_pseudolocalization_suffix**()

Suffix that will be appended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-translationdomain-method-add-translation"></a>

void **add_translation**(translation: [Translation](class_translation.md#class-translation)) [🔗](class_translationdomain.md#class-translationdomain-method-add-translation)

Adds a translation.

---


<a id="class-translationdomain-method-clear"></a>

void **clear**() [🔗](class_translationdomain.md#class-translationdomain-method-clear)

Removes all translations.

---


<a id="class-translationdomain-method-find-translations"></a>

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **find_translations**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const [🔗](class_translationdomain.md#class-translationdomain-method-find-translations)

Returns the [Translation](class_translation.md#class-translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---


<a id="class-translationdomain-method-get-locale-override"></a>

[String](class_string.md#class-string) **get_locale_override**() const [🔗](class_translationdomain.md#class-translationdomain-method-get-locale-override)

Returns the locale override of the domain. Returns an empty string if locale override is disabled.

---


<a id="class-translationdomain-method-get-translation-object"></a>

[Translation](class_translation.md#class-translation) **get_translation_object**(locale: [String](class_string.md#class-string)) const [🔗](class_translationdomain.md#class-translationdomain-method-get-translation-object)

**Deprecated:** Use [find_translations()](class_translationdomain.md#class-translationdomain-method-find-translations) instead.

Returns the [Translation](class_translation.md#class-translation) instance that best matches `locale`. Returns `null` if there are no matches.

---


<a id="class-translationdomain-method-get-translations"></a>

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **get_translations**() const [🔗](class_translationdomain.md#class-translationdomain-method-get-translations)

Returns all available [Translation](class_translation.md#class-translation) instances as added by [add_translation()](class_translationdomain.md#class-translationdomain-method-add-translation).

---


<a id="class-translationdomain-method-has-translation"></a>

[bool](class_bool.md#class-bool) **has_translation**(translation: [Translation](class_translation.md#class-translation)) const [🔗](class_translationdomain.md#class-translationdomain-method-has-translation)

Returns `true` if this translation domain contains the given `translation`.

---


<a id="class-translationdomain-method-has-translation-for-locale"></a>

[bool](class_bool.md#class-bool) **has_translation_for_locale**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool)) const [🔗](class_translationdomain.md#class-translationdomain-method-has-translation-for-locale)

Returns `true` if there are any [Translation](class_translation.md#class-translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---


<a id="class-translationdomain-method-pseudolocalize"></a>

[StringName](class_stringname.md#class-stringname) **pseudolocalize**(message: [StringName](class_stringname.md#class-stringname)) const [🔗](class_translationdomain.md#class-translationdomain-method-pseudolocalize)

Returns the pseudolocalized string based on the `message` passed in.

---


<a id="class-translationdomain-method-remove-translation"></a>

void **remove_translation**(translation: [Translation](class_translation.md#class-translation)) [🔗](class_translationdomain.md#class-translationdomain-method-remove-translation)

Removes the given translation.

---


<a id="class-translationdomain-method-set-locale-override"></a>

void **set_locale_override**(locale: [String](class_string.md#class-string)) [🔗](class_translationdomain.md#class-translationdomain-method-set-locale-override)

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise, `locale` will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

**Note:** Calling this method does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) signal manually.

---


<a id="class-translationdomain-method-translate"></a>

[StringName](class_stringname.md#class-stringname) **translate**(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translationdomain.md#class-translationdomain-method-translate)

Returns the current locale's translation for the given message and context.

---


<a id="class-translationdomain-method-translate-plural"></a>

[StringName](class_stringname.md#class-stringname) **translate_plural**(message: [StringName](class_stringname.md#class-stringname), message_plural: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translationdomain.md#class-translationdomain-method-translate-plural)

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.
