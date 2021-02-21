from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:sprite:create", ["str"], "CreatingSpriteComponent")
def lpg_comp_sprite(args):
    return SpriteComponent(args[0])

@lispy_function("lpg:comp:sprite:sprite", ["SpriteComponent"], "Getting sprite from SpriteComponent")
def lpg_comp_sprite_sprite(args):
    return args[0].sprite

@lispy_function("lpg:comp:sprite:setsprite", ["SpriteComponent", "str"], "Setting sprite to SpriteComponent")
def lpg_comp_sprite_setsprite(args):
    args[0].sprite = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:size", ["SpriteComponent"], "Getting size from SpriteComponent")
def lpg_comp_sprite_size(args):
    return args[0].size

@lispy_function("lpg:comp:sprite:setsize", ["SpriteComponent", "Vec2"], "Setting size to SpriteComponent")
def lpg_comp_sprite_setsize(args):
    args[0].size = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:rotation", ["SpriteComponent"], "Getting rotation from SpriteComponent")
def lpg_comp_sprite_rotation(args):
    return args[0].rotation

@lispy_function("lpg:comp:sprite:setrotation", ["SpriteComponent", "int"], "Setting rotation to SpriteComponent")
def lpg_comp_sprite_setrotation(args):
    args[0].rotation = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:flipx", ["SpriteComponent"], "Return if sprite is flipx from SpriteComponent")
def lpg_comp_sprite_flipx(args):
    return args[0].flipx

@lispy_function("lpg:comp:sprite:setflipx", ["SpriteComponent", "bool"], "Setting if sprite is flipx to SpriteComponent")
def lpg_comp_sprite_setflipx(args):
    args[0].flipx = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:flipy", ["SpriteComponent"], "Return if sprite is flipy from SpriteComponent")
def lpg_comp_sprite_flipy(args):
    return args[0].flipy

@lispy_function("lpg:comp:sprite:setflipy", ["SpriteComponent", "bool"], "Setting if sprite is flipy to SpriteComponent")
def lpg_comp_sprite_setflipy(args):
    args[0].flipy = args[1]
    args[0].update_image()

@lispy_function("lpg:comp:sprite:updateimage", ["SpriteComponent"], "Update Image of SpriteComponent")
def lpg_comp_sprite_updateimage(args):
    args[0].update_image()