from lispy.objects.modules_def import *

import math
import string


modules = {
    "math": {
        'math:pi': math.pi, 'math:e': math.e, 'math:tau': math.tau, 'math:inf': math.inf, 'math:nan': math.nan, "math:!": math_fact, "math:fib": math_fib, "math:ceil": math_ceil,
        "math:comb": math_comb, "math:abs": math_abs, "math:isfinite": math_isfinite, "math:isinf": math_isinf, "math:isnan": math_isnan, "math:perm": math_perm, "math:trunc": math_trunc,
        "math:exp": math_exp, "math:log": math_log, "math:log10": math_log10, "math:pow": math_pow, "math:sqrt": math_sqrt, "math:acos": math_acos, "math:asin": math_asin, 
        "math:atan": math_atan, "math:atan2": math_atan2, "math:cos": math_cos, "math:sin": math_sin, "math:tan": math_tan, "math:degrees": math_degrees, "math:radians": math_radians,
        "math:clamp": math_clamp, "math:odd": math_odd, "math:even": math_even, "math:divs": math_divs,
    },
    "rand": {
        "rand:randint": random_randint, "rand:randrange": random_randrange, "rand:choice": random_choice, "rand:random": random_random, "rand:uniform": random_uniform
    },
    "list": {
        "list:join": list_join, "list:first": list_first, "list:last": list_last, "list:get": list_get, "list:len": list_len, "list:reverse": list_reverse,
        "list:in": list_in, "list:replace": list_replace, "list:sort": list_sort, "list:min": list_min, "list:max": list_max, "list:count": list_count, "list:clear": list_clear,
        "list:range": list_range, "list:append": list_append, "list:remove": list_remove, "list:insert": list_insert, "list:sub": list_sub, "list:map": list_map, "list:filter": list_filter,
        "list:zip": list_zip, "list:+": list_sum, "list:set": list_set,
    },
    "stats": {
        "stats:mean": statistics_mean, "stats:median": statistics_median, "stats:mode": statistics_mode, "stats:variance": statistics_variance
    },
    "str": {
        "str:ascii_letters": string.ascii_letters, "str:ascii_lowercase": string.ascii_lowercase, "str:ascii_uppercase": string.ascii_uppercase, "str:digits": string.digits,
        "str:hexdigits": string.hexdigits, "str:octdigits": string.octdigits, "str:punctuation": string.punctuation, "str:printable": string.printable, "str:whitespace": string.whitespace,
        "str:capitalize": str_capitalize, "str:title": str_title, "str:endswith": str_endswith, "str:startswith": str_startswith, "str:isalnum": str_isalnum, 
        "str:isalpha": str_isalpha, "str:isascii": str_isascii, "str:isdecimal": str_isdecimal, "str:isdigit": str_isdigit, "str:isidentifier": str_isidentifier, "str:islower": str_islower, 
        "str:isnumeric": str_isnumeric, "str:isprintable": str_isprintable, "str:isspace": str_isspace, "str:istitle": str_istitle, "str:isupper": str_isupper, "str:lower": str_lower,
        "str:upper": str_upper, "str:split": str_split, "str:reverse": str_reverse, "str:replace": str_replace, "str:sub": str_sub,
    },
    "path": {
        "path:read": path_read, "path:readlines": path_readlines, "path:write": path_write, "path:append": path_append, "path:exists": path_exists, "path:isdir": path_isdir, 
        "path:isfile": path_isfile, "path:remove": path_remove, "path:touch": path_touch, "path:rename": path_rename, "path:listdir": path_listdir, "path:makedirs": path_makedirs
    },
    "turtle": {
        "turtle:forward": turtle_forward, "turtle:back": turtle_back, "turtle:right": turtle_right, "turtle:left": turtle_left, "turtle:setpos": turtle_setpos, 
        "turtle:setx": turtle_setx, "turtle:sety": turtle_sety, "turtle:setangle": turtle_setangle, "turtle:home": turtle_home, "turtle:circle": turtle_circle, 
        "turtle:dot": turtle_dot, "turtle:undo": turtle_undo, "turtle:setspeed": turtle_setspeed, "turtle:speed": turtle_speed, "turtle:pos": turtle_pos, 
        "turtle:towards": turtle_towards, "turtle:x": turtle_x, "turtle:y": turtle_y, "turtle:angle": turtle_angle, "turtle:down": turtle_down, "turtle:up": turtle_up, 
        "turtle:setwidth": turtle_setwidth, "turtle:width": turtle_width, "turtle:isdown": turtle_isdown, "turtle:setpencolor": turtle_setpencolor, "turtle:pencolor": turtle_pencolor, 
        "turtle:setfillcolor": turtle_setfillcolor, "turtle:fillcolor": turtle_fillcolor, "turtle:isfilling": turtle_isfilling, "turtle:beginfill": turtle_beginfill, 
        "turtle:endfill": turtle_endfill, "turtle:reset": turtle_reset, "turtle:clear": turtle_clear, "turtle:hide": turtle_hide, "turtle:show": turtle_show, 
        "turtle:isshowed": turtle_isshowed, "turtle:end": turtle_end
    },
    "sqlite": {
        "sqlite:connect": sqlite_connect, "sqlite:executewithreturn": sqlite_executewithreturn, "sqlite:executewithoutreturn": sqlite_executewithoutreturn, "sqlite:reconnect": sqlite_reconnect, 
        "sqlite:disconnect": sqlite_disconnect
    }, 
    "dict": {
        "dict:get": dict_get, "dict:haskey": dict_haskey, "dict:hasvalue": dict_hasvalue, "dict:set": dict_set, "dict:keys": dict_keys, "dict:items": dict_items, "dict:values": dict_values
    },
    "sys": {
        "sys:version": sys_version, "sys:platform": sys_platform, "sys:pyversion": sys_pyversion
    },
    "os": {
        "os:name": os_name, "os:getpid": os_getpid, "os:terminalsize": os_terminalsize, "os:chdir": os_chdir, "os:getcwd": os_getcwd
    }
}