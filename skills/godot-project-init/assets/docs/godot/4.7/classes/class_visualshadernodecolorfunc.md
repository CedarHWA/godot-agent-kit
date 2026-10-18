> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecolorfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecolorfunc"></a>

<a id="class-visualshadernodecolorfunc"></a>

# VisualShaderNodeColorFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) function to be used within the visual shader graph.

<a id="description"></a>

## Description

Accept a [Color](class_color.md#class-color) to the input port and transform it according to [function](class_visualshadernodecolorfunc.md#class-visualshadernodecolorfunc-property-function).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) | [function](class_visualshadernodecolorfunc.md#class-visualshadernodecolorfunc-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodecolorfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function)

<a id="class-visualshadernodecolorfunc-constant-func-grayscale"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_GRAYSCALE** = `0`

Converts the color to grayscale using the following formula:

```gdscript
vec3 c = input;
float max1 = max(c.r, c.g);
float max2 = max(max1, c.b);
float max3 = max(max1, max2);
return vec3(max3, max3, max3);
```

<a id="class-visualshadernodecolorfunc-constant-func-hsv2rgb"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_HSV2RGB** = `1`

Converts HSV vector to RGB equivalent.

<a id="class-visualshadernodecolorfunc-constant-func-rgb2hsv"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_RGB2HSV** = `2`

Converts RGB vector to HSV equivalent.

<a id="class-visualshadernodecolorfunc-constant-func-sepia"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_SEPIA** = `3`

Applies sepia tone effect using the following formula:

```gdscript
vec3 c = input;
float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
return vec3(r, g, b);
```

<a id="class-visualshadernodecolorfunc-constant-func-linear-to-srgb"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_LINEAR_TO_SRGB** = `4`

Converts color from linear encoding to nonlinear sRGB encoding using the following formula:

```gdscript
const vec3 a = vec3(0.055f);
return mix((vec3(1.0f) + a) * pow(c.rgb, vec3(1.0f / 2.4f)) - a, 12.92f * c.rgb, lessThan(c.rgb, vec3(0.0031308f)));
```

The Compatibility renderer uses a simpler formula that may produce undefined behavior with negative input values:

```gdscript
vec3 c = input;
return max(vec3(1.055) * pow(c, vec3(0.416666667)) - vec3(0.055), vec3(0.0));
```

<a id="class-visualshadernodecolorfunc-constant-func-srgb-to-linear"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_SRGB_TO_LINEAR** = `5`

Converts color from nonlinear sRGB encoding to linear encoding using the following formula:

```gdscript
vec3 c = input;
return mix(pow((c.rgb + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), c.rgb * (1.0 / 12.92), lessThan(c.rgb, vec3(0.04045)));
```

The Compatibility renderer uses a simpler formula that behaves poorly with negative input values:

```gdscript
vec3 c = input;
return c * (c * (c * 0.305306011 + 0.682171111) + 0.012522878);
```

<a id="class-visualshadernodecolorfunc-constant-func-max"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **FUNC_MAX** = `6`

Represents the size of the [Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecolorfunc-property-function"></a>

[Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **function** = `0` [🔗](class_visualshadernodecolorfunc.md#class-visualshadernodecolorfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function))
- [Function](class_visualshadernodecolorfunc.md#enum-visualshadernodecolorfunc-function) **get_function**()

A function to be applied to the input color.
