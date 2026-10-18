> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventscreendrag.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventscreendrag"></a>

<a id="class-inputeventscreendrag"></a>

# InputEventScreenDrag

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a screen drag event.

<a id="description"></a>

## Description

Stores information about screen drag events. See [Node._input()](class_node.md#class-node-private-method-input).

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [index](class_inputeventscreendrag.md#class-inputeventscreendrag-property-index) | `0` |
| [bool](class_bool.md#class-bool) | [pen_inverted](class_inputeventscreendrag.md#class-inputeventscreendrag-property-pen-inverted) | `false` |
| [Vector2](class_vector2.md#class-vector2) | [position](class_inputeventscreendrag.md#class-inputeventscreendrag-property-position) | `Vector2(0, 0)` |
| [float](class_float.md#class-float) | [pressure](class_inputeventscreendrag.md#class-inputeventscreendrag-property-pressure) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-relative) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [screen_relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-relative) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [screen_velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-velocity) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [tilt](class_inputeventscreendrag.md#class-inputeventscreendrag-property-tilt) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-velocity) | `Vector2(0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventscreendrag-property-index"></a>

[int](class_int.md#class-int) **index** = `0` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-index)

- void **set_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index**()

The drag event index in the case of a multi-drag event.

---


<a id="class-inputeventscreendrag-property-pen-inverted"></a>

[bool](class_bool.md#class-bool) **pen_inverted** = `false` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-pen-inverted)

- void **set_pen_inverted**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_pen_inverted**()

Returns `true` when using the eraser end of a stylus pen.

---


<a id="class-inputeventscreendrag-property-position"></a>

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-position)

- void **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The drag position in the viewport the node is in, using the coordinate system of this viewport.

---


<a id="class-inputeventscreendrag-property-pressure"></a>

[float](class_float.md#class-float) **pressure** = `0.0` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-pressure)

- void **set_pressure**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure**()

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.

---


<a id="class-inputeventscreendrag-property-relative"></a>

[Vector2](class_vector2.md#class-vector2) **relative** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-relative)

- void **set_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_relative**()

The drag position relative to the previous position (position at the last frame).

**Note:** [relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-relative) is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using [relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-relative) in a script that handles touch aiming. To avoid this, use [screen_relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-relative) instead.

---


<a id="class-inputeventscreendrag-property-screen-relative"></a>

[Vector2](class_vector2.md#class-vector2) **screen_relative** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-relative)

- void **set_screen_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_relative**()

The unscaled drag position relative to the previous position in screen coordinates (position at the last frame). This position is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by). This should be preferred over [relative](class_inputeventscreendrag.md#class-inputeventscreendrag-property-relative) for touch aiming regardless of the project's stretch mode.

---


<a id="class-inputeventscreendrag-property-screen-velocity"></a>

[Vector2](class_vector2.md#class-vector2) **screen_velocity** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-velocity)

- void **set_screen_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_velocity**()

The unscaled drag velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by). This should be preferred over [velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-velocity) for touch aiming regardless of the project's stretch mode.

---


<a id="class-inputeventscreendrag-property-tilt"></a>

[Vector2](class_vector2.md#class-vector2) **tilt** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-tilt)

- void **set_tilt**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_tilt**()

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

---


<a id="class-inputeventscreendrag-property-velocity"></a>

[Vector2](class_vector2.md#class-vector2) **velocity** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class-inputeventscreendrag-property-velocity)

- void **set_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_velocity**()

The drag velocity.

**Note:** [velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-velocity) is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using [velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-velocity) in a script that handles touch aiming. To avoid this, use [screen_velocity](class_inputeventscreendrag.md#class-inputeventscreendrag-property-screen-velocity) instead.
