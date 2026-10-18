extends Node

signal happened

@export var config: Resource
var ready_count: int = 0
var observed_count: int = 0


func _ready() -> void:
	ready_count += 1


func observe() -> void:
	observed_count += 1
