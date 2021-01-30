import math
from lispy.error import lispy_function

@lispy_function("math:fib", ["int"])
def math_fib(args):
    nb = args[0]
    if nb == 0:
        return 0
    if nb == 1:
        return 1
    if nb == 2:
        return 1
    nb1 = 1
    nb2 = 1
    suivant = 0
    for i in range(2, nb):
        suivant = nb1 + nb2
        nb1 = nb2
        nb2 = suivant
    return suivant

@lispy_function("math:ceil", ["float|int"])
def math_ceil(args):
    return math.ceil(args[0])

@lispy_function("math:comb", ["int", "int"])
def math_comb(args):
    return math.comb(args[0], args[1])

@lispy_function("math:abs", ["float|int"])
def math_abs(args):
    return math.fabs(args[0])

@lispy_function("math:!", ["int"])
def math_fact(args):
    return math.factorial(args[0])

@lispy_function("math:isfinite", ["int|float"])
def math_isfinite(args):
    return math.isfinite(args[0])

@lispy_function("math:isinf", ["int|float"])
def math_isinf(args):
    return math.isinf(args[0])

@lispy_function("math:isnan", ["int|float"])
def math_isnan(args):
    return math.isnan(args[0])

@lispy_function("math:perm", ["int", "int"])
def math_perm(args):
    return math.perm(args[0], args[1])

@lispy_function("math:trunc", ["int|float"])
def math_trunc(args):
    return math.trunc(args[0])

@lispy_function("math:exp", ["int|float"])
def math_exp(args):
    return math.exp(args[0])

@lispy_function("math:log", ["int|float", "int|float"])
def math_log(args):
    return math.log(args[0], args[1])

@lispy_function("math:log10", ["int|float"])
def math_log10(args):
    return math.log10(args[0])

@lispy_function("math:pow", ["int", "int"])
def math_pow(args):
    return pow(args[0], args[1])

@lispy_function("math:sqrt", ["int|float"])
def math_sqrt(args):
    return math.sqrt(args[0])

@lispy_function("math:acos", ["int|float"])
def math_acos(args):
    return math.acos(args[0])

@lispy_function("math:asin", ["int|float"])
def math_asin(args):
    return math.asin(args[0])

@lispy_function("math:atan", ["int|float"])
def math_atan(args):
    return math.atan(args[0])

@lispy_function("math:atan2", ["int|float", "int|float"])
def math_atan2(args):
    return math.atan2(args[0], args[1])

@lispy_function("math:cos", ["int|float"])
def math_cos(args):
    return math.cos(args[0])

@lispy_function("math:sin", ["int|float"])
def math_sin(args):
    return math.sin(args[0])
    
@lispy_function("math:tan", ["int|float"])
def math_tan(args):
    return math.tan(args[0])

@lispy_function("math:degrees", ["int|float"])
def math_degrees(args):
    return math.degrees(args[0])

@lispy_function("math:radians", ["int|float"])
def math_radians(args):
    return math.radians(args[0])
