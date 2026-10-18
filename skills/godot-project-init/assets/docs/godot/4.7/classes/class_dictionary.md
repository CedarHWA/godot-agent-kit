> Source: https://docs.godotengine.org/en/4.7/classes/class_dictionary.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="dictionary"></a>

<a id="class-dictionary"></a>

# Dictionary

A built-in data structure that holds key-value pairs.

<a id="description"></a>

## Description

Dictionaries are associative containers that contain values referenced by unique keys. Dictionaries will preserve the insertion order when adding new entries. In other programming languages, this data structure is often referred to as a hash map or an associative array.

You can define a dictionary by placing a comma-separated list of `key: value` pairs inside curly braces `{}`.

Creating a dictionary:

```gdscript
var my_dict = {} # Creates an empty dictionary.

var dict_variable_key = "Another key name"
var dict_variable_value = "value2"
var another_dict = {
    "Some key name": "value1",
    dict_variable_key: dict_variable_value,
}

var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }

# Alternative Lua-style syntax.
# Doesn't require quotes around keys, but only string constants can be used as key names.
# Additionally, key names must start with a letter or an underscore.
# Here, `some_key` is a string literal, not a variable!
another_dict = {
    some_key = 42,
}
```

```csharp
var myDict = new Godot.Collections.Dictionary(); // Creates an empty dictionary.
var pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};
```

You can access a dictionary's value by referencing its corresponding key. In the above example, `points_dict["White"]` will return `50`. You can also write `points_dict.White`, which is equivalent. However, you'll have to use the bracket syntax if the key you're accessing the dictionary with isn't a fixed string (such as a number or variable).

```gdscript
@export_enum("White", "Yellow", "Orange") var my_color: String
var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
func _ready():
    # We can't use dot syntax here as `my_color` is a variable.
    var points = points_dict[my_color]
```

```csharp
[Export(PropertyHint.Enum, "White,Yellow,Orange")]
public string MyColor { get; set; }
private Godot.Collections.Dictionary _pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};

public override void _Ready()
{
    int points = (int)_pointsDict[MyColor];
}
```

In the above code, `points` will be assigned the value that is paired with the appropriate color selected in `my_color`.

Dictionaries can contain more complex data:

```gdscript
var my_dict = {
    "First Array": [1, 2, 3, 4] # Assigns an Array to a String key.
}
```

```csharp
var myDict = new Godot.Collections.Dictionary
{
    { "First Array", new Godot.Collections.Array { 1, 2, 3, 4 } }
};
```

To add a key to an existing dictionary, access it like an existing key and assign to it:

```gdscript
var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
points_dict["Blue"] = 150 # Add "Blue" as a key and assign 150 as its value.
```

```csharp
var pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};
pointsDict["Blue"] = 150; // Add "Blue" as a key and assign 150 as its value.
```

Finally, untyped dictionaries can contain different types of keys and values in the same dictionary:

```gdscript
# This is a valid dictionary.
# To access the string "Nested value" below, use `my_dict.sub_dict.sub_key` or `my_dict["sub_dict"]["sub_key"]`.
# Indexing styles can be mixed and matched depending on your needs.
var my_dict = {
    "String Key": 5,
    4: [1, 2, 3],
    7: "Hello",
    "sub_dict": { "sub_key": "Nested value" },
}
```

```csharp
// This is a valid dictionary.
// To access the string "Nested value" below, use `((Godot.Collections.Dictionary)myDict["sub_dict"])["sub_key"]`.
var myDict = new Godot.Collections.Dictionary {
    { "String Key", 5 },
    { 4, new Godot.Collections.Array { 1, 2, 3 } },
    { 7, "Hello" },
    { "sub_dict", new Godot.Collections.Dictionary { { "sub_key", "Nested value" } } },
};
```

The keys of a dictionary can be iterated with the `for` keyword:

```gdscript
var groceries = { "Orange": 20, "Apple": 2, "Banana": 4 }
for fruit in groceries:
    var amount = groceries[fruit]
```

