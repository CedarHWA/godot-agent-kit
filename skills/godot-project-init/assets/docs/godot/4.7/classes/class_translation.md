> Source: https://docs.godotengine.org/en/4.7/classes/class_translation.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="translation"></a>

<a id="class-translation"></a>

# Translation

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OptimizedTranslation](class_optimizedtranslation.md#class-optimizedtranslation)

A language translation that maps a collection of strings to their individual translations.

<a id="description"></a>

## Description

**Translation** maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

A **Translation** consists of messages. A message is identified by its context and untranslated string. Unlike [gettext](https://www.gnu.org/software/gettext/), using an empty context string in Godot means not using any context.

<a id="tutorials"></a>

## Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)
- [Localization using gettext](../tutorials/i18n/localization_using_gettext.md)
- [Locales](../tutorials/i18n/locales.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [locale](class_translation.md#class-translation-property-locale) | `"en"` |
| [String](class_string.md#class-string) | [plural_rules_override](class_translation.md#class-translation-property-plural-rules-override) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [StringName](class_stringname.md#class-stringname) | [_get_message](class_translation.md#class-translation-private-method-get-message)(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname)) virtual const |
| [StringName](class_stringname.md#class-stringname) | [_get_plural_message](class_translation.md#class-translation-private-method-get-plural-message)(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname)) virtual const |
| void | [add_message](class_translation.md#class-translation-method-add-message)(src_message: [StringName](class_stringname.md#class-stringname), xlated_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") |
| void | [add_plural_message](class_translation.md#class-translation-method-add-plural-message)(src_message: [StringName](class_stringname.md#class-stringname), xlated_messages: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), context: [StringName](class_stringname.md#class-stringname) = &"") |
| void | [erase_message](class_translation.md#class-translation-method-erase-message)(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") |
| [StringName](class_stringname.md#class-stringname) | [get_message](class_translation.md#class-translation-method-get-message)(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const |
| [int](class_int.md#class-int) | [get_message_count](class_translation.md#class-translation-method-get-message-count)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_message_list](class_translation.md#class-translation-method-get-message-list)() const |
| [StringName](class_stringname.md#class-stringname) | [get_plural_message](class_translation.md#class-translation-method-get-plural-message)(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_translated_message_list](class_translation.md#class-translation-method-get-translated-message-list)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-translation-property-locale"></a>

[String](class_string.md#class-string) **locale** = `"en"` [🔗](class_translation.md#class-translation-property-locale)

- void **set_locale**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_locale**()

The locale of the translation.

---


<a id="class-translation-property-plural-rules-override"></a>

[String](class_string.md#class-string) **plural_rules_override** = `""` [🔗](class_translation.md#class-translation-property-plural-rules-override)

- void **set_plural_rules_override**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_plural_rules_override**()

The plural rules string to enforce. See [GNU gettext](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html) for examples and more info.

If empty or invalid, default plural rules from [TranslationServer.get_plural_rules()](class_translationserver.md#class-translationserver-method-get-plural-rules) are used. The English plural rules are used as a fallback.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-translation-private-method-get-message"></a>

[StringName](class_stringname.md#class-stringname) **_get_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_translation.md#class-translation-private-method-get-message)

Virtual method to override [get_message()](class_translation.md#class-translation-method-get-message).

---


<a id="class-translation-private-method-get-plural-message"></a>

[StringName](class_stringname.md#class-stringname) **_get_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_translation.md#class-translation-private-method-get-plural-message)

Virtual method to override [get_plural_message()](class_translation.md#class-translation-method-get-plural-message).

---


<a id="class-translation-method-add-message"></a>

void **add_message**(src_message: [StringName](class_stringname.md#class-stringname), xlated_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_translation.md#class-translation-method-add-message)

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---


<a id="class-translation-method-add-plural-message"></a>

void **add_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), xlated_messages: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), context: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_translation.md#class-translation-method-add-plural-message)

Adds a message involving plural translation if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---


<a id="class-translation-method-erase-message"></a>

void **erase_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_translation.md#class-translation-method-erase-message)

Erases a message.

---


<a id="class-translation-method-get-message"></a>

[StringName](class_stringname.md#class-stringname) **get_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translation.md#class-translation-method-get-message)

Returns a message's translation.

---


<a id="class-translation-method-get-message-count"></a>

[int](class_int.md#class-int) **get_message_count**() const [🔗](class_translation.md#class-translation-method-get-message-count)

Returns the number of existing messages.

---


<a id="class-translation-method-get-message-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_message_list**() const [🔗](class_translation.md#class-translation-method-get-message-list)

Returns the keys of all messages, that is, the context and untranslated strings of each message.

**Note:** If a message does not use a context, the corresponding element is the untranslated string. Otherwise, the corresponding element is the context and untranslated string separated by the EOT character (`U+0004`). This is done for compatibility purposes.

```gdscript
for key in translation.get_message_list():
    var p = key.find("\u0004")
    if p == -1:
        var untranslated = key
        print("Message %s" % untranslated)
    else:
        var context = key.substr(0, p)
        var untranslated = key.substr(p + 1)
        print("Message %s with context %s" % [untranslated, context])
```

---


<a id="class-translation-method-get-plural-message"></a>

[StringName](class_stringname.md#class-stringname) **get_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_translation.md#class-translation-method-get-plural-message)

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

**Note:** Plurals are only supported in [gettext-based translations (PO)](../tutorials/i18n/localization_using_gettext.md), not CSV.

---


<a id="class-translation-method-get-translated-message-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_translated_message_list**() const [🔗](class_translation.md#class-translation-method-get-translated-message-list)

Returns all the translated strings.
