> Source: https://docs.godotengine.org/en/4.7/classes/class_placeholdercubemaparray.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="placeholdercubemaparray"></a>

<a id="class-placeholdercubemaparray"></a>

# PlaceholderCubemapArray

**Inherits:** [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class-placeholdertexturelayered) **<** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [CubemapArray](class_cubemaparray.md#class-cubemaparray) without image data.

<a id="description"></a>

## Description

This class replaces a [CubemapArray](class_cubemaparray.md#class-cubemaparray) or a [CubemapArray](class_cubemaparray.md#class-cubemaparray)-derived class in 2 conditions:

- In dedicated server mode, where the image data shouldn't affect game logic. This allows reducing the exported PCK's size significantly.
- When the [CubemapArray](class_cubemaparray.md#class-cubemaparray)-derived class is missing, for example when using a different engine version.

**Note:** This class is not intended for rendering or for use in shaders. Operations like calculating UV are not guaranteed to work.
