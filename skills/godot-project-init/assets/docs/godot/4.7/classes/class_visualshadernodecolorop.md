> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecolorop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecolorop"></a>

<a id="class-visualshadernodecolorop"></a>

# VisualShaderNodeColorOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Applies [operator](class_visualshadernodecolorop.md#class-visualshadernodecolorop-property-operator) to two color inputs.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) | [operator](class_visualshadernodecolorop.md#class-visualshadernodecolorop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodecolorop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator)

<a id="class-visualshadernodecolorop-constant-op-screen"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_SCREEN** = `0`

Produce a screen effect with the following formula:

```gdscript
result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);
```

<a id="class-visualshadernodecolorop-constant-op-difference"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_DIFFERENCE** = `1`

Produce a difference effect with the following formula:

```gdscript
result = abs(a - b);
```

<a id="class-visualshadernodecolorop-constant-op-darken"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_DARKEN** = `2`

Produce a darken effect with the following formula:

```gdscript
result = min(a, b);
```

<a id="class-visualshadernodecolorop-constant-op-lighten"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_LIGHTEN** = `3`

Produce a lighten effect with the following formula:

```gdscript
result = max(a, b);
```

<a id="class-visualshadernodecolorop-constant-op-overlay"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_OVERLAY** = `4`

Produce an overlay effect with the following formula:

```gdscript
for (int i = 0; i < 3; i++) {
    float base = a[i];
    float blend = b[i];
    if (base < 0.5) {
        result[i] = 2.0 * base * blend;
    } else {
        result[i] = 1.0 - 2.0 * (1.0 - blend) * (1.0 - base);
    }
}
```

<a id="class-visualshadernodecolorop-constant-op-dodge"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_DODGE** = `5`

Produce a dodge effect with the following formula:

```gdscript
result = a / (vec3(1.0) - b);
```

<a id="class-visualshadernodecolorop-constant-op-burn"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_BURN** = `6`

Produce a burn effect with the following formula:

```gdscript
result = vec3(1.0) - (vec3(1.0) - a) / b;
```

<a id="class-visualshadernodecolorop-constant-op-soft-light"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_SOFT_LIGHT** = `7`

Produce a soft light effect with the following formula:

```gdscript
for (int i = 0; i < 3; i++) {
    float base = a[i];
    float blend = b[i];
    if (base < 0.5) {
        result[i] = base * (blend + 0.5);
    } else {
        result[i] = 1.0 - (1.0 - base) * (1.0 - (blend - 0.5));
    }
}
```

<a id="class-visualshadernodecolorop-constant-op-hard-light"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_HARD_LIGHT** = `8`

Produce a hard light effect with the following formula:

```gdscript
for (int i = 0; i < 3; i++) {
    float base = a[i];
    float blend = b[i];
    if (base < 0.5) {
        result[i] = base * (2.0 * blend);
    } else {
        result[i] = 1.0 - (1.0 - base) * (1.0 - 2.0 * (blend - 0.5));
    }
}
```

<a id="class-visualshadernodecolorop-constant-op-max"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **OP_MAX** = `9`

Represents the size of the [Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecolorop-property-operator"></a>

[Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **operator** = `0` [🔗](class_visualshadernodecolorop.md#class-visualshadernodecolorop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator))
- [Operator](class_visualshadernodecolorop.md#enum-visualshadernodecolorop-operator) **get_operator**()

An operator to be applied to the inputs.
