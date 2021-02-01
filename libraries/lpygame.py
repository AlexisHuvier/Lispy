from libraries.lpygame_src.lispy_functions import *
from libraries.lpygame_src.lispy_functions.components import *

module = {
    "lpygame:win": lpygame_win, "lpygame:win:run": lpygame_win_run, "lpygame:win:setdebug": lpygame_win_setdebug, "lpygame:win:debug": lpygame_win_debug, "lpygame:win:fps": lpygame_win_fps, 
    "lpygame:win:setfps": lpygame_win_setfps, "lpygame:win:world": lpygame_win_world, "lpygame:win:setworld": lpygame_win_setworld, "lpygame:win:color": lpygame_win_color,
    "lpygame:win:setcolor": lpygame_win_setcolor,

    "lpygame:world": lpygame_world, "lpygame:world:getsystem": lpygame_world_getsystem,

    "lpygame:entitysystem:addentity": lpygame_entitysystem_addentity, "lpygame:entitysystem:removeentity": lpygame_entitysystem_removeentity, 
    "lpygame:entitysystem:getentity": lpygame_entitysystem_getentity, "lpygame:entitysystem:hasentity": lpygame_entitysystem_hasentity,

    "lpygame:entity": lpygame_entity, "lpygame:entity:addcomponent": lpygame_entity_addcomponent, "lpygame:entity:removecomponent": lpygame_entity_removecomponent, 
    "lpygame:entity:hascomponent": lpygame_entity_hascomponent, "lpygame:entity:getcomponent": lpygame_entity_getcomponent,

    "lpygame:components:show": lpygame_components_show, 
    "lpygame:components:text": lpygame_components_text, "lpygame:components:text:text": lpygame_components_text_text, "lpygame:components:text:settext": lpygame_components_text_settext, 
    "lpygame:components:text:font": lpygame_components_text_font, "lpygame:components:text:setfont": lpygame_components_text_setfont, 
    "lpygame:components:text:updaterender": lpygame_components_text_updaterender,
    "lpygame:components:position": lpygame_components_position, "lpygame:components:position:x": lpygame_components_position_x, "lpygame:components:position:y": lpygame_components_position_y, 
    "lpygame:components:position:setx": lpygame_components_position_setx, "lpygame:components:position:sety": lpygame_components_position_sety, 
    "lpygame:components:position:pos": lpygame_components_position_pos, "lpygame:components:position:setpos": lpygame_components_position_setpos, 

    "lpygame:font": lpygame_font, "lpygame:font:rendersize": lpygame_font_rendersize, "lpygame:font:name": lpygame_font_name, "lpygame:font:setname": lpygame_font_setname, 
    "lpygame:font:size": lpygame_font_size, "lpygame:font:setsize": lpygame_font_setsize, "lpygame:font:bold": lpygame_font_bold, "lpygame:font:setbold": lpygame_font_setbold, 
    "lpygame:font:italic": lpygame_font_italic, "lpygame:font:setitalic": lpygame_font_setitalic, "lpygame:font:underline": lpygame_font_underline, 
    "lpygame:font:setunderline": lpygame_font_setunderline, "lpygame:font:antialias": lpygame_font_antialias, "lpygame:font:setantialias": lpygame_font_setantialias, 
    "lpygame:font:color": lpygame_font_color, "lpygame:font:setcolor": lpygame_font_setcolor, "lpygame:font:background": lpygame_font_background, 
    "lpygame:font:setbackground": lpygame_font_setbackground,

    "lpygame:vec2": lpygame_vec2, "lpygame:vec2:setx": lpygame_vec2_setx, "lpygame:vec2:x": lpygame_vec2_x, "lpygame:vec2:sety": lpygame_vec2_sety, "lpygame:vec2:y": lpygame_vec2_y, 
    "lpygame:vec2:setcoords": lpygame_vec2_setcoords, "lpygame:vec2:coords": lpygame_vec2_coords, "lpygame:vec2:normalized": lpygame_vec2_normalized, "lpygame:vec2:zero": lpygame_vec2_zero, 
    "lpygame:vec2:one": lpygame_vec2_one, 

    "lpygame:color": lpygame_color, "lpygame:color:fromname": lpygame_color_fromname, "lpygame:color:fromhtml": lpygame_color_fromhtml, "lpygame:color:fromcolor": lpygame_color_fromcolor, 
    "lpygame:color:fromrgba": lpygame_color_fromrgba, "lpygame:color:fromrgb": lpygame_color_fromrgb, "lpygame:color:gethtml": lpygame_color_gethtml, 
    "lpygame:color:getrgba": lpygame_color_getrgba, "lpygame:color:getrgb": lpygame_color_getrgb, "lpygame:color:lighter": lpygame_color_lighter, "lpygame:color:darker": lpygame_color_darker
}