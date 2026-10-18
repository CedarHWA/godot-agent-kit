> Source: https://docs.godotengine.org/en/4.7/classes/class_tilesetatlassource.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="tilesetatlassource"></a>

<a id="class-tilesetatlassource"></a>

# TileSetAtlasSource

**Inherits:** [TileSetSource](class_tilesetsource.md#class-tilesetsource) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Exposes a 2D atlas texture as a set of tiles for a [TileSet](class_tileset.md#class-tileset) resource.

<a id="description"></a>

## Description

An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed using [create_tile()](class_tilesetatlassource.md#class-tilesetatlassource-method-create-tile). Those tiles are then indexed using their coordinates in the grid.

Each tile can also have a size in the grid coordinates, making it more or less cells in the atlas.

Alternatives version of a tile can be created using [create_alternative_tile()](class_tilesetatlassource.md#class-tilesetatlassource-method-create-alternative-tile), which are then indexed using an alternative ID. The main tile (the one in the grid), is accessed with an alternative ID equal to 0.

Each tile alternate has a set of properties that is defined by the source's [TileSet](class_tileset.md#class-tileset) layers. Those properties are stored in a TileData object that can be accessed and modified using [get_tile_data()](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-data).

As TileData properties are stored directly in the TileSetAtlasSource resource, their properties might also be set using `TileSetAtlasSource.set("<coords_x>:<coords_y>/<alternative_id>/<tile_data_property>")`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2i](class_vector2i.md#class-vector2i) | [margins](class_tilesetatlassource.md#class-tilesetatlassource-property-margins) | `Vector2i(0, 0)` |
| [Vector2i](class_vector2i.md#class-vector2i) | [separation](class_tilesetatlassource.md#class-tilesetatlassource-property-separation) | `Vector2i(0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_tilesetatlassource.md#class-tilesetatlassource-property-texture) |  |
| [Vector2i](class_vector2i.md#class-vector2i) | [texture_region_size](class_tilesetatlassource.md#class-tilesetatlassource-property-texture-region-size) | `Vector2i(16, 16)` |
| [bool](class_bool.md#class-bool) | [use_texture_padding](class_tilesetatlassource.md#class-tilesetatlassource-property-use-texture-padding) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_tiles_outside_texture](class_tilesetatlassource.md#class-tilesetatlassource-method-clear-tiles-outside-texture)() |
| [int](class_int.md#class-int) | [create_alternative_tile](class_tilesetatlassource.md#class-tilesetatlassource-method-create-alternative-tile)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_id_override: [int](class_int.md#class-int) = -1) |
| void | [create_tile](class_tilesetatlassource.md#class-tilesetatlassource-method-create-tile)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(1, 1)) |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_atlas_grid_size](class_tilesetatlassource.md#class-tilesetatlassource-method-get-atlas-grid-size)() const |
| [int](class_int.md#class-int) | [get_next_alternative_tile_id](class_tilesetatlassource.md#class-tilesetatlassource-method-get-next-alternative-tile-id)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_runtime_texture](class_tilesetatlassource.md#class-tilesetatlassource-method-get-runtime-texture)() const |
| [Rect2i](class_rect2i.md#class-rect2i) | [get_runtime_tile_texture_region](class_tilesetatlassource.md#class-tilesetatlassource-method-get-runtime-tile-texture-region)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_tile_animation_columns](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-columns)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [float](class_float.md#class-float) | [get_tile_animation_frame_duration](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-frame-duration)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_tile_animation_frames_count](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-frames-count)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) | [get_tile_animation_mode](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-mode)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_tile_animation_separation](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-separation)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [float](class_float.md#class-float) | [get_tile_animation_speed](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-speed)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [float](class_float.md#class-float) | [get_tile_animation_total_duration](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-total-duration)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_tile_at_coords](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-at-coords)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [TileData](class_tiledata.md#class-tiledata) | [get_tile_data](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-data)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_tile_size_in_atlas](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-size-in-atlas)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Rect2i](class_rect2i.md#class-rect2i) | [get_tile_texture_region](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-texture-region)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int) = 0) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_tiles_to_be_removed_on_change](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tiles-to-be-removed-on-change)(texture: [Texture2D](class_texture2d.md#class-texture2d), margins: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i), texture_region_size: [Vector2i](class_vector2i.md#class-vector2i)) |
| [bool](class_bool.md#class-bool) | [has_room_for_tile](class_tilesetatlassource.md#class-tilesetatlassource-method-has-room-for-tile)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i), animation_columns: [int](class_int.md#class-int), animation_separation: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int), ignored_tile: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1)) const |
| [bool](class_bool.md#class-bool) | [has_tiles_outside_texture](class_tilesetatlassource.md#class-tilesetatlassource-method-has-tiles-outside-texture)() const |
| void | [move_tile_in_atlas](class_tilesetatlassource.md#class-tilesetatlassource-method-move-tile-in-atlas)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), new_atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), new_size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1)) |
| void | [remove_alternative_tile](class_tilesetatlassource.md#class-tilesetatlassource-method-remove-alternative-tile)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int)) |
| void | [remove_tile](class_tilesetatlassource.md#class-tilesetatlassource-method-remove-tile)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [set_alternative_tile_id](class_tilesetatlassource.md#class-tilesetatlassource-method-set-alternative-tile-id)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int), new_id: [int](class_int.md#class-int)) |
| void | [set_tile_animation_columns](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-columns)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_columns: [int](class_int.md#class-int)) |
| void | [set_tile_animation_frame_duration](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-frame-duration)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int), duration: [float](class_float.md#class-float)) |
| void | [set_tile_animation_frames_count](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-frames-count)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int)) |
| void | [set_tile_animation_mode](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-mode)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), mode: [TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode)) |
| void | [set_tile_animation_separation](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-separation)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [set_tile_animation_speed](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-speed)(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), speed: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-tilesetatlassource-tileanimationmode"></a>

enum **TileAnimationMode**: [🔗](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode)

<a id="class-tilesetatlassource-constant-tile-animation-mode-default"></a>

[TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) **TILE_ANIMATION_MODE_DEFAULT** = `0`

Tile animations start at same time, looking identical.

<a id="class-tilesetatlassource-constant-tile-animation-mode-random-start-times"></a>

[TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) **TILE_ANIMATION_MODE_RANDOM_START_TIMES** = `1`

Tile animations start at random times, looking varied.

<a id="class-tilesetatlassource-constant-tile-animation-mode-max"></a>

[TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) **TILE_ANIMATION_MODE_MAX** = `2`

Represents the size of the [TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) enum.

---


<a id="constants"></a>

## Constants

<a id="class-tilesetatlassource-constant-transform-flip-h"></a>

**TRANSFORM_FLIP_H** = `4096` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-constant-transform-flip-h)

Represents cell's horizontal flip flag. Should be used directly with [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer) to flip placed tiles by altering their alternative IDs.

```gdscript
var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
    # If tile is not already flipped, flip it.
    $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)
```

**Note:** These transformations can be combined to do the equivalent of 0, 90, 180, and 270 degree rotations, as shown below:

```gdscript
enum TileTransform {
    ROTATE_0 = 0,
    ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
    ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
    ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
}
```

<a id="class-tilesetatlassource-constant-transform-flip-v"></a>

**TRANSFORM_FLIP_V** = `8192` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-constant-transform-flip-v)

Represents cell's vertical flip flag. See [TRANSFORM_FLIP_H](class_tilesetatlassource.md#class-tilesetatlassource-constant-transform-flip-h) for usage.

<a id="class-tilesetatlassource-constant-transform-transpose"></a>

**TRANSFORM_TRANSPOSE** = `16384` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-constant-transform-transpose)

Represents cell's transposed flag. See [TRANSFORM_FLIP_H](class_tilesetatlassource.md#class-tilesetatlassource-constant-transform-flip-h) for usage.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-tilesetatlassource-property-margins"></a>

[Vector2i](class_vector2i.md#class-vector2i) **margins** = `Vector2i(0, 0)` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-property-margins)

- void **set_margins**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_margins**()

Margins, in pixels, to offset the origin of the grid in the texture.

---


<a id="class-tilesetatlassource-property-separation"></a>

[Vector2i](class_vector2i.md#class-vector2i) **separation** = `Vector2i(0, 0)` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-property-separation)

- void **set_separation**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_separation**()

Separation, in pixels, between each tile texture region of the grid.

---


<a id="class-tilesetatlassource-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_tilesetatlassource.md#class-tilesetatlassource-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The atlas texture.

---


<a id="class-tilesetatlassource-property-texture-region-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **texture_region_size** = `Vector2i(16, 16)` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-property-texture-region-size)

- void **set_texture_region_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_texture_region_size**()

The base tile size in the texture (in pixel). This size must be bigger than or equal to the TileSet's `tile_size` value.

---


<a id="class-tilesetatlassource-property-use-texture-padding"></a>

[bool](class_bool.md#class-bool) **use_texture_padding** = `true` [🔗](class_tilesetatlassource.md#class-tilesetatlassource-property-use-texture-padding)

- void **set_use_texture_padding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_texture_padding**()

If `true`, generates an internal texture with an additional one pixel padding around each tile. Texture padding avoids a common artifact where lines appear between tiles.

Disabling this setting might lead a small performance improvement, as generating the internal texture requires both memory and processing time when the TileSetAtlasSource resource is modified.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-tilesetatlassource-method-clear-tiles-outside-texture"></a>

void **clear_tiles_outside_texture**() [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-clear-tiles-outside-texture)

Removes all tiles that don't fit the available texture area. This method iterates over all the source's tiles, so it's advised to use [has_tiles_outside_texture()](class_tilesetatlassource.md#class-tilesetatlassource-method-has-tiles-outside-texture) beforehand.

---


<a id="class-tilesetatlassource-method-create-alternative-tile"></a>

[int](class_int.md#class-int) **create_alternative_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_id_override: [int](class_int.md#class-int) = -1) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-create-alternative-tile)

Creates an alternative tile for the tile at coordinates `atlas_coords`. If `alternative_id_override` is -1, give it an automatically generated unique ID, or assigns it the given ID otherwise.

Returns the new alternative identifier, or -1 if the alternative could not be created with a provided `alternative_id_override`.

---


<a id="class-tilesetatlassource-method-create-tile"></a>

void **create_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(1, 1)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-create-tile)

Creates a new tile at coordinates `atlas_coords` with the given `size`.

---


<a id="class-tilesetatlassource-method-get-atlas-grid-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_atlas_grid_size**() const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-atlas-grid-size)

Returns the atlas grid size, which depends on how many tiles can fit in the texture. It thus depends on the [texture](class_tilesetatlassource.md#class-tilesetatlassource-property-texture)'s size, the atlas [margins](class_tilesetatlassource.md#class-tilesetatlassource-property-margins), and the tiles' [texture_region_size](class_tilesetatlassource.md#class-tilesetatlassource-property-texture-region-size).

---


<a id="class-tilesetatlassource-method-get-next-alternative-tile-id"></a>

[int](class_int.md#class-int) **get_next_alternative_tile_id**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-next-alternative-tile-id)

Returns the alternative ID a following call to [create_alternative_tile()](class_tilesetatlassource.md#class-tilesetatlassource-method-create-alternative-tile) would return.

---


<a id="class-tilesetatlassource-method-get-runtime-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_runtime_texture**() const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-runtime-texture)

If [use_texture_padding](class_tilesetatlassource.md#class-tilesetatlassource-property-use-texture-padding) is `false`, returns [texture](class_tilesetatlassource.md#class-tilesetatlassource-property-texture). Otherwise, returns an internal [ImageTexture](class_imagetexture.md#class-imagetexture) created that includes the padding.

---


<a id="class-tilesetatlassource-method-get-runtime-tile-texture-region"></a>

[Rect2i](class_rect2i.md#class-rect2i) **get_runtime_tile_texture_region**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-runtime-tile-texture-region)

Returns the region of the tile at coordinates `atlas_coords` for the given `frame` inside the texture returned by [get_runtime_texture()](class_tilesetatlassource.md#class-tilesetatlassource-method-get-runtime-texture).

**Note:** If [use_texture_padding](class_tilesetatlassource.md#class-tilesetatlassource-property-use-texture-padding) is `false`, returns the same as [get_tile_texture_region()](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-texture-region).

---


<a id="class-tilesetatlassource-method-get-tile-animation-columns"></a>

[int](class_int.md#class-int) **get_tile_animation_columns**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-columns)

Returns how many columns the tile at `atlas_coords` has in its animation layout.

---


<a id="class-tilesetatlassource-method-get-tile-animation-frame-duration"></a>

[float](class_float.md#class-float) **get_tile_animation_frame_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-frame-duration)

Returns the animation frame duration of frame `frame_index` for the tile at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-get-tile-animation-frames-count"></a>

[int](class_int.md#class-int) **get_tile_animation_frames_count**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-frames-count)

Returns how many animation frames has the tile at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-get-tile-animation-mode"></a>

[TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode) **get_tile_animation_mode**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-mode)

Returns the tile animation mode of the tile at `atlas_coords`. See also [set_tile_animation_mode()](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-mode).

---


<a id="class-tilesetatlassource-method-get-tile-animation-separation"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_animation_separation**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-separation)

Returns the separation (as in the atlas grid) between each frame of an animated tile at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-get-tile-animation-speed"></a>

[float](class_float.md#class-float) **get_tile_animation_speed**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-speed)

Returns the animation speed of the tile at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-get-tile-animation-total-duration"></a>

[float](class_float.md#class-float) **get_tile_animation_total_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-total-duration)

Returns the sum of the sum of the frame durations of the tile at coordinates `atlas_coords`. This value needs to be divided by the animation speed to get the actual animation loop duration.

---


<a id="class-tilesetatlassource-method-get-tile-at-coords"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_at_coords**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-at-coords)

If there is a tile covering the `atlas_coords` coordinates, returns the top-left coordinates of the tile (thus its coordinate ID). Returns `Vector2i(-1, -1)` otherwise.

---


<a id="class-tilesetatlassource-method-get-tile-data"></a>

[TileData](class_tiledata.md#class-tiledata) **get_tile_data**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-data)

Returns the [TileData](class_tiledata.md#class-tiledata) object for the given atlas coordinates and alternative ID.

---


<a id="class-tilesetatlassource-method-get-tile-size-in-atlas"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_size_in_atlas**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-size-in-atlas)

Returns the size of the tile (in the grid coordinates system) at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-get-tile-texture-region"></a>

[Rect2i](class_rect2i.md#class-rect2i) **get_tile_texture_region**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int) = 0) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-texture-region)

Returns a tile's texture region in the atlas texture. For animated tiles, a `frame` argument might be provided for the different frames of the animation.

---


<a id="class-tilesetatlassource-method-get-tiles-to-be-removed-on-change"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_tiles_to_be_removed_on_change**(texture: [Texture2D](class_texture2d.md#class-texture2d), margins: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i), texture_region_size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tiles-to-be-removed-on-change)

Returns an array of tiles coordinates ID that will be automatically removed when modifying one or several of those properties: `texture`, `margins`, `separation` or `texture_region_size`. This can be used to undo changes that would have caused tiles data loss.

---


<a id="class-tilesetatlassource-method-has-room-for-tile"></a>

[bool](class_bool.md#class-bool) **has_room_for_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i), animation_columns: [int](class_int.md#class-int), animation_separation: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int), ignored_tile: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1)) const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-has-room-for-tile)

Returns whether there is enough room in an atlas to create/modify a tile with the given properties. If `ignored_tile` is provided, act as is the given tile was not present in the atlas. This may be used when you want to modify a tile's properties.

---


<a id="class-tilesetatlassource-method-has-tiles-outside-texture"></a>

[bool](class_bool.md#class-bool) **has_tiles_outside_texture**() const [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-has-tiles-outside-texture)

Checks if the source has any tiles that don't fit the texture area (either partially or completely).

---


<a id="class-tilesetatlassource-method-move-tile-in-atlas"></a>

void **move_tile_in_atlas**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), new_atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), new_size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-move-tile-in-atlas)

Move the tile and its alternatives at the `atlas_coords` coordinates to the `new_atlas_coords` coordinates with the `new_size` size. This functions will fail if a tile is already present in the given area.

If `new_atlas_coords` is `Vector2i(-1, -1)`, keeps the tile's coordinates. If `new_size` is `Vector2i(-1, -1)`, keeps the tile's size.

To avoid an error, first check if a move is possible using [has_room_for_tile()](class_tilesetatlassource.md#class-tilesetatlassource-method-has-room-for-tile).

---


<a id="class-tilesetatlassource-method-remove-alternative-tile"></a>

void **remove_alternative_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-remove-alternative-tile)

Remove a tile's alternative with alternative ID `alternative_tile`.

Calling this function with `alternative_tile` equals to 0 will fail, as the base tile alternative cannot be removed.

---


<a id="class-tilesetatlassource-method-remove-tile"></a>

void **remove_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-remove-tile)

Remove a tile and its alternative at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-set-alternative-tile-id"></a>

void **set_alternative_tile_id**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int), new_id: [int](class_int.md#class-int)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-alternative-tile-id)

Change a tile's alternative ID from `alternative_tile` to `new_id`.

Calling this function with `new_id` of 0 will fail, as the base tile alternative cannot be moved.

---


<a id="class-tilesetatlassource-method-set-tile-animation-columns"></a>

void **set_tile_animation_columns**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_columns: [int](class_int.md#class-int)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-columns)

Sets the number of columns in the animation layout of the tile at coordinates `atlas_coords`. If set to 0, then the different frames of the animation are laid out as a single horizontal line in the atlas.

---


<a id="class-tilesetatlassource-method-set-tile-animation-frame-duration"></a>

void **set_tile_animation_frame_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int), duration: [float](class_float.md#class-float)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-frame-duration)

Sets the animation frame `duration` of frame `frame_index` for the tile at coordinates `atlas_coords`.

---


<a id="class-tilesetatlassource-method-set-tile-animation-frames-count"></a>

void **set_tile_animation_frames_count**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-frames-count)

Sets how many animation frames the tile at coordinates `atlas_coords` has.

---


<a id="class-tilesetatlassource-method-set-tile-animation-mode"></a>

void **set_tile_animation_mode**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), mode: [TileAnimationMode](class_tilesetatlassource.md#enum-tilesetatlassource-tileanimationmode)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-mode)

Sets the tile animation mode of the tile at `atlas_coords` to `mode`. See also [get_tile_animation_mode()](class_tilesetatlassource.md#class-tilesetatlassource-method-get-tile-animation-mode).

---


<a id="class-tilesetatlassource-method-set-tile-animation-separation"></a>

void **set_tile_animation_separation**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-separation)

Sets the margin (in grid tiles) between each tile in the animation layout of the tile at coordinates `atlas_coords` has.

---


<a id="class-tilesetatlassource-method-set-tile-animation-speed"></a>

void **set_tile_animation_speed**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), speed: [float](class_float.md#class-float)) [🔗](class_tilesetatlassource.md#class-tilesetatlassource-method-set-tile-animation-speed)

Sets the animation speed of the tile at coordinates `atlas_coords` has.
