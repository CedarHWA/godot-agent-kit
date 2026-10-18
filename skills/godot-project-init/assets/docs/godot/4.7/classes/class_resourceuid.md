> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceuid.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceuid"></a>

<a id="class-resourceuid"></a>

# ResourceUID

**Inherits:** [Object](class_object.md#class-object)

A singleton that manages the unique identifiers of all resources within a project.

<a id="description"></a>

## Description

Resource UIDs (Unique IDentifiers) allow the engine to keep references between resources intact, even if files are renamed or moved. They can be accessed with `uid://`.

**ResourceUID** keeps track of all registered resource UIDs in a project, generates new UIDs, and converts between their string and integer representations.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_id](class_resourceuid.md#class-resourceuid-method-add-id)(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string)) |
| [int](class_int.md#class-int) | [create_id](class_resourceuid.md#class-resourceuid-method-create-id)() |
| [int](class_int.md#class-int) | [create_id_for_path](class_resourceuid.md#class-resourceuid-method-create-id-for-path)(path: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [ensure_path](class_resourceuid.md#class-resourceuid-method-ensure-path)(path_or_uid: [String](class_string.md#class-string)) static |
| [String](class_string.md#class-string) | [get_id_path](class_resourceuid.md#class-resourceuid-method-get-id-path)(id: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_id](class_resourceuid.md#class-resourceuid-method-has-id)(id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [id_to_text](class_resourceuid.md#class-resourceuid-method-id-to-text)(id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [path_to_uid](class_resourceuid.md#class-resourceuid-method-path-to-uid)(path: [String](class_string.md#class-string)) static |
| void | [remove_id](class_resourceuid.md#class-resourceuid-method-remove-id)(id: [int](class_int.md#class-int)) |
| void | [set_id](class_resourceuid.md#class-resourceuid-method-set-id)(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string)) |
| [int](class_int.md#class-int) | [text_to_id](class_resourceuid.md#class-resourceuid-method-text-to-id)(text_id: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [uid_to_path](class_resourceuid.md#class-resourceuid-method-uid-to-path)(uid: [String](class_string.md#class-string)) static |

---


<a id="constants"></a>

## Constants

<a id="class-resourceuid-constant-invalid-id"></a>

**INVALID_ID** = `-1` [🔗](class_resourceuid.md#class-resourceuid-constant-invalid-id)

The value to use for an invalid UID, for example if the resource could not be loaded.

Its text representation is `uid://<invalid>`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-resourceuid-method-add-id"></a>

void **add_id**(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string)) [🔗](class_resourceuid.md#class-resourceuid-method-add-id)

Adds a new UID value which is mapped to the given resource path.

Fails with an error if the UID already exists, so be sure to check [has_id()](class_resourceuid.md#class-resourceuid-method-has-id) beforehand, or use [set_id()](class_resourceuid.md#class-resourceuid-method-set-id) instead.

---


<a id="class-resourceuid-method-create-id"></a>

[int](class_int.md#class-int) **create_id**() [🔗](class_resourceuid.md#class-resourceuid-method-create-id)

Generates a random resource UID which is guaranteed to be unique within the list of currently loaded UIDs.

In order for this UID to be registered, you must call [add_id()](class_resourceuid.md#class-resourceuid-method-add-id) or [set_id()](class_resourceuid.md#class-resourceuid-method-set-id).

---


<a id="class-resourceuid-method-create-id-for-path"></a>

[int](class_int.md#class-int) **create_id_for_path**(path: [String](class_string.md#class-string)) [🔗](class_resourceuid.md#class-resourceuid-method-create-id-for-path)

Like [create_id()](class_resourceuid.md#class-resourceuid-method-create-id), but the UID is seeded with the provided `path` and project name. UIDs generated for that path will be always the same within the current project.

---


<a id="class-resourceuid-method-ensure-path"></a>

[String](class_string.md#class-string) **ensure_path**(path_or_uid: [String](class_string.md#class-string)) static [🔗](class_resourceuid.md#class-resourceuid-method-ensure-path)

Returns a path, converting `path_or_uid` if necessary. Fails and returns an empty string if an invalid UID is provided.

---


<a id="class-resourceuid-method-get-id-path"></a>

[String](class_string.md#class-string) **get_id_path**(id: [int](class_int.md#class-int)) const [🔗](class_resourceuid.md#class-resourceuid-method-get-id-path)

Returns the path that the given UID value refers to.

Fails with an error if the UID does not exist, so be sure to check [has_id()](class_resourceuid.md#class-resourceuid-method-has-id) beforehand.

---


<a id="class-resourceuid-method-has-id"></a>

[bool](class_bool.md#class-bool) **has_id**(id: [int](class_int.md#class-int)) const [🔗](class_resourceuid.md#class-resourceuid-method-has-id)

Returns whether the given UID value is known to the cache.

---


<a id="class-resourceuid-method-id-to-text"></a>

[String](class_string.md#class-string) **id_to_text**(id: [int](class_int.md#class-int)) const [🔗](class_resourceuid.md#class-resourceuid-method-id-to-text)

Converts the given UID to a `uid://` string value.

---


<a id="class-resourceuid-method-path-to-uid"></a>

[String](class_string.md#class-string) **path_to_uid**(path: [String](class_string.md#class-string)) static [🔗](class_resourceuid.md#class-resourceuid-method-path-to-uid)

Converts the provided resource `path` to a UID. Returns the unchanged path if it has no associated UID.

---


<a id="class-resourceuid-method-remove-id"></a>

void **remove_id**(id: [int](class_int.md#class-int)) [🔗](class_resourceuid.md#class-resourceuid-method-remove-id)

Removes a loaded UID value from the cache.

Fails with an error if the UID does not exist, so be sure to check [has_id()](class_resourceuid.md#class-resourceuid-method-has-id) beforehand.

---


<a id="class-resourceuid-method-set-id"></a>

void **set_id**(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string)) [🔗](class_resourceuid.md#class-resourceuid-method-set-id)

Updates the resource path of an existing UID.

Fails with an error if the UID does not exist, so be sure to check [has_id()](class_resourceuid.md#class-resourceuid-method-has-id) beforehand, or use [add_id()](class_resourceuid.md#class-resourceuid-method-add-id) instead.

---


<a id="class-resourceuid-method-text-to-id"></a>

[int](class_int.md#class-int) **text_to_id**(text_id: [String](class_string.md#class-string)) const [🔗](class_resourceuid.md#class-resourceuid-method-text-to-id)

Extracts the UID value from the given `uid://` string.

---


<a id="class-resourceuid-method-uid-to-path"></a>

[String](class_string.md#class-string) **uid_to_path**(uid: [String](class_string.md#class-string)) static [🔗](class_resourceuid.md#class-resourceuid-method-uid-to-path)

Converts the provided `uid` to a path. Prints an error if the UID is invalid.
