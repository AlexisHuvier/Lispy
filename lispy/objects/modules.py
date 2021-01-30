from lispy.objects.modules_def import *

import math
import string


modules = {
    "math": {
        'math:pi': math.pi, 'math:e': math.e, 'math:tau': math.tau, 'math:inf': math.inf, 'math:nan': math.nan, "math:!": math_fact, "math:fib": math_fib, "math:ceil": math_ceil,
        "math:comb": math_comb, "math:abs": math_abs, "math:isfinite": math_isfinite, "math:isinf": math_isinf, "math:isnan": math_isnan, "math:perm": math_perm, "math:trunc": math_trunc,
        "math:exp": math_exp, "math:log": math_log, "math:log10": math_log10, "math:pow": math_pow, "math:sqrt": math_sqrt, "math:acos": math_acos, "math:asin": math_asin, 
        "math:atan": math_atan, "math:atan2": math_atan2, "math:cos": math_cos, "math:sin": math_sin, "math:tan": math_tan, "math:degrees": math_degrees, "math:radians": math_radians
    },
    "rand": {
        "rand:randint": random_randint, "rand:randrange": random_randrange, "rand:choice": random_choice, "rand:random": random_random, "rand:uniform": random_uniform
    },
    "list": {
        "list:create": list_create, "list:join": list_join, "list:first": list_first, "list:last": list_last, "list:get": list_get, "list:len": list_len, "list:reverse": list_reverse,
        "list:in": list_in, "list:replace": list_replace, "list:sort": list_sort, "list:min": list_min, "list:max": list_max, "list:count": list_count, "list:clear": list_clear,
        "list:range": list_range, "list:append": list_append, "list:remove": list_remove, "list:insert": list_insert, "list:sub": list_sub
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
        "str:upper": str_upper, "str:split": str_split
    },
    "file": {
        "file:read": file_read, "file:readlines": file_readlines, "file:write": file_write, "file:append": file_append
    }
}