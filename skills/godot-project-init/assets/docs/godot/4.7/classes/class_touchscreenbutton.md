> Source: https://docs.godotengine.org/en/4.7/classes/class_touchscreenbutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="touchscreenbutton"></a>

<a id="class-touchscreenbutton"></a>

# TouchScreenButton

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Button for touch screen devices for gameplay use.

<a id="description"></a>

## Description

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike [Button](class_button.md#class-button), TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

This node inherits from [Node2D](class_node2d.md#class-node2d). Unlike with [Control](class_control.md#class-control) nodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to use [Button](class_button.md#class-button) nodes instead. To make button nodes react to touch events, you can enable [ProjectSettings.input_devices/pointing/emulate_mouse_from_touch](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-mouse-from-touch) in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [action](class_touchscreenbutton.md#class-touchscreenbutton-property-action) | `""` |
| [BitMap](class_bitmap.md#class-bitmap) | [bitmask](class_touchscreenbutton.md#class-touchscreenbutton-property-bitmask) |  |
| [bool](class_bool.md#class-bool) | [passby_press](class_touchscreenbutton.md#class-touchscreenbutton-property-passby-press) | `false` |
| [Shape2D](class_shape2d.md#class-shape2d) | [shape](class_touchscreenbutton.md#class-touchscreenbutton-property-shape) |  |
| [bool](class_bool.md#class-bool) | [shape_centered](class_touchscreenbutton.md#class-touchscreenbutton-property-shape-centered) | `true` |
| [bool](class_bool.md#class-bool) | [shape_visible](class_touchscreenbutton.md#class-touchscreenbutton-property-shape-visible) | `true` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_normal](class_touchscreenbutton.md#class-touchscreenbutton-property-texture-normal) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_pressed](class_touchscreenbutton.md#class-touchscreenbutton-property-texture-pressed) |  |
| [VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode) | [visibility_mode](class_touchscreenbutton.md#class-touchscreenbutton-property-visibility-mode) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_pressed](class_touchscreenbutton.md#class-touchscreenbutton-method-is-pressed)() const |

---


<a id="signals"></a>

## Signals

<a id="class-touchscreenbutton-signal-pressed"></a>

**pressed**() [🔗](class_touchscreenbutton.md#class-touchscreenbutton-signal-pressed)

Emitted when the button is pressed (down).

---


<a id="class-touchscreenbutton-signal-released"></a>

**released**() [🔗](class_touchscreenbutton.md#class-touchscreenbutton-signal-released)

Emitted when the button is released (up).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-touchscreenbutton-visibilitymode"></a>

enum **VisibilityMode**: [🔗](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode)

<a id="class-touchscreenbutton-constant-visibility-always"></a>

[VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode) **VISIBILITY_ALWAYS** = `0`

Always visible.

<a id="class-touchscreenbutton-constant-visibility-touchscreen-only"></a>

[VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode) **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-touchscreenbutton-property-action"></a>

[String](class_string.md#class-string) **action** = `""` [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-action)

- void **set_action**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_action**()

The button's action. Actions can be handled with [InputEventAction](class_inputeventaction.md#class-inputeventaction).

---


<a id="class-touchscreenbutton-property-bitmask"></a>

[BitMap](class_bitmap.md#class-bitmap) **bitmask** [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-bitmask)

- void **set_bitmask**(value: [BitMap](class_bitmap.md#class-bitmap))
- [BitMap](class_bitmap.md#class-bitmap) **get_bitmask**()

The button's bitmask.

---


<a id="class-touchscreenbutton-property-passby-press"></a>

[bool](class_bool.md#class-bool) **passby_press** = `false` [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-passby-press)

- void **set_passby_press**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_passby_press_enabled**()

If `true`, the [pressed](class_touchscreenbutton.md#class-touchscreenbutton-signal-pressed) and [released](class_touchscreenbutton.md#class-touchscreenbutton-signal-released) signals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.

**Note:** This is a "pass-by" (not "bypass") press mode.

---


<a id="class-touchscreenbutton-property-shape"></a>

[Shape2D](class_shape2d.md#class-shape2d) **shape** [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-shape)

- void **set_shape**(value: [Shape2D](class_shape2d.md#class-shape2d))
- [Shape2D](class_shape2d.md#class-shape2d) **get_shape**()

The button's shape.

---


<a id="class-touchscreenbutton-property-shape-centered"></a>

[bool](class_bool.md#class-bool) **shape_centered** = `true` [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-shape-centered)

- void **set_shape_centered**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shape_centered**()

If `true`, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.

---


<a id="class-touchscreenbutton-property-shape-visible"></a>

[bool](class_bool.md#class-bool) **shape_visible** = `true` [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-shape-visible)

- void **set_shape_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shape_visible**()

If `true`, the button's shape is visible in the editor.

---


<a id="class-touchscreenbutton-property-texture-normal"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_normal** [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-texture-normal)

- void **set_texture_normal**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_normal**()

The button's texture for the normal state.

---


<a id="class-touchscreenbutton-property-texture-pressed"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_pressed** [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-texture-pressed)

- void **set_texture_pressed**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_pressed**()

The button's texture for the pressed state.

---


<a id="class-touchscreenbutton-property-visibility-mode"></a>

[VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode) **visibility_mode** = `0` [🔗](class_touchscreenbutton.md#class-touchscreenbutton-property-visibility-mode)

- void **set_visibility_mode**(value: [VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode))
- [VisibilityMode](class_touchscreenbutton.md#enum-touchscreenbutton-visibilitymode) **get_visibility_mode**()

The button's visibility mode.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-touchscreenbutton-method-is-pressed"></a>

[bool](class_bool.md#class-bool) **is_pressed**() const [🔗](class_touchscreenbutton.md#class-touchscreenbutton-method-is-pressed)

Returns `true` if this button is currently pressed.
