from lispy.objects.modules_def import *

import random
import math
import operator as op
import string


modules = {
    "math": {
        "math:pow": pow, "math:abs": abs, "math:sin": math.sin, "math:cos": math.cos, "math:tan": math.tan, "math:log": math.log, "math:log10": math.log10, "math:asin": math.asin, 
        "math:acos": math.acos, "math:atan": math.atan, "math:atan2": math.atan2, "math:dist": math.dist, "math:sqrt": math.sqrt, "math:exp": math.exp, 
        "math:degrees": math.degrees, "math:radiants": math.radians, "math:floor": math.floor, "math:ceil": math.ceil, 'math:pi': math.pi, 'math:e': math.e, 
        'math:tau': math.tau, 'math:inf': math.inf, 'math:nan': math.nan, "math:!": math.factorial, "math:fib": fib
    },
    "rand": {
        "rand:randint": random.randint, "rand:randrange": random.randrange, "rand:choice": choice_advanced, "rand:random": random.random, "rand:uniform": random.uniform
    },
    "list": {
        "list:create": list_create, "list:join": list_join, "list:first": list_first, "list:last": list_last, "list:get": list_get, "list:len": list_len, "list:reverse": list_reverse,
        "list:in": list_in, "list:replace": list_replace, "list:sort": list_sort, "list:min": list_min, "list:max": list_max, "list:count": list_count, "list:clear": list_clear,
        "list:range": list_range, "list:append": list_append, "list:remove": list_remove, "list:insert": list_insert
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