```csharp
var groceries = new Godot.Collections.Dictionary { { "Orange", 20 }, { "Apple", 2 }, { "Banana", 4 } };
foreach (var (fruit, amount) in groceries)
{
    // `fruit` is the key, `amount` is the value.
}
```

To enforce a certain type for keys and values, you can create a *typed dictionary*. Typed dictionaries can only contain keys and values of the given types, or that inherit from the given classes:

```gdscript
# Creates a typed dictionary with String keys and int values.
# Attempting to use any other type for keys or values will result in an error.
var typed_dict: Dictionary[String, int] = {
    "some_key": 1,
    "some_other_key": 2,
}

# Creates a typed dictionary with String keys and values of any type.
# Attempting to use any other type for keys will result in an error.
var typed_dict_key_only: Dictionary[String, Variant] = {
    "some_key": 12.34,
    "some_other_key": "string",
}
```

```csharp
// Creates a typed dictionary with String keys and int values.
// Attempting to use any other type for keys or values will result in an error.
var typedDict = new Godot.Collections.Dictionary<String, int> {
    {"some_key", 1},
    {"some_other_key", 2},
};

// Creates a typed dictionary with String keys and values of any type.
// Attempting to use any other type for keys will result in an error.
var typedDictKeyOnly = new Godot.Collections.Dictionary<String, Variant> {
    {"some_key", 12.34},
    {"some_other_key", "string"},
};
```

