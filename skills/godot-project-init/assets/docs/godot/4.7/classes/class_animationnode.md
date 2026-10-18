> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnode.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnode"></a>

<a id="class-animationnode"></a>

# AnimationNode

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimationNodeExtension](class_animationnodeextension.md#class-animationnodeextension), [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput), [AnimationNodeSync](class_animationnodesync.md#class-animationnodesync), [AnimationNodeTimeScale](class_animationnodetimescale.md#class-animationnodetimescale), [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek), [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)

Base class for [AnimationTree](class_animationtree.md#class-animationtree) nodes. Not related to scene nodes.

<a id="description"></a>

## Description

Base resource for [AnimationTree](class_animationtree.md#class-animationtree) nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

Inherit this when creating animation nodes mainly for use in [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree), otherwise [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) should be used instead.

You can access the time information as read-only parameter which is processed and stored in the previous frame for all nodes except [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput).

**Note:** If multiple inputs exist in the **AnimationNode**, which time information takes precedence depends on the type of **AnimationNode**.

```gdscript
var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]
```

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [filter_enabled](class_animationnode.md#class-animationnode-property-filter-enabled) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [_get_caption](class_animationnode.md#class-animationnode-private-method-get-caption)() virtual const |
| [AnimationNode](class_animationnode.md#class-animationnode) | [_get_child_by_name](class_animationnode.md#class-animationnode-private-method-get-child-by-name)(name: [StringName](class_stringname.md#class-stringname)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_child_nodes](class_animationnode.md#class-animationnode-private-method-get-child-nodes)() virtual const |
| [Variant](class_variant.md#class-variant) | [_get_parameter_default_value](class_animationnode.md#class-animationnode-private-method-get-parameter-default-value)(parameter: [StringName](class_stringname.md#class-stringname)) virtual const |
| [Array](class_array.md#class-array) | [_get_parameter_list](class_animationnode.md#class-animationnode-private-method-get-parameter-list)() virtual const |
| [bool](class_bool.md#class-bool) | [_has_filter](class_animationnode.md#class-animationnode-private-method-has-filter)() virtual const |
| [bool](class_bool.md#class-bool) | [_is_parameter_read_only](class_animationnode.md#class-animationnode-private-method-is-parameter-read-only)(parameter: [StringName](class_stringname.md#class-stringname)) virtual const |
| [float](class_float.md#class-float) | [_process](class_animationnode.md#class-animationnode-private-method-process)(time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), test_only: [bool](class_bool.md#class-bool)) virtual |
| [bool](class_bool.md#class-bool) | [add_input](class_animationnode.md#class-animationnode-method-add-input)(name: [String](class_string.md#class-string)) |
| void | [blend_animation](class_animationnode.md#class-animationnode-method-blend-animation)(animation: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float), delta: [float](class_float.md#class-float), seeked: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), looped_flag: [LoopedFlag](class_animation.md#enum-animation-loopedflag) = 0) |
| [float](class_float.md#class-float) | [blend_input](class_animationnode.md#class-animationnode-method-blend-input)(input_index: [int](class_int.md#class-int), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: [FilterAction](class_animationnode.md#enum-animationnode-filteraction) = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false) |
| [float](class_float.md#class-float) | [blend_node](class_animationnode.md#class-animationnode-method-blend-node)(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: [FilterAction](class_animationnode.md#enum-animationnode-filteraction) = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int) | [find_input](class_animationnode.md#class-animationnode-method-find-input)(name: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [get_input_count](class_animationnode.md#class-animationnode-method-get-input-count)() const |
| [String](class_string.md#class-string) | [get_input_name](class_animationnode.md#class-animationnode-method-get-input-name)(input: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_parameter](class_animationnode.md#class-animationnode-method-get-parameter)(name: [StringName](class_stringname.md#class-stringname)) const |
| [int](class_int.md#class-int) | [get_processing_animation_tree_instance_id](class_animationnode.md#class-animationnode-method-get-processing-animation-tree-instance-id)() const |
| [bool](class_bool.md#class-bool) | [is_path_filtered](class_animationnode.md#class-animationnode-method-is-path-filtered)(path: [NodePath](class_nodepath.md#class-nodepath)) const |
| [bool](class_bool.md#class-bool) | [is_process_testing](class_animationnode.md#class-animationnode-method-is-process-testing)() const |
| void | [remove_input](class_animationnode.md#class-animationnode-method-remove-input)(index: [int](class_int.md#class-int)) |
| void | [set_filter_path](class_animationnode.md#class-animationnode-method-set-filter-path)(path: [NodePath](class_nodepath.md#class-nodepath), enable: [bool](class_bool.md#class-bool)) |
| [bool](class_bool.md#class-bool) | [set_input_name](class_animationnode.md#class-animationnode-method-set-input-name)(input: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [set_parameter](class_animationnode.md#class-animationnode-method-set-parameter)(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |

---


<a id="signals"></a>

## Signals

<a id="class-animationnode-signal-animation-node-removed"></a>

**animation_node_removed**(object_id: [int](class_int.md#class-int), node_name: [String](class_string.md#class-string)) [🔗](class_animationnode.md#class-animationnode-signal-animation-node-removed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes removes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---


<a id="class-animationnode-signal-animation-node-renamed"></a>

**animation_node_renamed**(object_id: [int](class_int.md#class-int), old_name: [String](class_string.md#class-string), new_name: [String](class_string.md#class-string)) [🔗](class_animationnode.md#class-animationnode-signal-animation-node-renamed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation node names changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---


<a id="class-animationnode-signal-node-updated"></a>

**node_updated**(object_id: [int](class_int.md#class-int)) [🔗](class_animationnode.md#class-animationnode-signal-node-updated)

**Experimental:** This signal may be changed or removed in future versions.

Emitted by [AnimationNodeAnimation](class_animationnodeanimation.md#class-animationnodeanimation) when its [AnimationNodeAnimation.animation](class_animationnodeanimation.md#class-animationnodeanimation-property-animation) resource is changed, or by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree) when its connections change.

---


<a id="class-animationnode-signal-tree-changed"></a>

**tree_changed**() [🔗](class_animationnode.md#class-animationnode-signal-tree-changed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree) and [AnimationNodeTransition](class_animationnodetransition.md#class-animationnodetransition).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnode-filteraction"></a>

enum **FilterAction**: [🔗](class_animationnode.md#enum-animationnode-filteraction)

<a id="class-animationnode-constant-filter-ignore"></a>

[FilterAction](class_animationnode.md#enum-animationnode-filteraction) **FILTER_IGNORE** = `0`

Do not use filtering.

<a id="class-animationnode-constant-filter-pass"></a>

[FilterAction](class_animationnode.md#enum-animationnode-filteraction) **FILTER_PASS** = `1`

Paths matching the filter will be allowed to pass.

<a id="class-animationnode-constant-filter-stop"></a>

[FilterAction](class_animationnode.md#enum-animationnode-filteraction) **FILTER_STOP** = `2`

Paths matching the filter will be discarded.

<a id="class-animationnode-constant-filter-blend"></a>

[FilterAction](class_animationnode.md#enum-animationnode-filteraction) **FILTER_BLEND** = `3`

Paths matching the filter will be blended (by the blend value).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnode-property-filter-enabled"></a>

[bool](class_bool.md#class-bool) **filter_enabled** [🔗](class_animationnode.md#class-animationnode-property-filter-enabled)

- void **set_filter_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_filter_enabled**()

If `true`, filtering is enabled.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationnode-private-method-get-caption"></a>

[String](class_string.md#class-string) **_get_caption**() virtual const [🔗](class_animationnode.md#class-animationnode-private-method-get-caption)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to override the text caption for this animation node.

---


<a id="class-animationnode-private-method-get-child-by-name"></a>

[AnimationNode](class_animationnode.md#class-animationnode) **_get_child_by_name**(name: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_animationnode.md#class-animationnode-private-method-get-child-by-name)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return a child animation node by its `name`.

---


<a id="class-animationnode-private-method-get-child-nodes"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_child_nodes**() virtual const [🔗](class_animationnode.md#class-animationnode-private-method-get-child-nodes)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return all child animation nodes in order as a `name: node` dictionary.

---


<a id="class-animationnode-private-method-get-parameter-default-value"></a>

[Variant](class_variant.md#class-variant) **_get_parameter_default_value**(parameter: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_animationnode.md#class-animationnode-private-method-get-parameter-default-value)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return the default value of a `parameter`. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---


<a id="class-animationnode-private-method-get-parameter-list"></a>

[Array](class_array.md#class-array) **_get_parameter_list**() virtual const [🔗](class_animationnode.md#class-animationnode-private-method-get-parameter-list)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return a list of the properties on this animation node. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees. Format is similar to [Object.get_property_list()](class_object.md#class-object-method-get-property-list).

---


<a id="class-animationnode-private-method-has-filter"></a>

[bool](class_bool.md#class-bool) **_has_filter**() virtual const [🔗](class_animationnode.md#class-animationnode-private-method-has-filter)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return whether the blend tree editor should display filter editing on this animation node.

---


<a id="class-animationnode-private-method-is-parameter-read-only"></a>

[bool](class_bool.md#class-bool) **_is_parameter_read_only**(parameter: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_animationnode.md#class-animationnode-private-method-is-parameter-read-only)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return whether the `parameter` is read-only. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---


<a id="class-animationnode-private-method-process"></a>

[float](class_float.md#class-float) **_process**(time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), test_only: [bool](class_bool.md#class-bool)) virtual [🔗](class_animationnode.md#class-animationnode-private-method-process)

**Deprecated:** Currently this is mostly useless as there is a lack of many APIs to extend AnimationNode by GDScript. It is planned that a more flexible API using structures will be provided in the future.

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to run some code when this animation node is processed. The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute.

Here, call the [blend_input()](class_animationnode.md#class-animationnode-method-blend-input), [blend_node()](class_animationnode.md#class-animationnode-method-blend-node) or [blend_animation()](class_animationnode.md#class-animationnode-method-blend-animation) functions. You can also use [get_parameter()](class_animationnode.md#class-animationnode-method-get-parameter) and [set_parameter()](class_animationnode.md#class-animationnode-method-set-parameter) to modify local memory.

This function should return the delta.

---


<a id="class-animationnode-method-add-input"></a>

[bool](class_bool.md#class-bool) **add_input**(name: [String](class_string.md#class-string)) [🔗](class_animationnode.md#class-animationnode-method-add-input)

Adds an input to the animation node. This is only useful for animation nodes created for use in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). If the addition fails, returns `false`.

---


<a id="class-animationnode-method-blend-animation"></a>

void **blend_animation**(animation: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float), delta: [float](class_float.md#class-float), seeked: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), looped_flag: [LoopedFlag](class_animation.md#enum-animation-loopedflag) = 0) [🔗](class_animationnode.md#class-animationnode-method-blend-animation)

Blends an animation by `blend` amount (name must be valid in the linked [AnimationPlayer](class_animationplayer.md#class-animationplayer)). A `time` and `delta` may be passed, as well as whether `seeked` happened.

A `looped_flag` is used by internal processing immediately after the loop.

---


<a id="class-animationnode-method-blend-input"></a>

[float](class_float.md#class-float) **blend_input**(input_index: [int](class_int.md#class-int), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: [FilterAction](class_animationnode.md#enum-animationnode-filteraction) = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false) [🔗](class_animationnode.md#class-animationnode-method-blend-input)

Blends an input. This is only useful for animation nodes created for an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute. A filter mode may be optionally passed.

---


<a id="class-animationnode-method-blend-node"></a>

[float](class_float.md#class-float) **blend_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: [FilterAction](class_animationnode.md#enum-animationnode-filteraction) = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false) [🔗](class_animationnode.md#class-animationnode-method-blend-node)

Blend another animation node (in case this animation node contains child animation nodes). This function is only useful if you inherit from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) instead, otherwise editors will not display your animation node for addition.

---


<a id="class-animationnode-method-find-input"></a>

[int](class_int.md#class-int) **find_input**(name: [String](class_string.md#class-string)) const [🔗](class_animationnode.md#class-animationnode-method-find-input)

Returns the input index which corresponds to `name`. If not found, returns `-1`.

---


<a id="class-animationnode-method-get-input-count"></a>

[int](class_int.md#class-int) **get_input_count**() const [🔗](class_animationnode.md#class-animationnode-method-get-input-count)

Amount of inputs in this animation node, only useful for animation nodes that go into [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---


<a id="class-animationnode-method-get-input-name"></a>

[String](class_string.md#class-string) **get_input_name**(input: [int](class_int.md#class-int)) const [🔗](class_animationnode.md#class-animationnode-method-get-input-name)

Gets the name of an input by index.

---


<a id="class-animationnode-method-get-parameter"></a>

[Variant](class_variant.md#class-variant) **get_parameter**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnode.md#class-animationnode-method-get-parameter)

Gets the value of a parameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---


<a id="class-animationnode-method-get-processing-animation-tree-instance-id"></a>

[int](class_int.md#class-int) **get_processing_animation_tree_instance_id**() const [🔗](class_animationnode.md#class-animationnode-method-get-processing-animation-tree-instance-id)

Returns the object id of the [AnimationTree](class_animationtree.md#class-animationtree) that owns this node.

**Note:** This method should only be called from within the [AnimationNodeExtension._process_animation_node()](class_animationnodeextension.md#class-animationnodeextension-private-method-process-animation-node) method, and will return an invalid id otherwise.

---


<a id="class-animationnode-method-is-path-filtered"></a>

[bool](class_bool.md#class-bool) **is_path_filtered**(path: [NodePath](class_nodepath.md#class-nodepath)) const [🔗](class_animationnode.md#class-animationnode-method-is-path-filtered)

Returns `true` if the given path is filtered.

---


<a id="class-animationnode-method-is-process-testing"></a>

[bool](class_bool.md#class-bool) **is_process_testing**() const [🔗](class_animationnode.md#class-animationnode-method-is-process-testing)

Returns `true` if this animation node is being processed in test-only mode.

---


<a id="class-animationnode-method-remove-input"></a>

void **remove_input**(index: [int](class_int.md#class-int)) [🔗](class_animationnode.md#class-animationnode-method-remove-input)

Removes an input, call this only when inactive.

---


<a id="class-animationnode-method-set-filter-path"></a>

void **set_filter_path**(path: [NodePath](class_nodepath.md#class-nodepath), enable: [bool](class_bool.md#class-bool)) [🔗](class_animationnode.md#class-animationnode-method-set-filter-path)

Adds or removes a path for the filter.

---


<a id="class-animationnode-method-set-input-name"></a>

[bool](class_bool.md#class-bool) **set_input_name**(input: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_animationnode.md#class-animationnode-method-set-input-name)

Sets the name of the input at the given `input` index. If the setting fails, returns `false`.

---


<a id="class-animationnode-method-set-parameter"></a>

void **set_parameter**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_animationnode.md#class-animationnode-method-set-parameter)

Sets a custom parameter. These are used as local memory, because resources can be reused across the tree or scenes.
