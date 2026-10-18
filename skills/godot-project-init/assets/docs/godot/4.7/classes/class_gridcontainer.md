> Source: https://docs.godotengine.org/en/4.7/classes/class_gridcontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gridcontainer"></a>

<a id="class-gridcontainer"></a>

# GridContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that arranges its child controls in a grid layout.

<a id="description"></a>

## Description

**GridContainer** arranges its child controls in a grid layout. The number of columns is specified by the [columns](class_gridcontainer.md#class-gridcontainer-property-columns) property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

**Note:** **GridContainer** only works with child nodes inheriting from [Control](class_control.md#class-control). It won't rearrange child nodes inheriting from [Node2D](class_node2d.md#class-node2d).

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)
- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [columns](class_gridcontainer.md#class-gridcontainer-property-columns) | `1` |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [h_separation](class_gridcontainer.md#class-gridcontainer-theme-constant-h-separation) | `4` |
| [int](class_int.md#class-int) | [v_separation](class_gridcontainer.md#class-gridcontainer-theme-constant-v-separation) | `4` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gridcontainer-property-columns"></a>

[int](class_int.md#class-int) **columns** = `1` [🔗](class_gridcontainer.md#class-gridcontainer-property-columns)

- void **set_columns**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_columns**()

The number of columns in the **GridContainer**. If modified, **GridContainer** reorders its Control-derived children to accommodate the new layout.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-gridcontainer-theme-constant-h-separation"></a>

[int](class_int.md#class-int) **h_separation** = `4` [🔗](class_gridcontainer.md#class-gridcontainer-theme-constant-h-separation)

The horizontal separation of child nodes.

---


<a id="class-gridcontainer-theme-constant-v-separation"></a>

[int](class_int.md#class-int) **v_separation** = `4` [🔗](class_gridcontainer.md#class-gridcontainer-theme-constant-v-separation)

The vertical separation of child nodes.