**Note:** Dictionaries are always passed by reference. To get a copy of a dictionary which can be modified independently of the original dictionary, use [duplicate()](class_dictionary.md#class-dictionary-method-duplicate).

**Note:** Erasing elements while iterating over dictionaries is **not** supported and will result in unpredictable behavior.

**Note:** In a boolean context, a dictionary will evaluate to `false` if it's empty (`{}`). Otherwise, a dictionary will always evaluate to `true`.

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="tutorials"></a>

## Tutorials

- [GDScript basics: Dictionary](../tutorials/scripting/gdscript/gdscript_basics.md#dictionary)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)
- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [Dictionary](class_dictionary.md#class-dictionary) | [Dictionary](class_dictionary.md#class-dictionary-constructor-dictionary)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [Dictionary](class_dictionary.md#class-dictionary-constructor-dictionary)(base: [Dictionary](class_dictionary.md#class-dictionary), key_type: [int](class_int.md#class-int), key_class_name: [StringName](class_stringname.md#class-stringname), key_script: [Variant](class_variant.md#class-variant), value_type: [int](class_int.md#class-int), value_class_name: [StringName](class_stringname.md#class-stringname), value_script: [Variant](class_variant.md#class-variant)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [Dictionary](class_dictionary.md#class-dictionary-constructor-dictionary)(from: [Dictionary](class_dictionary.md#class-dictionary)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [assign](class_dictionary.md#class-dictionary-method-assign)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [clear](class_dictionary.md#class-dictionary-method-clear)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [duplicate](class_dictionary.md#class-dictionary-method-duplicate)(deep: [bool](class_bool.md#class-bool) = false) const |
| [Dictionary](class_dictionary.md#class-dictionary) | [duplicate_deep](class_dictionary.md#class-dictionary-method-duplicate-deep)(deep_subresources_mode: [int](class_int.md#class-int) = 1) const |
| [bool](class_bool.md#class-bool) | [erase](class_dictionary.md#class-dictionary-method-erase)(key: [Variant](class_variant.md#class-variant)) |
| [Variant](class_variant.md#class-variant) | [find_key](class_dictionary.md#class-dictionary-method-find-key)(value: [Variant](class_variant.md#class-variant)) const |
| [Variant](class_variant.md#class-variant) | [get](class_dictionary.md#class-dictionary-method-get)(key: [Variant](class_variant.md#class-variant), default: [Variant](class_variant.md#class-variant) = null) const |
| [Variant](class_variant.md#class-variant) | [get_or_add](class_dictionary.md#class-dictionary-method-get-or-add)(key: [Variant](class_variant.md#class-variant), default: [Variant](class_variant.md#class-variant) = null) |
| [int](class_int.md#class-int) | [get_typed_key_builtin](class_dictionary.md#class-dictionary-method-get-typed-key-builtin)() const |
| [StringName](class_stringname.md#class-stringname) | [get_typed_key_class_name](class_dictionary.md#class-dictionary-method-get-typed-key-class-name)() const |
| [Variant](class_variant.md#class-variant) | [get_typed_key_script](class_dictionary.md#class-dictionary-method-get-typed-key-script)() const |
| [int](class_int.md#class-int) | [get_typed_value_builtin](class_dictionary.md#class-dictionary-method-get-typed-value-builtin)() const |
| [StringName](class_stringname.md#class-stringname) | [get_typed_value_class_name](class_dictionary.md#class-dictionary-method-get-typed-value-class-name)() const |
| [Variant](class_variant.md#class-variant) | [get_typed_value_script](class_dictionary.md#class-dictionary-method-get-typed-value-script)() const |
| [bool](class_bool.md#class-bool) | [has](class_dictionary.md#class-dictionary-method-has)(key: [Variant](class_variant.md#class-variant)) const |
| [bool](class_bool.md#class-bool) | [has_all](class_dictionary.md#class-dictionary-method-has-all)(keys: [Array](class_array.md#class-array)) const |
| [int](class_int.md#class-int) | [hash](class_dictionary.md#class-dictionary-method-hash)() const |
| [bool](class_bool.md#class-bool) | [is_empty](class_dictionary.md#class-dictionary-method-is-empty)() const |
| [bool](class_bool.md#class-bool) | [is_read_only](class_dictionary.md#class-dictionary-method-is-read-only)() const |
| [bool](class_bool.md#class-bool) | [is_same_typed](class_dictionary.md#class-dictionary-method-is-same-typed)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const |
| [bool](class_bool.md#class-bool) | [is_same_typed_key](class_dictionary.md#class-dictionary-method-is-same-typed-key)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const |
| [bool](class_bool.md#class-bool) | [is_same_typed_value](class_dictionary.md#class-dictionary-method-is-same-typed-value)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const |
| [bool](class_bool.md#class-bool) | [is_typed](class_dictionary.md#class-dictionary-method-is-typed)() const |
| [bool](class_bool.md#class-bool) | [is_typed_key](class_dictionary.md#class-dictionary-method-is-typed-key)() const |
| [bool](class_bool.md#class-bool) | [is_typed_value](class_dictionary.md#class-dictionary-method-is-typed-value)() const |
| [Array](class_array.md#class-array) | [keys](class_dictionary.md#class-dictionary-method-keys)() const |
| void | [make_read_only](class_dictionary.md#class-dictionary-method-make-read-only)() |
| void | [merge](class_dictionary.md#class-dictionary-method-merge)(dictionary: [Dictionary](class_dictionary.md#class-dictionary), overwrite: [bool](class_bool.md#class-bool) = false) |
| [Dictionary](class_dictionary.md#class-dictionary) | [merged](class_dictionary.md#class-dictionary-method-merged)(dictionary: [Dictionary](class_dictionary.md#class-dictionary), overwrite: [bool](class_bool.md#class-bool) = false) const |
| [bool](class_bool.md#class-bool) | [recursive_equal](class_dictionary.md#class-dictionary-method-recursive-equal)(dictionary: [Dictionary](class_dictionary.md#class-dictionary), recursion_count: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [set](class_dictionary.md#class-dictionary-method-set)(key: [Variant](class_variant.md#class-variant), value: [Variant](class_variant.md#class-variant)) |
| [int](class_int.md#class-int) | [size](class_dictionary.md#class-dictionary-method-size)() const |
| void | [sort](class_dictionary.md#class-dictionary-method-sort)() |
| [Array](class_array.md#class-array) | [values](class_dictionary.md#class-dictionary-method-values)() const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_dictionary.md#class-dictionary-operator-neq-dictionary)(right: [Dictionary](class_dictionary.md#class-dictionary)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_dictionary.md#class-dictionary-operator-eq-dictionary)(right: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Variant](class_variant.md#class-variant) | [operator []](class_dictionary.md#class-dictionary-operator-idx-variant)(key: [Variant](class_variant.md#class-variant)) |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-dictionary-constructor-dictionary"></a>

[Dictionary](class_dictionary.md#class-dictionary) **Dictionary**() [🔗](class_dictionary.md#class-dictionary-constructor-dictionary)

Constructs an empty **Dictionary**.

---

[Dictionary](class_dictionary.md#class-dictionary) **Dictionary**(base: [Dictionary](class_dictionary.md#class-dictionary), key_type: [int](class_int.md#class-int), key_class_name: [StringName](class_stringname.md#class-stringname), key_script: [Variant](class_variant.md#class-variant), value_type: [int](class_int.md#class-int), value_class_name: [StringName](class_stringname.md#class-stringname), value_script: [Variant](class_variant.md#class-variant))

Creates a typed dictionary from the `base` dictionary. A typed dictionary can only contain keys and values of the given types, or that inherit from the given classes, as described by this constructor's parameters.

---

[Dictionary](class_dictionary.md#class-dictionary) **Dictionary**(from: [Dictionary](class_dictionary.md#class-dictionary))

Returns the same dictionary as `from`. If you need a copy of the dictionary, use [duplicate()](class_dictionary.md#class-dictionary-method-duplicate).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-dictionary-method-assign"></a>

void **assign**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_dictionary.md#class-dictionary-method-assign)

Assigns elements of another `dictionary` into the dictionary. Resizes the dictionary to match `dictionary`. Performs type conversions if the dictionary is typed.

---


<a id="class-dictionary-method-clear"></a>

void **clear**() [🔗](class_dictionary.md#class-dictionary-method-clear)

Clears the dictionary, removing all entries from it.

---


<a id="class-dictionary-method-duplicate"></a>

[Dictionary](class_dictionary.md#class-dictionary) **duplicate**(deep: [bool](class_bool.md#class-bool) = false) const [🔗](class_dictionary.md#class-dictionary-method-duplicate)

Returns a new copy of the dictionary.

By default, a **shallow** copy is returned: all nested [Array](class_array.md#class-array), **Dictionary**, and [Resource](class_resource.md#class-resource) keys and values are shared with the original dictionary. Modifying any of those in one dictionary will also affect them in the other.

If `deep` is `true`, a **deep** copy is returned: all nested arrays and dictionaries are also duplicated (recursively). Any [Resource](class_resource.md#class-resource) is still shared with the original dictionary, though.

---


<a id="class-dictionary-method-duplicate-deep"></a>

[Dictionary](class_dictionary.md#class-dictionary) **duplicate_deep**(deep_subresources_mode: [int](class_int.md#class-int) = 1) const [🔗](class_dictionary.md#class-dictionary-method-duplicate-deep)

Duplicates this dictionary, deeply, like [duplicate()](class_dictionary.md#class-dictionary-method-duplicate) when passing `true`, with extra control over how subresources are handled.

`deep_subresources_mode` must be one of the values from [DeepDuplicateMode](class_resource.md#enum-resource-deepduplicatemode). By default, only internal resources will be duplicated (recursively).

---


<a id="class-dictionary-method-erase"></a>

[bool](class_bool.md#class-bool) **erase**(key: [Variant](class_variant.md#class-variant)) [🔗](class_dictionary.md#class-dictionary-method-erase)

Removes the dictionary entry by key, if it exists. Returns `true` if the given `key` existed in the dictionary, otherwise `false`.

**Note:** Do not erase entries while iterating over the dictionary. You can iterate over the [keys()](class_dictionary.md#class-dictionary-method-keys) array instead.

---


<a id="class-dictionary-method-find-key"></a>

[Variant](class_variant.md#class-variant) **find_key**(value: [Variant](class_variant.md#class-variant)) const [🔗](class_dictionary.md#class-dictionary-method-find-key)

Finds and returns the first key whose associated value is equal to `value`, or `null` if it is not found.

**Note:** `null` is also a valid key. If inside the dictionary, [find_key()](class_dictionary.md#class-dictionary-method-find-key) may give misleading results.

---


<a id="class-dictionary-method-get"></a>

[Variant](class_variant.md#class-variant) **get**(key: [Variant](class_variant.md#class-variant), default: [Variant](class_variant.md#class-variant) = null) const [🔗](class_dictionary.md#class-dictionary-method-get)

Returns the corresponding value for the given `key` in the dictionary. If the `key` does not exist, returns `default`, or `null` if the parameter is omitted.

**Note:** If the `default` argument is computationally expensive or has unwanted side effects, consider using the [has()](class_dictionary.md#class-dictionary-method-has) method instead:

```gdscript
# Always calls `expensive_function()`.
dict.get("key", expensive_function())
# Calls `expensive_function()` only if the key does not exist.
dict.get("key") if dict.has("key") else expensive_function()
```

---


<a id="class-dictionary-method-get-or-add"></a>

[Variant](class_variant.md#class-variant) **get_or_add**(key: [Variant](class_variant.md#class-variant), default: [Variant](class_variant.md#class-variant) = null) [🔗](class_dictionary.md#class-dictionary-method-get-or-add)

Gets a value and ensures the key is set. If the `key` exists in the dictionary, this behaves like [get()](class_dictionary.md#class-dictionary-method-get). Otherwise, the `default` value is inserted into the dictionary and returned.

---


<a id="class-dictionary-method-get-typed-key-builtin"></a>

[int](class_int.md#class-int) **get_typed_key_builtin**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-key-builtin)

Returns the built-in [Variant](class_variant.md#class-variant) type of the typed dictionary's keys as a [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) constant. If the keys are not typed, returns [@GlobalScope.TYPE_NIL](class_@globalscope.md#class-globalscope-constant-type-nil). See also [is_typed_key()](class_dictionary.md#class-dictionary-method-is-typed-key).

---


<a id="class-dictionary-method-get-typed-key-class-name"></a>

[StringName](class_stringname.md#class-stringname) **get_typed_key_class_name**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-key-class-name)

Returns the **built-in** class name of the typed dictionary's keys, if the built-in [Variant](class_variant.md#class-variant) type is [@GlobalScope.TYPE_OBJECT](class_@globalscope.md#class-globalscope-constant-type-object). Otherwise, returns an empty [StringName](class_stringname.md#class-stringname). See also [is_typed_key()](class_dictionary.md#class-dictionary-method-is-typed-key) and [Object.get_class()](class_object.md#class-object-method-get-class).

---


<a id="class-dictionary-method-get-typed-key-script"></a>

[Variant](class_variant.md#class-variant) **get_typed_key_script**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-key-script)

Returns the [Script](class_script.md#class-script) instance associated with this typed dictionary's keys, or `null` if it does not exist. See also [is_typed_key()](class_dictionary.md#class-dictionary-method-is-typed-key).

---


<a id="class-dictionary-method-get-typed-value-builtin"></a>

[int](class_int.md#class-int) **get_typed_value_builtin**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-value-builtin)

Returns the built-in [Variant](class_variant.md#class-variant) type of the typed dictionary's values as a [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) constant. If the values are not typed, returns [@GlobalScope.TYPE_NIL](class_@globalscope.md#class-globalscope-constant-type-nil). See also [is_typed_value()](class_dictionary.md#class-dictionary-method-is-typed-value).

---


<a id="class-dictionary-method-get-typed-value-class-name"></a>

[StringName](class_stringname.md#class-stringname) **get_typed_value_class_name**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-value-class-name)

Returns the **built-in** class name of the typed dictionary's values, if the built-in [Variant](class_variant.md#class-variant) type is [@GlobalScope.TYPE_OBJECT](class_@globalscope.md#class-globalscope-constant-type-object). Otherwise, returns an empty [StringName](class_stringname.md#class-stringname). See also [is_typed_value()](class_dictionary.md#class-dictionary-method-is-typed-value) and [Object.get_class()](class_object.md#class-object-method-get-class).

---


<a id="class-dictionary-method-get-typed-value-script"></a>

[Variant](class_variant.md#class-variant) **get_typed_value_script**() const [🔗](class_dictionary.md#class-dictionary-method-get-typed-value-script)

Returns the [Script](class_script.md#class-script) instance associated with this typed dictionary's values, or `null` if it does not exist. See also [is_typed_value()](class_dictionary.md#class-dictionary-method-is-typed-value).

---


<a id="class-dictionary-method-has"></a>

[bool](class_bool.md#class-bool) **has**(key: [Variant](class_variant.md#class-variant)) const [🔗](class_dictionary.md#class-dictionary-method-has)

Returns `true` if the dictionary contains an entry with the given `key`.

```gdscript
var my_dict = {
    "Godot" : 4,
    210 : null,
}

print(my_dict.has("Godot")) # Prints true
print(my_dict.has(210))     # Prints true
print(my_dict.has(4))       # Prints false
```

```csharp
var myDict = new Godot.Collections.Dictionary
{
    { "Godot", 4 },
    { 210, default },
};

GD.Print(myDict.ContainsKey("Godot")); // Prints True
GD.Print(myDict.ContainsKey(210));     // Prints True
GD.Print(myDict.ContainsKey(4));       // Prints False
```

In GDScript, this is equivalent to the `in` operator:

```gdscript
if "Godot" in { "Godot": 4 }:
    print("The key is here!") # Will be printed.
```

**Note:** This method returns `true` as long as the `key` exists, even if its corresponding value is `null`.

---


<a id="class-dictionary-method-has-all"></a>

[bool](class_bool.md#class-bool) **has_all**(keys: [Array](class_array.md#class-array)) const [🔗](class_dictionary.md#class-dictionary-method-has-all)

Returns `true` if the dictionary contains all keys in the given `keys` array.

```gdscript
var data = { "width": 10, "height": 20 }
data.has_all(["height", "width"]) # Returns true
```

---


<a id="class-dictionary-method-hash"></a>

[int](class_int.md#class-int) **hash**() const [🔗](class_dictionary.md#class-dictionary-method-hash)

Returns a hashed 32-bit integer value representing the dictionary contents.

```gdscript
var dict1 = { "A": 10, "B": 2 }
var dict2 = { "A": 10, "B": 2 }

print(dict1.hash() == dict2.hash()) # Prints true
```

```csharp
var dict1 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };
var dict2 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };

// Godot.Collections.Dictionary has no Hash() method. Use GD.Hash() instead.
GD.Print(GD.Hash(dict1) == GD.Hash(dict2)); // Prints True
```

**Note:** Dictionaries with the same entries but in a different order will not have the same hash.

**Note:** Dictionaries with equal hash values are *not* guaranteed to be the same, because of hash collisions. On the contrary, dictionaries with different hash values are guaranteed to be different.

---


<a id="class-dictionary-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_dictionary.md#class-dictionary-method-is-empty)

Returns `true` if the dictionary is empty (its size is `0`). See also [size()](class_dictionary.md#class-dictionary-method-size).

---


<a id="class-dictionary-method-is-read-only"></a>

[bool](class_bool.md#class-bool) **is_read_only**() const [🔗](class_dictionary.md#class-dictionary-method-is-read-only)

Returns `true` if the dictionary is read-only. See [make_read_only()](class_dictionary.md#class-dictionary-method-make-read-only). Dictionaries are automatically read-only if declared with `const` keyword.

---


<a id="class-dictionary-method-is-same-typed"></a>

[bool](class_bool.md#class-bool) **is_same_typed**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const [🔗](class_dictionary.md#class-dictionary-method-is-same-typed)

Returns `true` if the dictionary is typed the same as `dictionary`.

---


<a id="class-dictionary-method-is-same-typed-key"></a>

[bool](class_bool.md#class-bool) **is_same_typed_key**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const [🔗](class_dictionary.md#class-dictionary-method-is-same-typed-key)

Returns `true` if the dictionary's keys are typed the same as `dictionary`'s keys.

---


<a id="class-dictionary-method-is-same-typed-value"></a>

[bool](class_bool.md#class-bool) **is_same_typed_value**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) const [🔗](class_dictionary.md#class-dictionary-method-is-same-typed-value)

Returns `true` if the dictionary's values are typed the same as `dictionary`'s values.

---


<a id="class-dictionary-method-is-typed"></a>

[bool](class_bool.md#class-bool) **is_typed**() const [🔗](class_dictionary.md#class-dictionary-method-is-typed)

Returns `true` if the dictionary is typed. Typed dictionaries can only store keys/values of their associated type and provide type safety for the `[]` operator. Methods of typed dictionary still return [Variant](class_variant.md#class-variant).

---


<a id="class-dictionary-method-is-typed-key"></a>

[bool](class_bool.md#class-bool) **is_typed_key**() const [🔗](class_dictionary.md#class-dictionary-method-is-typed-key)

Returns `true` if the dictionary's keys are typed.

---


<a id="class-dictionary-method-is-typed-value"></a>

[bool](class_bool.md#class-bool) **is_typed_value**() const [🔗](class_dictionary.md#class-dictionary-method-is-typed-value)

Returns `true` if the dictionary's values are typed.

---


<a id="class-dictionary-method-keys"></a>

[Array](class_array.md#class-array) **keys**() const [🔗](class_dictionary.md#class-dictionary-method-keys)

Returns the list of keys in the dictionary.

---


<a id="class-dictionary-method-make-read-only"></a>

void **make_read_only**() [🔗](class_dictionary.md#class-dictionary-method-make-read-only)

Makes the dictionary read-only, i.e. disables modification of the dictionary's contents. Does not apply to nested content, e.g. content of nested dictionaries.

---


<a id="class-dictionary-method-merge"></a>

void **merge**(dictionary: [Dictionary](class_dictionary.md#class-dictionary), overwrite: [bool](class_bool.md#class-bool) = false) [🔗](class_dictionary.md#class-dictionary-method-merge)

Adds entries from `dictionary` to this dictionary. By default, duplicate keys are not copied over, unless `overwrite` is `true`.

```gdscript
var dict = { "item": "sword", "quantity": 2 }
var other_dict = { "quantity": 15, "color": "silver" }

# Overwriting of existing keys is disabled by default.
dict.merge(other_dict)
print(dict)  # { "item": "sword", "quantity": 2, "color": "silver" }

# With overwriting of existing keys enabled.
dict.merge(other_dict, true)
print(dict)  # { "item": "sword", "quantity": 15, "color": "silver" }
```

```csharp
var dict = new Godot.Collections.Dictionary
{
    ["item"] = "sword",
    ["quantity"] = 2,
};

var otherDict = new Godot.Collections.Dictionary
{
    ["quantity"] = 15,
    ["color"] = "silver",
};

// Overwriting of existing keys is disabled by default.
dict.Merge(otherDict);
GD.Print(dict); // { "item": "sword", "quantity": 2, "color": "silver" }

// With overwriting of existing keys enabled.
dict.Merge(otherDict, true);
GD.Print(dict); // { "item": "sword", "quantity": 15, "color": "silver" }
```

**Note:** [merge()](class_dictionary.md#class-dictionary-method-merge) is *not* recursive. Nested dictionaries are considered as keys that can be overwritten or not depending on the value of `overwrite`, but they will never be merged together.

---


<a id="class-dictionary-method-merged"></a>

[Dictionary](class_dictionary.md#class-dictionary) **merged**(dictionary: [Dictionary](class_dictionary.md#class-dictionary), overwrite: [bool](class_bool.md#class-bool) = false) const [🔗](class_dictionary.md#class-dictionary-method-merged)

Returns a copy of this dictionary merged with the other `dictionary`. By default, duplicate keys are not copied over, unless `overwrite` is `true`. See also [merge()](class_dictionary.md#class-dictionary-method-merge).

This method is useful for quickly making dictionaries with default values:

```gdscript
var base = { "fruit": "apple", "vegetable": "potato" }
var extra = { "fruit": "orange", "dressing": "vinegar" }
# Prints { "fruit": "orange", "vegetable": "potato", "dressing": "vinegar" }
print(extra.merged(base))
# Prints { "fruit": "apple", "vegetable": "potato", "dressing": "vinegar" }
print(extra.merged(base, true))
```

---


<a id="class-dictionary-method-recursive-equal"></a>

[bool](class_bool.md#class-bool) **recursive_equal**(dictionary: [Dictionary](class_dictionary.md#class-dictionary), recursion_count: [int](class_int.md#class-int)) const [🔗](class_dictionary.md#class-dictionary-method-recursive-equal)

Returns `true` if the two dictionaries contain the same keys and values, inner **Dictionary** and [Array](class_array.md#class-array) keys and values are compared recursively.

---


<a id="class-dictionary-method-set"></a>

[bool](class_bool.md#class-bool) **set**(key: [Variant](class_variant.md#class-variant), value: [Variant](class_variant.md#class-variant)) [🔗](class_dictionary.md#class-dictionary-method-set)

Sets the value of the element at the given `key` to the given `value`. Returns `true` if the value is set successfully. Fails and returns `false` if the dictionary is read-only, or if `key` and `value` don't match the dictionary's types. This is the same as using the `[]` operator (`dict[key] = value`).

---


<a id="class-dictionary-method-size"></a>

[int](class_int.md#class-int) **size**() const [🔗](class_dictionary.md#class-dictionary-method-size)

Returns the number of entries in the dictionary. Empty dictionaries (`{ }`) always return `0`. See also [is_empty()](class_dictionary.md#class-dictionary-method-is-empty).

---


<a id="class-dictionary-method-sort"></a>

void **sort**() [🔗](class_dictionary.md#class-dictionary-method-sort)

Sorts the dictionary in ascending order, by key. The final order is dependent on the "less than" (`<`) comparison between keys.

```gdscript
var numbers = { "c": 2, "a": 0, "b": 1 }
numbers.sort()
print(numbers) # Prints { "a": 0, "b": 1, "c": 2 }
```

This method ensures that the dictionary's entries are ordered consistently when [keys()](class_dictionary.md#class-dictionary-method-keys) or [values()](class_dictionary.md#class-dictionary-method-values) are called, or when the dictionary needs to be converted to a string through [@GlobalScope.str()](class_@globalscope.md#class-globalscope-method-str) or [JSON.stringify()](class_json.md#class-json-method-stringify).

---


<a id="class-dictionary-method-values"></a>

[Array](class_array.md#class-array) **values**() const [🔗](class_dictionary.md#class-dictionary-method-values)

Returns the list of values in this dictionary.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-dictionary-operator-neq-dictionary"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_dictionary.md#class-dictionary-operator-neq-dictionary)

Returns `true` if the two dictionaries do not contain the same keys and values.

---


<a id="class-dictionary-operator-eq-dictionary"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_dictionary.md#class-dictionary-operator-eq-dictionary)

Returns `true` if the two dictionaries contain the same keys and values. The order of the entries does not matter.

**Note:** In C#, by convention, this operator compares by **reference**. If you need to compare by value, iterate over both dictionaries.

---


<a id="class-dictionary-operator-idx-variant"></a>

[Variant](class_variant.md#class-variant) **operator []**(key: [Variant](class_variant.md#class-variant)) [🔗](class_dictionary.md#class-dictionary-operator-idx-variant)

Returns the corresponding value for the given `key` in the dictionary. If the entry does not exist, fails and returns `null`. For safe access, use [get()](class_dictionary.md#class-dictionary-method-get) or [has()](class_dictionary.md#class-dictionary-method-has).
