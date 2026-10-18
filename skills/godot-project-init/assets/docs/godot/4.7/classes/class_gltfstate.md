> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfstate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfstate"></a>

<a id="class-gltfstate"></a>

# GLTFState

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [FBXState](class_fbxstate.md#class-fbxstate)

Represents all data of a glTF file.

<a id="description"></a>

## Description

Contains all nodes and resources of a glTF file. This is used by [GLTFDocument](class_gltfdocument.md#class-gltfdocument) as data storage, which allows [GLTFDocument](class_gltfdocument.md#class-gltfdocument) and all [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes to remain stateless.

GLTFState can be populated by [GLTFDocument](class_gltfdocument.md#class-gltfdocument) reading a file or by converting a Godot scene. Then the data can either be used to create a Godot scene or save to a glTF file. The code that converts to/from a Godot scene can be intercepted at arbitrary points by [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes. This allows for custom data to be stored in the glTF file or for custom data to be converted to/from Godot nodes.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [glTF asset header schema](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/schema/asset.schema.json)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [bake_fps](class_gltfstate.md#class-gltfstate-property-bake-fps) | `30.0` |
| [String](class_string.md#class-string) | [base_path](class_gltfstate.md#class-gltfstate-property-base-path) | `""` |
| [Array](class_array.md#class-array)[[PackedByteArray](class_packedbytearray.md#class-packedbytearray)] | [buffers](class_gltfstate.md#class-gltfstate-property-buffers) | `[]` |
| [String](class_string.md#class-string) | [copyright](class_gltfstate.md#class-gltfstate-property-copyright) | `""` |
| [bool](class_bool.md#class-bool) | [create_animations](class_gltfstate.md#class-gltfstate-property-create-animations) | `true` |
| [String](class_string.md#class-string) | [filename](class_gltfstate.md#class-gltfstate-property-filename) | `""` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [glb_data](class_gltfstate.md#class-gltfstate-property-glb-data) | `PackedByteArray()` |
| [HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) | [handle_binary_image_mode](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode) | `1` |
| [bool](class_bool.md#class-bool) | [import_as_skeleton_bones](class_gltfstate.md#class-gltfstate-property-import-as-skeleton-bones) | `false` |
| [Dictionary](class_dictionary.md#class-dictionary) | [json](class_gltfstate.md#class-gltfstate-property-json) | `{}` |
| [int](class_int.md#class-int) | [major_version](class_gltfstate.md#class-gltfstate-property-major-version) | `0` |
| [int](class_int.md#class-int) | [minor_version](class_gltfstate.md#class-gltfstate-property-minor-version) | `0` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [root_nodes](class_gltfstate.md#class-gltfstate-property-root-nodes) | `PackedInt32Array()` |
| [String](class_string.md#class-string) | [scene_name](class_gltfstate.md#class-gltfstate-property-scene-name) | `""` |
| [bool](class_bool.md#class-bool) | [use_named_skin_binds](class_gltfstate.md#class-gltfstate-property-use-named-skin-binds) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_used_extension](class_gltfstate.md#class-gltfstate-method-add-used-extension)(extension_name: [String](class_string.md#class-string), required: [bool](class_bool.md#class-bool)) |
| [int](class_int.md#class-int) | [append_data_to_buffers](class_gltfstate.md#class-gltfstate-method-append-data-to-buffers)(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), deduplication: [bool](class_bool.md#class-bool)) |
| [int](class_int.md#class-int) | [append_gltf_node](class_gltfstate.md#class-gltfstate-method-append-gltf-node)(gltf_node: [GLTFNode](class_gltfnode.md#class-gltfnode), godot_scene_node: [Node](class_node.md#class-node), parent_node_index: [int](class_int.md#class-int)) |
| [Array](class_array.md#class-array)[[GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor)] | [get_accessors](class_gltfstate.md#class-gltfstate-method-get-accessors)() const |
| [Variant](class_variant.md#class-variant) | [get_additional_data](class_gltfstate.md#class-gltfstate-method-get-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname)) const |
| [AnimationPlayer](class_animationplayer.md#class-animationplayer) | [get_animation_player](class_gltfstate.md#class-gltfstate-method-get-animation-player)(anim_player_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_animation_players_count](class_gltfstate.md#class-gltfstate-method-get-animation-players-count)(anim_player_index: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[GLTFAnimation](class_gltfanimation.md#class-gltfanimation)] | [get_animations](class_gltfstate.md#class-gltfstate-method-get-animations)() const |
| [Array](class_array.md#class-array)[[GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview)] | [get_buffer_views](class_gltfstate.md#class-gltfstate-method-get-buffer-views)() const |
| [Array](class_array.md#class-array)[[GLTFCamera](class_gltfcamera.md#class-gltfcamera)] | [get_cameras](class_gltfstate.md#class-gltfstate-method-get-cameras)() const |
| [int](class_int.md#class-int) | [get_handle_binary_image](class_gltfstate.md#class-gltfstate-method-get-handle-binary-image)() const |
| [Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)] | [get_images](class_gltfstate.md#class-gltfstate-method-get-images)() const |
| [Array](class_array.md#class-array)[[GLTFLight](class_gltflight.md#class-gltflight)] | [get_lights](class_gltfstate.md#class-gltfstate-method-get-lights)() const |
| [Array](class_array.md#class-array)[[Material](class_material.md#class-material)] | [get_materials](class_gltfstate.md#class-gltfstate-method-get-materials)() const |
| [Array](class_array.md#class-array)[[GLTFMesh](class_gltfmesh.md#class-gltfmesh)] | [get_meshes](class_gltfstate.md#class-gltfstate-method-get-meshes)() const |
| [int](class_int.md#class-int) | [get_node_index](class_gltfstate.md#class-gltfstate-method-get-node-index)(scene_node: [Node](class_node.md#class-node)) const |
| [Array](class_array.md#class-array)[[GLTFNode](class_gltfnode.md#class-gltfnode)] | [get_nodes](class_gltfstate.md#class-gltfstate-method-get-nodes)() const |
| [Node](class_node.md#class-node) | [get_scene_node](class_gltfstate.md#class-gltfstate-method-get-scene-node)(gltf_node_index: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)] | [get_skeletons](class_gltfstate.md#class-gltfstate-method-get-skeletons)() const |
| [Array](class_array.md#class-array)[[GLTFSkin](class_gltfskin.md#class-gltfskin)] | [get_skins](class_gltfstate.md#class-gltfstate-method-get-skins)() const |
| [Array](class_array.md#class-array)[[GLTFTextureSampler](class_gltftexturesampler.md#class-gltftexturesampler)] | [get_texture_samplers](class_gltfstate.md#class-gltfstate-method-get-texture-samplers)() const |
| [Array](class_array.md#class-array)[[GLTFTexture](class_gltftexture.md#class-gltftexture)] | [get_textures](class_gltfstate.md#class-gltfstate-method-get-textures)() const |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | [get_unique_animation_names](class_gltfstate.md#class-gltfstate-method-get-unique-animation-names)() const |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | [get_unique_names](class_gltfstate.md#class-gltfstate-method-get-unique-names)() const |
| void | [set_accessors](class_gltfstate.md#class-gltfstate-method-set-accessors)(accessors: [Array](class_array.md#class-array)[[GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor)]) |
| void | [set_additional_data](class_gltfstate.md#class-gltfstate-method-set-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |
| void | [set_animations](class_gltfstate.md#class-gltfstate-method-set-animations)(animations: [Array](class_array.md#class-array)[[GLTFAnimation](class_gltfanimation.md#class-gltfanimation)]) |
| void | [set_buffer_views](class_gltfstate.md#class-gltfstate-method-set-buffer-views)(buffer_views: [Array](class_array.md#class-array)[[GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview)]) |
| void | [set_cameras](class_gltfstate.md#class-gltfstate-method-set-cameras)(cameras: [Array](class_array.md#class-array)[[GLTFCamera](class_gltfcamera.md#class-gltfcamera)]) |
| void | [set_handle_binary_image](class_gltfstate.md#class-gltfstate-method-set-handle-binary-image)(method: [int](class_int.md#class-int)) |
| void | [set_images](class_gltfstate.md#class-gltfstate-method-set-images)(images: [Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)]) |
| void | [set_lights](class_gltfstate.md#class-gltfstate-method-set-lights)(lights: [Array](class_array.md#class-array)[[GLTFLight](class_gltflight.md#class-gltflight)]) |
| void | [set_materials](class_gltfstate.md#class-gltfstate-method-set-materials)(materials: [Array](class_array.md#class-array)[[Material](class_material.md#class-material)]) |
| void | [set_meshes](class_gltfstate.md#class-gltfstate-method-set-meshes)(meshes: [Array](class_array.md#class-array)[[GLTFMesh](class_gltfmesh.md#class-gltfmesh)]) |
| void | [set_nodes](class_gltfstate.md#class-gltfstate-method-set-nodes)(nodes: [Array](class_array.md#class-array)[[GLTFNode](class_gltfnode.md#class-gltfnode)]) |
| void | [set_skeletons](class_gltfstate.md#class-gltfstate-method-set-skeletons)(skeletons: [Array](class_array.md#class-array)[[GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)]) |
| void | [set_skins](class_gltfstate.md#class-gltfstate-method-set-skins)(skins: [Array](class_array.md#class-array)[[GLTFSkin](class_gltfskin.md#class-gltfskin)]) |
| void | [set_texture_samplers](class_gltfstate.md#class-gltfstate-method-set-texture-samplers)(texture_samplers: [Array](class_array.md#class-array)[[GLTFTextureSampler](class_gltftexturesampler.md#class-gltftexturesampler)]) |
| void | [set_textures](class_gltfstate.md#class-gltfstate-method-set-textures)(textures: [Array](class_array.md#class-array)[[GLTFTexture](class_gltftexture.md#class-gltftexture)]) |
| void | [set_unique_animation_names](class_gltfstate.md#class-gltfstate-method-set-unique-animation-names)(unique_animation_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) |
| void | [set_unique_names](class_gltfstate.md#class-gltfstate-method-set-unique-names)(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gltfstate-handlebinaryimagemode"></a>

enum **HandleBinaryImageMode**: [🔗](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode)

<a id="class-gltfstate-constant-handle-binary-image-mode-discard-textures"></a>

[HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES** = `0`

When importing a glTF file with embedded binary images, discards all images and uses untextured materials in their place. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.

<a id="class-gltfstate-constant-handle-binary-image-mode-extract-textures"></a>

[HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES** = `1`

When importing a glTF file with embedded binary images, extracts them and saves them to their own files. This allows the image to be imported by Godot's image importer, which can then have their import options customized by the user, including optionally compressing the image to VRAM texture formats.

This will save the images's bytes exactly as-is, without recompression. For image formats supplied by glTF extensions, the file will have a filename ending with the file extension supplied by [GLTFDocumentExtension._get_image_file_extension()](class_gltfdocumentextension.md#class-gltfdocumentextension-private-method-get-image-file-extension) of the extension class.

**Note:** This option is editor-only. At runtime, this acts the same as [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED](class_gltfstate.md#class-gltfstate-constant-handle-binary-image-mode-embed-as-uncompressed).

<a id="class-gltfstate-constant-handle-binary-image-mode-embed-as-basisu"></a>

[HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU** = `2`

When importing a glTF file with embedded binary images, embeds textures VRAM compressed with Basis Universal into the generated scene. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.

<a id="class-gltfstate-constant-handle-binary-image-mode-embed-as-uncompressed"></a>

[HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED** = `3`

When importing a glTF file with embedded binary images, embeds textures compressed losslessly into the generated scene. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.

---


<a id="constants"></a>

## Constants

<a id="class-gltfstate-constant-handle-binary-discard-textures"></a>

**HANDLE_BINARY_DISCARD_TEXTURES** = `0` [🔗](class_gltfstate.md#class-gltfstate-constant-handle-binary-discard-textures)

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES](class_gltfstate.md#class-gltfstate-constant-handle-binary-image-mode-discard-textures) instead.

Discards all embedded textures and uses untextured materials.

<a id="class-gltfstate-constant-handle-binary-extract-textures"></a>

**HANDLE_BINARY_EXTRACT_TEXTURES** = `1` [🔗](class_gltfstate.md#class-gltfstate-constant-handle-binary-extract-textures)

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES](class_gltfstate.md#class-gltfstate-constant-handle-binary-image-mode-extract-textures) instead.

Extracts embedded textures to be reimported and compressed. Editor only. Acts as uncompressed at runtime.

<a id="class-gltfstate-constant-handle-binary-embed-as-basisu"></a>

**HANDLE_BINARY_EMBED_AS_BASISU** = `2` [🔗](class_gltfstate.md#class-gltfstate-constant-handle-binary-embed-as-basisu)

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU](class_gltfstate.md#class-gltfstate-constant-handle-binary-image-mode-embed-as-basisu) instead.

Embeds textures VRAM compressed with Basis Universal into the generated scene.

<a id="class-gltfstate-constant-handle-binary-embed-as-uncompressed"></a>

**HANDLE_BINARY_EMBED_AS_UNCOMPRESSED** = `3` [🔗](class_gltfstate.md#class-gltfstate-constant-handle-binary-embed-as-uncompressed)

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED](class_gltfstate.md#class-gltfstate-constant-handle-binary-image-mode-embed-as-uncompressed) instead.

Embeds textures compressed losslessly into the generated scene, matching old behavior.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfstate-property-bake-fps"></a>

[float](class_float.md#class-float) **bake_fps** = `30.0` [🔗](class_gltfstate.md#class-gltfstate-property-bake-fps)

- void **set_bake_fps**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bake_fps**()

The baking fps of the animation for either import or export.

---


<a id="class-gltfstate-property-base-path"></a>

[String](class_string.md#class-string) **base_path** = `""` [🔗](class_gltfstate.md#class-gltfstate-property-base-path)

- void **set_base_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_base_path**()

The folder path associated with this glTF data. This is used to find other files the glTF file references, like images or binary buffers. This will be set during import when appending from a file, and will be set during export when writing to a file.

---


<a id="class-gltfstate-property-buffers"></a>

[Array](class_array.md#class-array)[[PackedByteArray](class_packedbytearray.md#class-packedbytearray)] **buffers** = `[]` [🔗](class_gltfstate.md#class-gltfstate-property-buffers)

- void **set_buffers**(value: [Array](class_array.md#class-array)[[PackedByteArray](class_packedbytearray.md#class-packedbytearray)])
- [Array](class_array.md#class-array)[[PackedByteArray](class_packedbytearray.md#class-packedbytearray)] **get_buffers**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-property-copyright"></a>

[String](class_string.md#class-string) **copyright** = `""` [🔗](class_gltfstate.md#class-gltfstate-property-copyright)

- void **set_copyright**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_copyright**()

The copyright string in the asset header of the glTF file. This is set during import if present and export if non-empty. See the glTF asset header documentation for more information.

---


<a id="class-gltfstate-property-create-animations"></a>

[bool](class_bool.md#class-bool) **create_animations** = `true` [🔗](class_gltfstate.md#class-gltfstate-property-create-animations)

- void **set_create_animations**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_create_animations**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-property-filename"></a>

[String](class_string.md#class-string) **filename** = `""` [🔗](class_gltfstate.md#class-gltfstate-property-filename)

- void **set_filename**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_filename**()

The file name associated with this glTF data. If it ends with `.gltf`, this is text-based glTF, otherwise this is binary GLB. This will be set during import when appending from a file, and will be set during export when writing to a file. If writing to a buffer, this will be an empty string.

---


<a id="class-gltfstate-property-glb-data"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **glb_data** = `PackedByteArray()` [🔗](class_gltfstate.md#class-gltfstate-property-glb-data)

- void **set_glb_data**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_glb_data**()

The binary buffer attached to a .glb file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-gltfstate-property-handle-binary-image-mode"></a>

[HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **handle_binary_image_mode** = `1` [🔗](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode)

- void **set_handle_binary_image_mode**(value: [HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode))
- [HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) **get_handle_binary_image_mode**()

When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled. Images can be discarded, saved as separate files, or embedded in the scene lossily or losslessly. See [HandleBinaryImageMode](class_gltfstate.md#enum-gltfstate-handlebinaryimagemode) for options.

This property does nothing for image files in the `res://` folder imported by Godot, as those are handled by Godot's image importer directly, and then the Godot scene generated from the glTF file will use the images as Godot imported them.

---


<a id="class-gltfstate-property-import-as-skeleton-bones"></a>

[bool](class_bool.md#class-bool) **import_as_skeleton_bones** = `false` [🔗](class_gltfstate.md#class-gltfstate-property-import-as-skeleton-bones)

- void **set_import_as_skeleton_bones**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_import_as_skeleton_bones**()

If `true`, forces all GLTFNodes in the document to be bones of a single [Skeleton3D](class_skeleton3d.md#class-skeleton3d) Godot node.

---


<a id="class-gltfstate-property-json"></a>

[Dictionary](class_dictionary.md#class-dictionary) **json** = `{}` [🔗](class_gltfstate.md#class-gltfstate-property-json)

- void **set_json**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_json**()

The original raw JSON document corresponding to this GLTFState.

---


<a id="class-gltfstate-property-major-version"></a>

[int](class_int.md#class-int) **major_version** = `0` [🔗](class_gltfstate.md#class-gltfstate-property-major-version)

- void **set_major_version**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_major_version**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-property-minor-version"></a>

[int](class_int.md#class-int) **minor_version** = `0` [🔗](class_gltfstate.md#class-gltfstate-property-minor-version)

- void **set_minor_version**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_minor_version**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-property-root-nodes"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **root_nodes** = `PackedInt32Array()` [🔗](class_gltfstate.md#class-gltfstate-property-root-nodes)

- void **set_root_nodes**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_root_nodes**()

The root nodes of the glTF file. Typically, a glTF file will only have one scene, and therefore one root node. However, a glTF file may have multiple scenes and therefore multiple root nodes, which will be generated as siblings of each other and as children of the root node of the generated Godot scene.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfstate-property-scene-name"></a>

[String](class_string.md#class-string) **scene_name** = `""` [🔗](class_gltfstate.md#class-gltfstate-property-scene-name)

- void **set_scene_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_scene_name**()

The name of the scene. When importing, if not specified, this will be the file name. When exporting, if specified, the scene name will be saved to the glTF file.

---


<a id="class-gltfstate-property-use-named-skin-binds"></a>

[bool](class_bool.md#class-bool) **use_named_skin_binds** = `false` [🔗](class_gltfstate.md#class-gltfstate-property-use-named-skin-binds)

- void **set_use_named_skin_binds**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_named_skin_binds**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfstate-method-add-used-extension"></a>

void **add_used_extension**(extension_name: [String](class_string.md#class-string), required: [bool](class_bool.md#class-bool)) [🔗](class_gltfstate.md#class-gltfstate-method-add-used-extension)

Appends an extension to the list of extensions used by this glTF file during serialization. If `required` is `true`, the extension will also be added to the list of required extensions. Do not run this in [GLTFDocumentExtension._export_post()](class_gltfdocumentextension.md#class-gltfdocumentextension-private-method-export-post), as that stage is too late to add extensions. The final list is sorted alphabetically.

---


<a id="class-gltfstate-method-append-data-to-buffers"></a>

[int](class_int.md#class-int) **append_data_to_buffers**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), deduplication: [bool](class_bool.md#class-bool)) [🔗](class_gltfstate.md#class-gltfstate-method-append-data-to-buffers)

Appends the given byte array `data` to the buffers and creates a [GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview) for it. The index of the destination [GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview) is returned. If `deduplication` is `true`, the buffers are first searched for duplicate data, otherwise new bytes are always appended.

---


<a id="class-gltfstate-method-append-gltf-node"></a>

[int](class_int.md#class-int) **append_gltf_node**(gltf_node: [GLTFNode](class_gltfnode.md#class-gltfnode), godot_scene_node: [Node](class_node.md#class-node), parent_node_index: [int](class_int.md#class-int)) [🔗](class_gltfstate.md#class-gltfstate-method-append-gltf-node)

Appends the given [GLTFNode](class_gltfnode.md#class-gltfnode) to the state, and returns its new index. This can be used to export one Godot node as multiple glTF nodes, or inject new glTF nodes at import time. On import, this must be called before [GLTFDocumentExtension._generate_scene_node()](class_gltfdocumentextension.md#class-gltfdocumentextension-private-method-generate-scene-node) finishes for the parent node. On export, this must be called before [GLTFDocumentExtension._export_node()](class_gltfdocumentextension.md#class-gltfdocumentextension-private-method-export-node) runs for the parent node.

The `godot_scene_node` parameter is the Godot scene node that corresponds to this glTF node. This is highly recommended to be set to a valid node, but may be `null` if there is no corresponding Godot scene node. One Godot scene node may be used for multiple glTF nodes, so if exporting multiple glTF nodes for one Godot scene node, use the same Godot scene node for each.

The `parent_node_index` parameter is the index of the parent [GLTFNode](class_gltfnode.md#class-gltfnode) in the state. If `-1`, the node will be a root node, otherwise the new node will be added to the parent's list of children. The index will also be written to the [GLTFNode.parent](class_gltfnode.md#class-gltfnode-property-parent) property of the new node.

---


<a id="class-gltfstate-method-get-accessors"></a>

[Array](class_array.md#class-array)[[GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor)] **get_accessors**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-accessors)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-get-additional-data"></a>

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_gltfstate.md#class-gltfstate-method-get-additional-data)

Gets additional arbitrary data in this **GLTFState** instance. This can be used to keep per-file state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---


<a id="class-gltfstate-method-get-animation-player"></a>

[AnimationPlayer](class_animationplayer.md#class-animationplayer) **get_animation_player**(anim_player_index: [int](class_int.md#class-int)) const [🔗](class_gltfstate.md#class-gltfstate-method-get-animation-player)

Returns the [AnimationPlayer](class_animationplayer.md#class-animationplayer) node with the given index. These nodes are only used during the export process when converting Godot [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes to glTF animations.

---


<a id="class-gltfstate-method-get-animation-players-count"></a>

[int](class_int.md#class-int) **get_animation_players_count**(anim_player_index: [int](class_int.md#class-int)) const [🔗](class_gltfstate.md#class-gltfstate-method-get-animation-players-count)

Returns the number of [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes in this **GLTFState**. These nodes are only used during the export process when converting Godot [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes to glTF animations.

---


<a id="class-gltfstate-method-get-animations"></a>

[Array](class_array.md#class-array)[[GLTFAnimation](class_gltfanimation.md#class-gltfanimation)] **get_animations**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-animations)

Returns an array of all [GLTFAnimation](class_gltfanimation.md#class-gltfanimation)s in the glTF file. When importing, these will be generated as animations in an [AnimationPlayer](class_animationplayer.md#class-animationplayer) node. When exporting, these will be generated from Godot [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes.

---


<a id="class-gltfstate-method-get-buffer-views"></a>

[Array](class_array.md#class-array)[[GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview)] **get_buffer_views**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-buffer-views)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-get-cameras"></a>

[Array](class_array.md#class-array)[[GLTFCamera](class_gltfcamera.md#class-gltfcamera)] **get_cameras**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-cameras)

Returns an array of all [GLTFCamera](class_gltfcamera.md#class-gltfcamera)s in the glTF file. These are the cameras that the [GLTFNode.camera](class_gltfnode.md#class-gltfnode-property-camera) index refers to.

---


<a id="class-gltfstate-method-get-handle-binary-image"></a>

[int](class_int.md#class-int) **get_handle_binary_image**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-handle-binary-image)

**Deprecated:** Use [handle_binary_image_mode](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode) instead.

Deprecated untyped alias for [handle_binary_image_mode](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode). When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.

---


<a id="class-gltfstate-method-get-images"></a>

[Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)] **get_images**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-images)

Gets the images of the glTF file as an array of [Texture2D](class_texture2d.md#class-texture2d)s. These are the images that the [GLTFTexture.src_image](class_gltftexture.md#class-gltftexture-property-src-image) index refers to.

---


<a id="class-gltfstate-method-get-lights"></a>

[Array](class_array.md#class-array)[[GLTFLight](class_gltflight.md#class-gltflight)] **get_lights**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-lights)

Returns an array of all [GLTFLight](class_gltflight.md#class-gltflight)s in the glTF file. These are the lights that the [GLTFNode.light](class_gltfnode.md#class-gltfnode-property-light) index refers to.

---


<a id="class-gltfstate-method-get-materials"></a>

[Array](class_array.md#class-array)[[Material](class_material.md#class-material)] **get_materials**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-materials)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-get-meshes"></a>

[Array](class_array.md#class-array)[[GLTFMesh](class_gltfmesh.md#class-gltfmesh)] **get_meshes**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-meshes)

Returns an array of all [GLTFMesh](class_gltfmesh.md#class-gltfmesh)es in the glTF file. These are the meshes that the [GLTFNode.mesh](class_gltfnode.md#class-gltfnode-property-mesh) index refers to.

---


<a id="class-gltfstate-method-get-node-index"></a>

[int](class_int.md#class-int) **get_node_index**(scene_node: [Node](class_node.md#class-node)) const [🔗](class_gltfstate.md#class-gltfstate-method-get-node-index)

Returns the index of the [GLTFNode](class_gltfnode.md#class-gltfnode) corresponding to this Godot scene node. This is the inverse of [get_scene_node()](class_gltfstate.md#class-gltfstate-method-get-scene-node). Useful during the export process.

**Note:** Not every Godot scene node will have a corresponding [GLTFNode](class_gltfnode.md#class-gltfnode), and not every [GLTFNode](class_gltfnode.md#class-gltfnode) will have a scene node generated. If there is no [GLTFNode](class_gltfnode.md#class-gltfnode) index for this scene node, `-1` is returned.

---


<a id="class-gltfstate-method-get-nodes"></a>

[Array](class_array.md#class-array)[[GLTFNode](class_gltfnode.md#class-gltfnode)] **get_nodes**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-nodes)

Returns an array of all [GLTFNode](class_gltfnode.md#class-gltfnode)s in the glTF file. These are the nodes that [GLTFNode.children](class_gltfnode.md#class-gltfnode-property-children) and [root_nodes](class_gltfstate.md#class-gltfstate-property-root-nodes) refer to. This includes nodes that may not be generated in the Godot scene, or nodes that may generate multiple Godot scene nodes.

---


<a id="class-gltfstate-method-get-scene-node"></a>

[Node](class_node.md#class-node) **get_scene_node**(gltf_node_index: [int](class_int.md#class-int)) const [🔗](class_gltfstate.md#class-gltfstate-method-get-scene-node)

Returns the Godot scene node that corresponds to the same index as the [GLTFNode](class_gltfnode.md#class-gltfnode) it was generated from. This is the inverse of [get_node_index()](class_gltfstate.md#class-gltfstate-method-get-node-index). Useful during the import process.

**Note:** Not every [GLTFNode](class_gltfnode.md#class-gltfnode) will have a scene node generated, and not every generated scene node will have a corresponding [GLTFNode](class_gltfnode.md#class-gltfnode). If there is no scene node for this [GLTFNode](class_gltfnode.md#class-gltfnode) index, `null` is returned.

---


<a id="class-gltfstate-method-get-skeletons"></a>

[Array](class_array.md#class-array)[[GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)] **get_skeletons**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-skeletons)

Returns an array of all [GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)s in the glTF file. These are the skeletons that the [GLTFNode.skeleton](class_gltfnode.md#class-gltfnode-property-skeleton) index refers to.

---


<a id="class-gltfstate-method-get-skins"></a>

[Array](class_array.md#class-array)[[GLTFSkin](class_gltfskin.md#class-gltfskin)] **get_skins**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-skins)

Returns an array of all [GLTFSkin](class_gltfskin.md#class-gltfskin)s in the glTF file. These are the skins that the [GLTFNode.skin](class_gltfnode.md#class-gltfnode-property-skin) index refers to.

---


<a id="class-gltfstate-method-get-texture-samplers"></a>

[Array](class_array.md#class-array)[[GLTFTextureSampler](class_gltftexturesampler.md#class-gltftexturesampler)] **get_texture_samplers**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-texture-samplers)

Retrieves the array of texture samplers that are used by the textures contained in the glTF.

---


<a id="class-gltfstate-method-get-textures"></a>

[Array](class_array.md#class-array)[[GLTFTexture](class_gltftexture.md#class-gltftexture)] **get_textures**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-textures)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-get-unique-animation-names"></a>

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_unique_animation_names**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-unique-animation-names)

Returns an array of unique animation names. This is only used during the import process.

---


<a id="class-gltfstate-method-get-unique-names"></a>

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_unique_names**() const [🔗](class_gltfstate.md#class-gltfstate-method-get-unique-names)

Returns an array of unique node names. This is used in both the import process and export process.

---


<a id="class-gltfstate-method-set-accessors"></a>

void **set_accessors**(accessors: [Array](class_array.md#class-array)[[GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-accessors)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-set-additional-data"></a>

void **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) [🔗](class_gltfstate.md#class-gltfstate-method-set-additional-data)

Sets additional arbitrary data in this **GLTFState** instance. This can be used to keep per-file state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.

---


<a id="class-gltfstate-method-set-animations"></a>

void **set_animations**(animations: [Array](class_array.md#class-array)[[GLTFAnimation](class_gltfanimation.md#class-gltfanimation)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-animations)

Sets the [GLTFAnimation](class_gltfanimation.md#class-gltfanimation)s in the state. When importing, these will be generated as animations in an [AnimationPlayer](class_animationplayer.md#class-animationplayer) node. When exporting, these will be generated from Godot [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes.

---


<a id="class-gltfstate-method-set-buffer-views"></a>

void **set_buffer_views**(buffer_views: [Array](class_array.md#class-array)[[GLTFBufferView](class_gltfbufferview.md#class-gltfbufferview)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-buffer-views)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-set-cameras"></a>

void **set_cameras**(cameras: [Array](class_array.md#class-array)[[GLTFCamera](class_gltfcamera.md#class-gltfcamera)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-cameras)

Sets the [GLTFCamera](class_gltfcamera.md#class-gltfcamera)s in the state. These are the cameras that the [GLTFNode.camera](class_gltfnode.md#class-gltfnode-property-camera) index refers to.

---


<a id="class-gltfstate-method-set-handle-binary-image"></a>

void **set_handle_binary_image**(method: [int](class_int.md#class-int)) [🔗](class_gltfstate.md#class-gltfstate-method-set-handle-binary-image)

**Deprecated:** Use [handle_binary_image_mode](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode) instead.

Deprecated untyped alias for [handle_binary_image_mode](class_gltfstate.md#class-gltfstate-property-handle-binary-image-mode). When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.

---


<a id="class-gltfstate-method-set-images"></a>

void **set_images**(images: [Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-images)

Sets the images in the state stored as an array of [Texture2D](class_texture2d.md#class-texture2d)s. This can be used during export. These are the images that the [GLTFTexture.src_image](class_gltftexture.md#class-gltftexture-property-src-image) index refers to.

---


<a id="class-gltfstate-method-set-lights"></a>

void **set_lights**(lights: [Array](class_array.md#class-array)[[GLTFLight](class_gltflight.md#class-gltflight)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-lights)

Sets the [GLTFLight](class_gltflight.md#class-gltflight)s in the state. These are the lights that the [GLTFNode.light](class_gltfnode.md#class-gltfnode-property-light) index refers to.

---


<a id="class-gltfstate-method-set-materials"></a>

void **set_materials**(materials: [Array](class_array.md#class-array)[[Material](class_material.md#class-material)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-materials)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-set-meshes"></a>

void **set_meshes**(meshes: [Array](class_array.md#class-array)[[GLTFMesh](class_gltfmesh.md#class-gltfmesh)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-meshes)

Sets the [GLTFMesh](class_gltfmesh.md#class-gltfmesh)es in the state. These are the meshes that the [GLTFNode.mesh](class_gltfnode.md#class-gltfnode-property-mesh) index refers to.

---


<a id="class-gltfstate-method-set-nodes"></a>

void **set_nodes**(nodes: [Array](class_array.md#class-array)[[GLTFNode](class_gltfnode.md#class-gltfnode)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-nodes)

Sets the [GLTFNode](class_gltfnode.md#class-gltfnode)s in the state. These are the nodes that [GLTFNode.children](class_gltfnode.md#class-gltfnode-property-children) and [root_nodes](class_gltfstate.md#class-gltfstate-property-root-nodes) refer to. Some of the nodes set here may not be generated in the Godot scene, or may generate multiple Godot scene nodes.

---


<a id="class-gltfstate-method-set-skeletons"></a>

void **set_skeletons**(skeletons: [Array](class_array.md#class-array)[[GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-skeletons)

Sets the [GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton)s in the state. These are the skeletons that the [GLTFNode.skeleton](class_gltfnode.md#class-gltfnode-property-skeleton) index refers to.

---


<a id="class-gltfstate-method-set-skins"></a>

void **set_skins**(skins: [Array](class_array.md#class-array)[[GLTFSkin](class_gltfskin.md#class-gltfskin)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-skins)

Sets the [GLTFSkin](class_gltfskin.md#class-gltfskin)s in the state. These are the skins that the [GLTFNode.skin](class_gltfnode.md#class-gltfnode-property-skin) index refers to.

---


<a id="class-gltfstate-method-set-texture-samplers"></a>

void **set_texture_samplers**(texture_samplers: [Array](class_array.md#class-array)[[GLTFTextureSampler](class_gltftexturesampler.md#class-gltftexturesampler)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-texture-samplers)

Sets the array of texture samplers that are used by the textures contained in the glTF.

---


<a id="class-gltfstate-method-set-textures"></a>

void **set_textures**(textures: [Array](class_array.md#class-array)[[GLTFTexture](class_gltftexture.md#class-gltftexture)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-textures)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfstate-method-set-unique-animation-names"></a>

void **set_unique_animation_names**(unique_animation_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-unique-animation-names)

Sets the unique animation names in the state. This is only used during the import process.

---


<a id="class-gltfstate-method-set-unique-names"></a>

void **set_unique_names**(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) [🔗](class_gltfstate.md#class-gltfstate-method-set-unique-names)

Sets the unique node names in the state. This is used in both the import process and export process.
