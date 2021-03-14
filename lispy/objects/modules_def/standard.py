import operator as op
from lispy.error import lispy_function, show_error
import sys

@lispy_function("input", ["..."], "Getting user input with a prompt")
def input_advanced(args):
    return input(" ".join(map(str, args)))

@lispy_function("print", ["..."], "Print values")
def print_advanced(args):
    return print(" ".join(map(str, args)))

@lispy_function("+", ["..."], "Adding values")
def add(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r += i
    return r

@lispy_function("-", ["..."], "Substracting values")
def sub(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r -= i
    return r

@lispy_function("*", ["..."], "Multipling values")
def mul(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r *= i
    return r

@lispy_function("/", ["..."], "Dividing values")
def div(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r /= i
    return r

@lispy_function("//", ["..."], "Getting euclidienne division of values")
def floordiv(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r = r // i
    return r

@lispy_function("%", ["..."], "Getting modulo of values")
def mod(args):
    r = None
    for i in args:
        if r is None:
            r = i
        else:
            r %= i
    return r

@lispy_function(">", ["", ""], "Return if value is greater than other value")
def gt(args):
    return op.gt(args[0], args[1])

@lispy_function("<", ["", ""], "Return if value is less than other value")
def lt(args):
    return op.lt(args[0], args[1])

@lispy_function(">=", ["", ""], "Return if value is greater or equal than other value")
def ge(args):
    return op.ge(args[0], args[1])

@lispy_function("<=", ["", ""], "Return if value is less or equal than other value")
def le(args):
    return op.le(args[0], args[1])

@lispy_function("=", ["", ""], "Return if value is equal than other value")
def eq(args):
    return op.eq(args[0], args[1])

@lispy_function("exit", ["int"], "Exit application with exit code")
def exit(args):
    sys.exit(args[0])

@lispy_function("int", [""], "Convert value to int")
def int_(args):
    return int(args[0])

@lispy_function("float", [""], "Convert value to float")
def float_(args):
    return float(args[0])

@lispy_function("str", [""], "Convert value to string")
def str_(args):
    return str(args[0])

@lispy_function("list", ["..."], "Create list by values")
def list_(args):
    return list(args)

@lispy_function("dict", ["list", "list"], "Create dict from two list")
def dict_(args):
    return {i: v for i, v in zip(args[0], args[1])}

@lispy_function("not", [""], "Invert value")
def not_(args):
    return not args[0]

@lispy_function("type", [""], "Return type of value")
def type_(args):
    return args[0].__class__.__name__

@lispy_function("assert", [""], "Assert if cond is true")
def assert_(args):
    if not bool(args[0]):
        show_error("AssertError", "Test : "+str(args[0]), True)
        