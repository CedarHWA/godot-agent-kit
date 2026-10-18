> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcontextpersistenceconfig.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcontextpersistenceconfig"></a>

<a id="class-openxrspatialcontextpersistenceconfig"></a>

# OpenXRSpatialContextPersistenceConfig

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for spatial persistence.

<a id="description"></a>

## Description

Configuration header for spatial persistence. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) as the next parameter to create a spatial context with spatial persistence capabilities.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_persistence_context](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-add-persistence-context)(persistence_context: [RID](class_rid.md#class-rid)) |
| [Array](class_array.md#class-array) | [get_persistence_contexts](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-get-persistence-contexts)() const |
| void | [remove_persistence_context](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-remove-persistence-context)(persistence_context: [RID](class_rid.md#class-rid)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcontextpersistenceconfig-method-add-persistence-context"></a>

void **add_persistence_context**(persistence_context: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-add-persistence-context)

Adds a persistence context to this configuration. You must add at least one persistence context to create a valid configuration. You can create a persistence context by calling [OpenXRSpatialAnchorCapability.create_persistence_context()](class_openxrspatialanchorcapability.md#class-openxrspatialanchorcapability-method-create-persistence-context).

---


<a id="class-openxrspatialcontextpersistenceconfig-method-get-persistence-contexts"></a>

[Array](class_array.md#class-array) **get_persistence_contexts**() const [🔗](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-get-persistence-contexts)

Gets the persistence context(s) (as [RID](class_rid.md#class-rid)s) received by [add_persistence_context()](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-add-persistence-context).

---


<a id="class-openxrspatialcontextpersistenceconfig-method-remove-persistence-context"></a>

void **remove_persistence_context**(persistence_context: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig-method-remove-persistence-context)

Removes a persistence context.
