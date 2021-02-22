import math
from lispy.error import lispy_function

@lispy_function("math:fib", ["int"], "Return fibonacci")
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

@lispy_function("math:clamp", ["int|float", "int|float", "int|float"], "Clamp value between two values")
def math_clamp(args):
    if args[0] < args[1]:
        return args[1]
    elif args[0] > args[2]:
        return args[2]
    return args[0]

@lispy_function("math:ceil", ["float|int"], "Return upper integer of value")
def math_ceil(args):
    return math.ceil(args[0])

@lispy_function("math:comb", ["int", "int"], "Return the number of ways to choose arg1 items from arg2 items without repetition and without order")
def math_comb(args):
    return math.comb(args[0], args[1])

@lispy_function("math:abs", ["float|int"], "Return absolute value")
def math_abs(args):
    return math.fabs(args[0])

@lispy_function("math:!", ["int"], "Return factorial value")
def math_fact(args):
    return math.factorial(args[0])

@lispy_function("math:isfinite", ["int|float"], "Return if value is finite")
def math_isfinite(args):
    return math.isfinite(args[0])

@lispy_function("math:isinf", ["int|float"], "Return if value is infinite")
def math_isinf(args):
    return math.isinf(args[0])

@lispy_function("math:isnan", ["int|float"], "Return if value is not a number")
def math_isnan(args):
    return math.isnan(args[0])

@lispy_function("math:perm", ["int", "int"], "Return the number of ways to choose arg1 items from arg2 items without repetition and with order.")
def math_perm(args):
    return math.perm(args[0], args[1])

@lispy_function("math:trunc", ["int|float"], "Return truncated value")
def math_trunc(args):
    return math.trunc(args[0])

@lispy_function("math:exp", ["int|float"], "Return exponential value")
def math_exp(args):
    return math.exp(args[0])

@lispy_function("math:log", ["int|float", "int|float"], "Return log value")
def math_log(args):
    return math.log(args[0], args[1])

@lispy_function("math:log10", ["int|float"], "Return log10 value")
def math_log10(args):
    return math.log10(args[0])

@lispy_function("math:pow", ["int", "int"], "Return arg1 power by arg2")
def math_pow(args):
    return pow(args[0], args[1])

@lispy_function("math:sqrt", ["int|float"], "Return sqrt value")
def math_sqrt(args):
    return math.sqrt(args[0])

@lispy_function("math:acos", ["int|float"], "Return acos value")
def math_acos(args):
    return math.acos(args[0])

@lispy_function("math:asin", ["int|float"], "Return asin value")
def math_asin(args):
    return math.asin(args[0])

@lispy_function("math:atan", ["int|float"], "Return atan value")
def math_atan(args):
    return math.atan(args[0])

@lispy_function("math:atan2", ["int|float", "int|float"], "Return atan2 value")
def math_atan2(args):
    return math.atan2(args[0], args[1])

@lispy_function("math:cos", ["int|float"], "Return cos value")
def math_cos(args):
    return math.cos(args[0])

@lispy_function("math:sin", ["int|float"], "Return sin value")
def math_sin(args):
    return math.sin(args[0])
    
@lispy_function("math:tan", ["int|float"], "Return tan value")
def math_tan(args):
    return math.tan(args[0])

@lispy_function("math:degrees", ["int|float"], "Return degrees value")
def math_degrees(args):
    return math.degrees(args[0])

@lispy_function("math:radians", ["int|float"], "Return radians value")
def math_radians(args):
    return math.radians(args[0])

@lispy_function("math:odd", ["int|float"], "Return if value is odd")
def math_odd(args):
    return args[0] % 2 == 1

@lispy_function("math:even", ["int|float"], "Return if value is even")
def math_even(args):
    return args[0] % 2 == 0

@lispy_function("math:divs", ["int|float"], "Return divisors of value")
def math_divs(args):
    divs = []
    for i in range(1, int(math.sqrt(args[0]) + 1)):
        if args[0] % i == 0:
            divs.append(i)
            if i*i != args[0]:
                divs.append(int(args[0] / i))
    divs.sort()
    return divs
