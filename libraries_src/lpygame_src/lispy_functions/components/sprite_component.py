from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpygame:components:sprite", ["str"])
def lpygame_components_sprite(args):
    return SpriteComponent(args[0])

@lispy_function("lpygame:components:sprite:sprite", ["SpriteComponent"])
def lpygame_components_sprite_sprite(args):
    return args[0].sprite

@lispy_function("lpygame:components:sprite:setsprite", ["SpriteComponent", "str"])
def lpygame_components_sprite_setsprite(args):
    args[0].sprite = args[1]
    args[0].update_image()

@lispy_function("lpygame:components:sprite:size", ["SpriteComponent"])
def lpygame_components_sprite_size(args):
    return args[0].size

@lispy_function("lpygame:components:sprite:setsize", ["SpriteComponent", "Vec2"])
def lpygame_components_sprite_setsize(args):
    args[0].size = args[1]
    args[0].update_image()

@lispy_function("lpygame:components:sprite:rotation", ["SpriteComponent"])
def lpygame_components_sprite_rotation(args):
    return args[0].rotation

@lispy_function("lpygame:components:sprite:setrotation", ["SpriteComponent", "int"])
def lpygame_components_sprite_setrotation(args):
    args[0].rotation = args[1]
    args[0].update_image()

@lispy_function("lpygame:components:sprite:flipx", ["SpriteComponent"])
def lpygame_components_sprite_flipx(args):
    return args[0].flipx

@lispy_function("lpygame:components:sprite:setflipx", ["SpriteComponent", "bool"])
def lpygame_components_sprite_setflipx(args):
    args[0].flipx = args[1]
    args[0].update_image()

@lispy_function("lpygame:components:sprite:flipy", ["SpriteComponent"])
def lpygame_components_sprite_flipy(args):
    return args[0].flipy

@lispy_function("lpygame:components:sprite:setflipy", ["SpriteComponent", "bool"])
def lpygame_components_sprite_setflipy(args):
    args[0].flipy = args[1]
    args[0].update_image()

@lispy_function("lpygame:components:sprite:updateimage", ["SpriteComponent"])
def lpygame_components_sprite_updateimage(args):
    args[0].update_image()