from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:sprite", ["str"])
def lpg_comp_sprite(args):
    return SpriteComponent(args[0])

@lispy_function("lpg:comp:sprite:sprite", ["SpriteComponent"])
def lpg_comp_sprite_sprite(args):
    return args[0].sprite

@lispy_function("lpg:comp:sprite:setsprite", ["SpriteComponent", "str"])
def lpg_comp_sprite_setsprite(args):
    args[0].sprite = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:size", ["SpriteComponent"])
def lpg_comp_sprite_size(args):
    return args[0].size

@lispy_function("lpg:comp:sprite:setsize", ["SpriteComponent", "Vec2"])
def lpg_comp_sprite_setsize(args):
    args[0].size = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:rotation", ["SpriteComponent"])
def lpg_comp_sprite_rotation(args):
    return args[0].rotation

@lispy_function("lpg:comp:sprite:setrotation", ["SpriteComponent", "int"])
def lpg_comp_sprite_setrotation(args):
    args[0].rotation = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:flipx", ["SpriteComponent"])
def lpg_comp_sprite_flipx(args):
    return args[0].flipx

@lispy_function("lpg:comp:sprite:setflipx", ["SpriteComponent", "bool"])
def lpg_comp_sprite_setflipx(args):
    args[0].flipx = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:flipy", ["SpriteComponent"])
def lpg_comp_sprite_flipy(args):
    return args[0].flipy

@lispy_function("lpg:comp:sprite:setflipy", ["SpriteComponent", "bool"])
def lpg_comp_sprite_setflipy(args):
    args[0].flipy = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:updateimage", ["SpriteComponent"])
def lpg_comp_sprite_updateimage(args):
    args[0].update_image()