from libraries_src.lpygame_src.lispy_functions import *
from libraries_src.lpygame_src.lispy_functions.components import *

module = {
    "lpg:win": lpg_win, "lpg:win:run": lpg_win_run, "lpg:win:setdebug": lpg_win_setdebug, "lpg:win:debug": lpg_win_debug, "lpg:win:setcolor": lpg_win_setcolor, 
    "lpg:win:color": lpg_win_color, "lpg:win:fps": lpg_win_fps, "lpg:win:setfps": lpg_win_setfps, "lpg:win:world": lpg_win_world, "lpg:win:setworld": lpg_win_setworld,


    "lpg:world": lpg_world, "lpg:world:getsystem": lpg_world_getsystem,


    "lpg:es:add": lpg_es_add, "lpg:es:remove": lpg_es_remove, "lpg:es:get": lpg_es_get, "lpg:es:has": lpg_es_has,


    "lpg:entity": lpg_entity, "lpg:entity:add": lpg_entity_add, "lpg:entity:remove": lpg_entity_remove, "lpg:entity:has": lpg_entity_has, "lpg:entity:get": lpg_entity_get,


    "lpg:comp:show": lpg_comp_show, 

    "lpg:comp:text": lpg_comp_text, "lpg:comp:text:text": lpg_comp_text_text, "lpg:comp:text:settext": lpg_comp_text_settext, "lpg:comp:text:font": lpg_comp_text_font, 
    "lpg:comp:text:setfont": lpg_comp_text_setfont, "lpg:comp:text:update": lpg_comp_text_update,

    "lpg:comp:position": lpg_comp_position, "lpg:comp:position:x": lpg_comp_position_x, "lpg:comp:position:y": lpg_comp_position_y, "lpg:comp:position:setx": lpg_comp_position_setx, 
    "lpg:comp:position:sety": lpg_comp_position_sety, "lpg:comp:position:pos": lpg_comp_position_pos, "lpg:comp:position:setpos": lpg_comp_position_setpos,

    "lpg:comp:sprite": lpg_comp_sprite, "lpg:comp:sprite:sprite": lpg_comp_sprite_sprite, "lpg:comp:sprite:setsprite": lpg_comp_sprite_setsprite, "lpg:comp:sprite:size": lpg_comp_sprite_size, 
    "lpg:comp:sprite:setsize": lpg_comp_sprite_setsize, "lpg:comp:sprite:rotation": lpg_comp_sprite_rotation, "lpg:comp:sprite:setrotation": lpg_comp_sprite_setrotation, 
    "lpg:comp:sprite:flipx": lpg_comp_sprite_flipx, "lpg:comp:sprite:setflipx": lpg_comp_sprite_setflipx, "lpg:comp:sprite:flipy": lpg_comp_sprite_flipy, 
    "lpg:comp:sprite:setflipy": lpg_comp_sprite_setflipy, "lpg:comp:sprite:updateimage": lpg_comp_sprite_updateimage,


    "lpg:font": lpg_font, "lpg:font:rendersize": lpg_font_rendersize, "lpg:font:name": lpg_font_name, "lpg:font:setname": lpg_font_setname, "lpg:font:size": lpg_font_size, 
    "lpg:font:setsize": lpg_font_setsize, "lpg:font:bold": lpg_font_bold, "lpg:font:setbold": lpg_font_setbold, "lpg:font:italic": lpg_font_italic, "lpg:font:setitalic": lpg_font_setitalic, 
    "lpg:font:underline": lpg_font_underline, "lpg:font:setunderline": lpg_font_setunderline, "lpg:font:antialias": lpg_font_antialias, "lpg:font:setantialias": lpg_font_setantialias, 
    "lpg:font:color": lpg_font_color, "lpg:font:setcolor": lpg_font_setcolor, "lpg:font:background": lpg_font_background, "lpg:font:setbackground": lpg_font_setbackground,


    "lpg:vec2": lpg_vec2, "lpg:vec2:setx": lpg_vec2_setx, "lpg:vec2:x": lpg_vec2_x, "lpg:vec2:sety": lpg_vec2_sety, "lpg:vec2:y": lpg_vec2_y, "lpg:vec2:setcoords": lpg_vec2_setcoords, 
    "lpg:vec2:coords": lpg_vec2_coords, "lpg:vec2:normalized": lpg_vec2_normalized, "lpg:vec2:zero": lpg_vec2_zero, "lpg:vec2:one": lpg_vec2_one,


    "lpg:color": lpg_color, "lpg:color:fromname": lpg_color_fromname, "lpg:color:fromhtml": lpg_color_fromhtml, "lpg:color:fromcolor": lpg_color_fromcolor, 
    "lpg:color:fromrgba": lpg_color_fromrgba, "lpg:color:fromrgb": lpg_color_fromrgb, "lpg:color:gethtml": lpg_color_gethtml, "lpg:color:getrgba": lpg_color_getrgba, 
    "lpg:color:getrgb": lpg_color_getrgb, "lpg:color:lighter": lpg_color_lighter, "lpg:color:darker": lpg_color_darker
}