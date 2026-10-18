> Source: https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="randomnumbergenerator"></a>

<a id="class-randomnumbergenerator"></a>

# RandomNumberGenerator

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides methods for generating pseudo-random numbers.

<a id="description"></a>

## Description

RandomNumberGenerator is a class for generating pseudo-random numbers. It currently uses [PCG32](https://www.pcg-random.org/).

**Note:** The underlying algorithm is an implementation detail and should not be depended upon.

To generate a random float number (within a given range) based on a time-dependent seed:

```gdscript
var rng = RandomNumberGenerator.new()
func _ready():
    var my_random_number = rng.randf_range(-10.0, 10.0)
```

<a id="tutorials"></a>

## Tutorials

- [Random number generation](../tutorials/math/random_number_generation.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [seed](class_randomnumbergenerator.md#class-randomnumbergenerator-property-seed) | `0` |
| [int](class_int.md#class-int) | [state](class_randomnumbergenerator.md#class-randomnumbergenerator-property-state) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [rand_weighted](class_randomnumbergenerator.md#class-randomnumbergenerator-method-rand-weighted)(weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |
| [float](class_float.md#class-float) | [randf](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randf)() |
| [float](class_float.md#class-float) | [randf_range](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randf-range)(from: [float](class_float.md#class-float), to: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [randfn](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randfn)(mean: [float](class_float.md#class-float) = 0.0, deviation: [float](class_float.md#class-float) = 1.0) |
| [int](class_int.md#class-int) | [randi](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randi)() |
| [int](class_int.md#class-int) | [randi_range](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randi-range)(from: [int](class_int.md#class-int), to: [int](class_int.md#class-int)) |
| void | [randomize](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randomize)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-randomnumbergenerator-property-seed"></a>

[int](class_int.md#class-int) **seed** = `0` [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-property-seed)

- void **set_seed**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_seed**()

Initializes the random number generator state based on the given seed value. A given seed will give a reproducible sequence of pseudo-random numbers.

**Note:** The RNG does not have an avalanche effect, and can output similar random streams given similar seeds. Consider using a hash function to improve your seed quality if they're sourced externally.

**Note:** The default value of this property is pseudo-random, and changes when calling [randomize()](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randomize). The `0` value documented here is a placeholder, and not the actual default seed.

**Note:** Setting this property produces a side effect of changing the internal [state](class_randomnumbergenerator.md#class-randomnumbergenerator-property-state), so make sure to initialize the seed *before* modifying the [state](class_randomnumbergenerator.md#class-randomnumbergenerator-property-state):

```gdscript
var rng = RandomNumberGenerator.new()
rng.seed = hash("Godot")
rng.state = 100 # Restore to some previously saved state.
```

---


<a id="class-randomnumbergenerator-property-state"></a>

[int](class_int.md#class-int) **state** = `0` [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-property-state)

- void **set_state**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_state**()

The current state of the random number generator. Save and restore this property to restore the generator to a previous state:

```gdscript
var rng = RandomNumberGenerator.new()
print(rng.randf())
var saved_state = rng.state # Store current state.
print(rng.randf()) # Advance internal state.
rng.state = saved_state # Restore the state.
print(rng.randf()) # Prints the same value as previously.
```

**Note:** Do not set state to arbitrary values, since the random number generator requires the state to have certain qualities to behave properly. It should only be set to values that came from the state property itself. To initialize the random number generator with arbitrary input, use [seed](class_randomnumbergenerator.md#class-randomnumbergenerator-property-seed) instead.

**Note:** The default value of this property is pseudo-random, and changes when calling [randomize()](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randomize). The `0` value documented here is a placeholder, and not the actual default state.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-randomnumbergenerator-method-rand-weighted"></a>

[int](class_int.md#class-int) **rand_weighted**(weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-rand-weighted)

Returns a random integer between `0` and the size of the array that is passed as a parameter. Each value in the array should be a floating-point number that represents the relative likelihood that it will be returned as an index. A higher value means the value is more likely to be returned as an index, while a value of `0` means it will never be returned as an index.

For example, if `[0.5, 1, 1, 2]` is passed as a parameter, then the method is twice as likely to return `3` (the index of the value `2`) and twice as unlikely to return `0` (the index of the value `0.5`) compared to the indices `1` and `2`.

Prints an error and returns `-1` if the array is empty.

```gdscript
var rng = RandomNumberGenerator.new()

var my_array = ["one", "two", "three", "four"]
var weights = PackedFloat32Array([0.5, 1, 1, 2])

# Prints one of the four elements in `my_array`.
# It is more likely to print "four", and less likely to print "one".
print(my_array[rng.rand_weighted(weights)])
```

---


<a id="class-randomnumbergenerator-method-randf"></a>

[float](class_float.md#class-float) **randf**() [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randf)

Returns a pseudo-random float between `0.0` and `1.0` (inclusive).

---


<a id="class-randomnumbergenerator-method-randf-range"></a>

[float](class_float.md#class-float) **randf_range**(from: [float](class_float.md#class-float), to: [float](class_float.md#class-float)) [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randf-range)

Returns a pseudo-random float between `from` and `to` (inclusive).

---


<a id="class-randomnumbergenerator-method-randfn"></a>

[float](class_float.md#class-float) **randfn**(mean: [float](class_float.md#class-float) = 0.0, deviation: [float](class_float.md#class-float) = 1.0) [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randfn)

Returns a [normally-distributed](https://en.wikipedia.org/wiki/Normal_distribution), pseudo-random floating-point number from the specified `mean` and a standard `deviation`. This is also known as a Gaussian distribution.

**Note:** This method uses the [Box-Muller transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform) algorithm.

---


<a id="class-randomnumbergenerator-method-randi"></a>

[int](class_int.md#class-int) **randi**() [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randi)

Returns a pseudo-random 32-bit unsigned integer between `0` and `4294967295` (inclusive).

---


<a id="class-randomnumbergenerator-method-randi-range"></a>

[int](class_int.md#class-int) **randi_range**(from: [int](class_int.md#class-int), to: [int](class_int.md#class-int)) [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randi-range)

Returns a pseudo-random 32-bit signed integer between `from` and `to` (inclusive).

---


<a id="class-randomnumbergenerator-method-randomize"></a>

void **randomize**() [🔗](class_randomnumbergenerator.md#class-randomnumbergenerator-method-randomize)

Sets up a time-based seed for this **RandomNumberGenerator** instance. Unlike the [@GlobalScope](class_@globalscope.md#class-globalscope) random number generation functions, different **RandomNumberGenerator** instances can use different seeds.
