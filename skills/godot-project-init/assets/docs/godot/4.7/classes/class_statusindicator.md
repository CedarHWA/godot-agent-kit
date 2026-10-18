> Source: https://docs.godotengine.org/en/4.7/classes/class_statusindicator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="statusindicator"></a>

<a id="class-statusindicator"></a>

# StatusIndicator

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Application status indicator (aka notification area icon).

**Note:** Status indicator is implemented on macOS and Windows.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Texture2D](class_texture2d.md#class-texture2d) | [icon](class_statusindicator.md#class-statusindicator-property-icon) |  |
| [NodePath](class_nodepath.md#class-nodepath) | [menu](class_statusindicator.md#class-statusindicator-property-menu) | `NodePath("")` |
| [String](class_string.md#class-string) | [tooltip](class_statusindicator.md#class-statusindicator-property-tooltip) | `""` |
| [bool](class_bool.md#class-bool) | [visible](class_statusindicator.md#class-statusindicator-property-visible) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Rect2](class_rect2.md#class-rect2) | [get_rect](class_statusindicator.md#class-statusindicator-method-get-rect)() const |

---


<a id="signals"></a>

## Signals

<a id="class-statusindicator-signal-pressed"></a>

**pressed**(mouse_button: [int](class_int.md#class-int), mouse_position: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_statusindicator.md#class-statusindicator-signal-pressed)

Emitted when the status indicator is pressed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-statusindicator-property-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **icon** [🔗](class_statusindicator.md#class-statusindicator-property-icon)

- void **set_icon**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_icon**()

Status indicator icon.

---


<a id="class-statusindicator-property-menu"></a>

[NodePath](class_nodepath.md#class-nodepath) **menu** = `NodePath("")` [🔗](class_statusindicator.md#class-statusindicator-property-menu)

- void **set_menu**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_menu**()

Status indicator native popup menu. If this is set, the [pressed](class_statusindicator.md#class-statusindicator-signal-pressed) signal is not emitted.

**Note:** Native popup is only supported if [NativeMenu](class_nativemenu.md#class-nativemenu) supports [NativeMenu.FEATURE_POPUP_MENU](class_nativemenu.md#class-nativemenu-constant-feature-popup-menu) feature.

---


<a id="class-statusindicator-property-tooltip"></a>

[String](class_string.md#class-string) **tooltip** = `""` [🔗](class_statusindicator.md#class-statusindicator-property-tooltip)

- void **set_tooltip**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_tooltip**()

Status indicator tooltip.

---


<a id="class-statusindicator-property-visible"></a>

[bool](class_bool.md#class-bool) **visible** = `true` [🔗](class_statusindicator.md#class-statusindicator-property-visible)

- void **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, the status indicator is visible.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-statusindicator-method-get-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_rect**() const [🔗](class_statusindicator.md#class-statusindicator-method-get-rect)

Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an empty [Rect2](class_rect2.md#class-rect2).
