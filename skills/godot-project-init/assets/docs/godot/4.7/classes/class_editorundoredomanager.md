> Source: https://docs.godotengine.org/en/4.7/classes/class_editorundoredomanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorundoredomanager"></a>

<a id="class-editorundoredomanager"></a>

# EditorUndoRedoManager

**Inherits:** [Object](class_object.md#class-object)

Manages undo history of scenes opened in the editor.

<a id="description"></a>

## Description

**EditorUndoRedoManager** is a manager for [UndoRedo](class_undoredo.md#class-undoredo) objects associated with edited scenes. Each scene has its own undo history and **EditorUndoRedoManager** ensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes ([ProjectSettings](class_projectsettings.md#class-projectsettings) edits, external resources, etc.), a separate global history is used.

The usage is mostly the same as [UndoRedo](class_undoredo.md#class-undoredo). You create and commit actions and the manager automatically decides under-the-hood what scenes it belongs to. The scene is deduced based on the first operation in an action, using the object from the operation. The rules are as follows:

- If the object is a [Node](class_node.md#class-node), use the currently edited scene;
- If the object is a built-in resource, use the scene from its path;
- If the object is external resource or anything else, use global history.

This guessing can sometimes yield false results, so you can provide a custom context object when creating an action.

**EditorUndoRedoManager** is intended to be used by Godot editor plugins. You can obtain it using [EditorPlugin.get_undo_redo()](class_editorplugin.md#class-editorplugin-method-get-undo-redo). For non-editor uses or plugins that don't need to integrate with the editor's undo history, use [UndoRedo](class_undoredo.md#class-undoredo) instead.

The manager's API is mostly the same as in [UndoRedo](class_undoredo.md#class-undoredo), so you can refer to its documentation for more examples. The main difference is that **EditorUndoRedoManager** uses object + method name for actions, instead of [Callable](class_callable.md#class-callable).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_do_method](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-method)(object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), ...) vararg |
| void | [add_do_property](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-property)(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |
| void | [add_do_reference](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-reference)(object: [Object](class_object.md#class-object)) |
| void | [add_undo_method](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-method)(object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), ...) vararg |
| void | [add_undo_property](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-property)(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |
| void | [add_undo_reference](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-reference)(object: [Object](class_object.md#class-object)) |
| void | [clear_history](class_editorundoredomanager.md#class-editorundoredomanager-method-clear-history)(id: [int](class_int.md#class-int) = -99, increase_version: [bool](class_bool.md#class-bool) = true) |
| void | [commit_action](class_editorundoredomanager.md#class-editorundoredomanager-method-commit-action)(execute: [bool](class_bool.md#class-bool) = true) |
| void | [create_action](class_editorundoredomanager.md#class-editorundoredomanager-method-create-action)(name: [String](class_string.md#class-string), merge_mode: [MergeMode](class_undoredo.md#enum-undoredo-mergemode) = 0, custom_context: [Object](class_object.md#class-object) = null, backward_undo_ops: [bool](class_bool.md#class-bool) = false, mark_unsaved: [bool](class_bool.md#class-bool) = true) |
| void | [force_fixed_history](class_editorundoredomanager.md#class-editorundoredomanager-method-force-fixed-history)() |
| [UndoRedo](class_undoredo.md#class-undoredo) | [get_history_undo_redo](class_editorundoredomanager.md#class-editorundoredomanager-method-get-history-undo-redo)(id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_object_history_id](class_editorundoredomanager.md#class-editorundoredomanager-method-get-object-history-id)(object: [Object](class_object.md#class-object)) const |
| [bool](class_bool.md#class-bool) | [is_committing_action](class_editorundoredomanager.md#class-editorundoredomanager-method-is-committing-action)() const |

---


<a id="signals"></a>

## Signals

<a id="class-editorundoredomanager-signal-history-changed"></a>

**history_changed**() [🔗](class_editorundoredomanager.md#class-editorundoredomanager-signal-history-changed)

Emitted when the list of actions in any history has changed, either when an action is committed or a history is cleared.

---


<a id="class-editorundoredomanager-signal-version-changed"></a>

**version_changed**() [🔗](class_editorundoredomanager.md#class-editorundoredomanager-signal-version-changed)

Emitted when the version of any history has changed as a result of undo or redo call.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorundoredomanager-specialhistory"></a>

enum **SpecialHistory**: [🔗](class_editorundoredomanager.md#enum-editorundoredomanager-specialhistory)

<a id="class-editorundoredomanager-constant-global-history"></a>

[SpecialHistory](class_editorundoredomanager.md#enum-editorundoredomanager-specialhistory) **GLOBAL_HISTORY** = `0`

Global history not associated with any scene, but with external resources etc.

<a id="class-editorundoredomanager-constant-remote-history"></a>

[SpecialHistory](class_editorundoredomanager.md#enum-editorundoredomanager-specialhistory) **REMOTE_HISTORY** = `-9`

History associated with remote inspector. Used when live editing a running project.

<a id="class-editorundoredomanager-constant-invalid-history"></a>

[SpecialHistory](class_editorundoredomanager.md#enum-editorundoredomanager-specialhistory) **INVALID_HISTORY** = `-99`

Invalid "null" history. It's a special value, not associated with any object.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorundoredomanager-method-add-do-method"></a>

void **add_do_method**(object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), ...) vararg [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-method)

Register a method that will be called when the action is committed (i.e. the "do" action).

If this is the first operation, the `object` will be used to deduce target undo history.

---


<a id="class-editorundoredomanager-method-add-do-property"></a>

void **add_do_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-property)

Register a property value change for "do".

If this is the first operation, the `object` will be used to deduce target undo history.

---


<a id="class-editorundoredomanager-method-add-do-reference"></a>

void **add_do_reference**(object: [Object](class_object.md#class-object)) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-reference)

Register a reference for "do" that will be erased if the "do" history is lost. This is useful mostly for new nodes created for the "do" call. Do not use for resources.

---


<a id="class-editorundoredomanager-method-add-undo-method"></a>

void **add_undo_method**(object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), ...) vararg [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-method)

Register a method that will be called when the action is undone (i.e. the "undo" action).

If this is the first operation, the `object` will be used to deduce target undo history.

---


<a id="class-editorundoredomanager-method-add-undo-property"></a>

void **add_undo_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-property)

Register a property value change for "undo".

If this is the first operation, the `object` will be used to deduce target undo history.

---


<a id="class-editorundoredomanager-method-add-undo-reference"></a>

void **add_undo_reference**(object: [Object](class_object.md#class-object)) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-reference)

Register a reference for "undo" that will be erased if the "undo" history is lost. This is useful mostly for nodes removed with the "do" call (not the "undo" call!).

---


<a id="class-editorundoredomanager-method-clear-history"></a>

void **clear_history**(id: [int](class_int.md#class-int) = -99, increase_version: [bool](class_bool.md#class-bool) = true) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-clear-history)

Clears the given undo history. You can clear history for a specific scene, global history, or for all histories at once (except [REMOTE_HISTORY](class_editorundoredomanager.md#class-editorundoredomanager-constant-remote-history)) if `id` is [INVALID_HISTORY](class_editorundoredomanager.md#class-editorundoredomanager-constant-invalid-history).

If `increase_version` is `true`, the undo history version will be increased, marking it as unsaved. Useful for operations that modify the scene, but don't support undo.

```gdscript
var scene_root = EditorInterface.get_edited_scene_root()
var undo_redo = EditorInterface.get_editor_undo_redo()
undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))
```

**Note:** If you want to mark an edited scene as unsaved without clearing its history, use [EditorInterface.mark_scene_as_unsaved()](class_editorinterface.md#class-editorinterface-method-mark-scene-as-unsaved) instead.

---


<a id="class-editorundoredomanager-method-commit-action"></a>

void **commit_action**(execute: [bool](class_bool.md#class-bool) = true) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-commit-action)

Commits the action. If `execute` is `true` (default), all "do" methods/properties are called/set when this function is called.

---


<a id="class-editorundoredomanager-method-create-action"></a>

void **create_action**(name: [String](class_string.md#class-string), merge_mode: [MergeMode](class_undoredo.md#enum-undoredo-mergemode) = 0, custom_context: [Object](class_object.md#class-object) = null, backward_undo_ops: [bool](class_bool.md#class-bool) = false, mark_unsaved: [bool](class_bool.md#class-bool) = true) [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-create-action)

Create a new action. After this is called, do all your calls to [add_do_method()](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-method), [add_undo_method()](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-method), [add_do_property()](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-property), and [add_undo_property()](class_editorundoredomanager.md#class-editorundoredomanager-method-add-undo-property), then commit the action with [commit_action()](class_editorundoredomanager.md#class-editorundoredomanager-method-commit-action).

The way actions are merged is dictated by the `merge_mode` argument.

If `custom_context` object is provided, it will be used for deducing target history (instead of using the first operation).

The way undo operation are ordered in actions is dictated by `backward_undo_ops`. When `backward_undo_ops` is `false` undo option are ordered in the same order they were added. Which means the first operation to be added will be the first to be undone.

If `mark_unsaved` is `false`, the action will not mark the history as unsaved. This is useful for example for actions that change a selection, or a setting that will be saved automatically. Otherwise, this should be left to `true` if the action requires saving by the user or if it can cause data loss when left unsaved.

---


<a id="class-editorundoredomanager-method-force-fixed-history"></a>

void **force_fixed_history**() [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-force-fixed-history)

Forces the next operation (e.g. [add_do_method()](class_editorundoredomanager.md#class-editorundoredomanager-method-add-do-method)) to use the action's history rather than guessing it from the object. This is sometimes needed when a history can't be correctly determined, like for a nested resource that doesn't have a path yet.

This method should only be used when absolutely necessary, otherwise it might cause invalid history state. For most of complex cases, the `custom_context` parameter of [create_action()](class_editorundoredomanager.md#class-editorundoredomanager-method-create-action) is sufficient.

---


<a id="class-editorundoredomanager-method-get-history-undo-redo"></a>

[UndoRedo](class_undoredo.md#class-undoredo) **get_history_undo_redo**(id: [int](class_int.md#class-int)) const [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-get-history-undo-redo)

Returns the [UndoRedo](class_undoredo.md#class-undoredo) object associated with the given history `id`.

`id` above `0` are mapped to the opened scene tabs (but it doesn't match their order). `id` of `0` or lower have special meaning (see [SpecialHistory](class_editorundoredomanager.md#enum-editorundoredomanager-specialhistory)).

Best used with [get_object_history_id()](class_editorundoredomanager.md#class-editorundoredomanager-method-get-object-history-id). This method is only provided in case you need some more advanced methods of [UndoRedo](class_undoredo.md#class-undoredo) (but keep in mind that directly operating on the [UndoRedo](class_undoredo.md#class-undoredo) object might affect editor's stability).

---


<a id="class-editorundoredomanager-method-get-object-history-id"></a>

[int](class_int.md#class-int) **get_object_history_id**(object: [Object](class_object.md#class-object)) const [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-get-object-history-id)

Returns the history ID deduced from the given `object`. It can be used with [get_history_undo_redo()](class_editorundoredomanager.md#class-editorundoredomanager-method-get-history-undo-redo).

---


<a id="class-editorundoredomanager-method-is-committing-action"></a>

[bool](class_bool.md#class-bool) **is_committing_action**() const [🔗](class_editorundoredomanager.md#class-editorundoredomanager-method-is-committing-action)

Returns `true` if the **EditorUndoRedoManager** is currently committing the action, i.e. running its "do" method or property change (see [commit_action()](class_editorundoredomanager.md#class-editorundoredomanager-method-commit-action)).
