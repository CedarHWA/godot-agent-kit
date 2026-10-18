> Source: https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/objectdb_profiler.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="using-the-objectdb-profiler"></a>

<a id="doc-objectdb-profiler"></a>

# Using the ObjectDB profiler

Since Godot 4.6, there is a new **ObjectDB Profiler** tab in the Debugger bottom panel.
This profiler allows you to take snapshots of the current state of the ObjectDB,
which is the database that contains all the [Object](../../../classes/class_object.md#class-object)-derived classes
currently allocated in memory. This is useful for identifying memory leaks and
understanding the memory usage of your project.

Additionally, this tool is able to visualize differences between two snapshots.
This can be used to identify improvements or regressions in memory usage after
making changes to your project. Reducing memory usage can lead to better performance,
even in cases where memory is not a bottleneck. By reducing memory usage,
you can perform fewer allocations, which can be a costly operation, especially
if performed in large amounts during gameplay.

See also

See [When and how to avoid using nodes for everything](../../best_practices/node_alternatives.md#doc-node-alternatives) for information on using lighter-weight
alternatives to nodes, which can help reduce memory usage in your project.

Warning

The ObjectDB profiler does **not** track every bit of memory used by the engine or
by external libraries. Native engine classes that are not exposed to the scripting
API will not appear in snapshots.

Consider using external memory profiling tools if you need access to this information.

<a id="usage"></a>

## Usage

Open the ObjectDB Profiler tab in the Debugger bottom panel.
You will land on the summary page with no snapshots taken yet.

<a id="id1"></a>
![ObjectDB profiler summary with no snapshots taken](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_summary_no_snapshots.webp)


ObjectDB profiler summary with no snapshots taken

Run the project, then get to a point where you'd like to take a snapshot
(for example, after loading a level). Click Take ObjectDB Snapshot
to take a snapshot at the current point in time. If the button appears grayed out,
make sure the project is running first.

<a id="id2"></a>
![ObjectDB profiler summary with one snapshot taken](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_summary_snapshot.webp)


ObjectDB profiler summary with one snapshot taken

You can take multiple snapshots during a single run of the project.
Also, you can right-click a snapshot in the snapshot list to rename it,
show it in the file manager, or delete it.

Tip

It's a good idea to rename snapshots
after taking them to give them descriptive names (e.g., `before_optimization`,
`after_optimization`). Regardless of the name, the date at which the snapshot
was taken remains saved in the snapshot file itself.

Snapshot files have a `.odb_snapshot` extension and are located in
`user://objectdb_snapshots/` (see [Data paths](../../io/data_paths.md#doc-data-paths-accessing-persistent-user-data)
details). These can safely be copied across devices, as they're platform-independent.

<a id="viewing-differences-between-snapshots"></a>

### Viewing differences between snapshots

After taking at least two snapshots, the Diff Against dropdown becomes
available. Here, you can select another snapshot to compare the currently selected
snapshot with.

<a id="id3"></a>
![Diff Against dropdown in the bottom-left corner of the ObjectDB profiler](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_summary_diff_against.webp)


Diff Against dropdown in the bottom-left corner of the ObjectDB profiler

The summary page will then show the differences between the two snapshots:

<a id="id4"></a>
![Two snapshots being compared in the Summary tab](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_summary_snapshot_diff.webp)


Two snapshots being compared in the Summary tab

This also applies to every other tab in the ObjectDB profiler, which will show
the differences between the two snapshots in additional columns.

<a id="classes"></a>

### Classes

In the Classes tab, you can view how many instances of each class have been
created at the moment the snapshot was taken:

<a id="id5"></a>
![One snapshots being viewed in the Classes tab](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_classes.webp)


One snapshots being viewed in the Classes tab

When in diff mode, it will show the class instance count for the currently
selected snapshot (column A) and the snapshot that is being diffed against
(column B). It will also show the difference in instance count in the column Delta.

<a id="id6"></a>
![Two snapshots being compared in the Classes tab. Here, column A is ``second_session``, column B is ``first_session``](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_classes_diff.webp)


Two snapshots being compared in the Classes tab. Here, column A is `second_session`, column B is `first_session`

You can click on a class in the list on the right to view it in the inspector.

<a id="id7"></a>
![A selected class instance being viewed in the inspector](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_classes_inspector.webp)


A selected class instance being viewed in the inspector

Tip

Previewing instances in the inspector is also available in other tabs
(Nodes, Objects, and RefCounted).

<a id="objects"></a>

### Objects

The Objects tab is similar, but differs in the way it presents data. Here,
every instance is listed in a linear fashion, instead of grouping them by class.
When selecting an object, you will see a list of other objects it references
on the right (Outbound References), as well as a list of objects
it's being referenced by (Inbound References).

This allows you to view objects either in a "top-down" manner (viewing
what objects a given object references) or in a "bottom-up" manner (viewing
what objects reference a given object).

<a id="id8"></a>
![The Objects tab being used to view objects in a "top-down" manner](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_objects_top_down.webp)


The Objects tab being used to view objects in a "top-down" manner

In the above image, clicking the `default_font` object in the list will
switch the view to the perspective of that object. This object is being
referenced by a lot of other objects as well, which effectively switches
to a "bottom-up" perspective.

<a id="id9"></a>
![The Objects tab being used to view objects in a "bottom-up" manner](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_objects_bottom_up.webp)


The Objects tab being used to view objects in a "bottom-up" manner

<a id="nodes"></a>

### Nodes

Next, the Nodes tab shows the scene tree at the time the snapshot was taken.

<a id="id10"></a>
![The Nodes tab being used to view the scene tree](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_nodes.webp)


The Nodes tab being used to view the scene tree

This tab is particularly interesting in diff view, since it supports showing
the difference between the two snapshots in a more visual manner.
When Combined Diff is unchecked, you can see the differences side by side.

<a id="id11"></a>
![Separate diff view in the Nodes tab](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_nodes_diff_separate.webp)


Separate diff view in the Nodes tab

When Combined Diff is checked, you can see the differences merged
into a single tree, with added nodes highlighted in green and removed nodes
highlighted in red.

<a id="id12"></a>
![Combined diff view in the Nodes tab](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_nodes_diff_combined.webp)


Combined diff view in the Nodes tab

Additionally, you can view a list of orphan nodes (nodes that are not
attached to the scene tree root) at the end of the tree view. You can view
it more easily by collapsing the root node, since these are listed outside
the main scene tree.

<a id="id13"></a>
![Orphan nodes at the end of the nodes tree in the ObjectDB profiler](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_nodes_orphan.webp)


Orphan nodes at the end of the nodes tree in the ObjectDB profiler

<a id="refcounted"></a>

### RefCounted

The last tab is the RefCounted tab. This tab is similar to the Objects
tab, but it shows the reference counts of [RefCounted](../../../classes/class_refcounted.md#class-refcounted)-derived
classes directly in the table. The table has four columns:

- **Native Refs:** The number of native engine references to the object.
- **ObjectDB Refs:** The number of ObjectDB references to the object.
- **Total Refs:** The sum of native references and ObjectDB references.
- **ObjectDB Cycles:** The number of circular references detected.

When in diff view, snapshot B is always listed *above* snapshot A
if a RefCounted instance exists in both snapshots.

The list on the right shows details on the selected instance,
including a list of references and whether these are duplicates.

<a id="id14"></a>
![The RefCounted tab being used to view RefCounted instances](https://docs.godotengine.org/en/4.7/_images/objectdb_profiler_refcounted.webp)


The RefCounted tab being used to view RefCounted instances

Note

The RefCounted tab does **not** list objects that derive directly from
[Object](../../../classes/class_object.md#class-object), as these don't use reference counting.
