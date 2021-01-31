from libraries.lpygame_src.lispy_functions import *

module = {
    "lpygame:win": lpygame_win, "lpygame:win:run": lpygame_win_run, "lpygame:win:setdebug": lpygame_win_setdebug, "lpygame:win:debug": lpygame_win_debug,

    "lpygame:font": lpygame_font, "lpygame:font:rendersize": lpygame_font_rendersize,

    "lpygame:vec2": lpygame_vec2, "lpygame:vec2:setx": lpygame_vec2_setx, "lpygame:vec2:x": lpygame_vec2_x, "lpygame:vec2:sety": lpygame_vec2_sety, "lpygame:vec2:y": lpygame_vec2_y, 
    "lpygame:vec2:setcoords": lpygame_vec2_setcoords, "lpygame:vec2:coords": lpygame_vec2_coords, "lpygame:vec2:normalized": lpygame_vec2_normalized, "lpygame:vec2:zero": lpygame_vec2_zero, 
    "lpygame:vec2:one": lpygame_vec2_one, 

    "lpygame:color": lpygame_color, "lpygame:color:fromname": lpygame_color_fromname, "lpygame:color:fromhtml": lpygame_color_fromhtml, "lpygame:color:fromcolor": lpygame_color_fromcolor, 
    "lpygame:color:fromrgba": lpygame_color_fromrgba, "lpygame:color:fromrgb": lpygame_color_fromrgb, "lpygame:color:gethtml": lpygame_color_gethtml, 
    "lpygame:color:getrgba": lpygame_color_getrgba, "lpygame:color:getrgb": lpygame_color_getrgb, "lpygame:color:lighter": lpygame_color_lighter, "lpygame:color:darker": lpygame_color_darker
}