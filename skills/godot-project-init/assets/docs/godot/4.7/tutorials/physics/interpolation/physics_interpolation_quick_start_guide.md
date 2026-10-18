> Source: https://docs.godotengine.org/en/4.7/tutorials/physics/interpolation/physics_interpolation_quick_start_guide.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="quick-start-guide"></a>

<a id="doc-physics-interpolation-quick-start-guide"></a>

# Quick start guide

- Turn on physics interpolation: [Project Settings > Physics > Common > Physics Interpolation](../../../classes/class_projectsettings.md#class-projectsettings-property-physics-common-physics-interpolation)
- Make sure you move objects and run your game logic in `_physics_process()`
  rather than `_process()`. This includes moving objects directly *and
  indirectly* (by e.g. moving a parent, or using another mechanism to automatically
  move nodes).
- Be sure to call [Node.reset_physics_interpolation](../../../classes/class_node.md#class-node-method-reset-physics-interpolation)
  on nodes *after* you first position or teleport them, to prevent "streaking".
- Temporarily try setting [Project Settings > Physics > Common > Physics Ticks per Second](../../../classes/class_projectsettings.md#class-projectsettings-property-physics-common-physics-ticks-per-second)
  to 10 to see the difference with and without interpolation.
