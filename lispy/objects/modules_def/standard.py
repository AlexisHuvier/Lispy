import operator as op
from lispy.error import lispy_function, show_error
import sys

@lispy_function("input", [""], "Getting user input")
def input_advanced(args):
    return input(str(args[0]))

@lispy_function("print", [""], "Print value")
def print_advanced(args):
    return print(str(args[0]))

@lispy_function("+", ["", ""], "Adding two values")
def add(args):
    return op.add(args[0], args[1])

@lispy_function("-", ["", ""], "Substracting two values")
def sub(args):
    return op.sub(args[0], args[1])

@lispy_function("*", ["", ""], "Multipling two values")
def mul(args):
    return op.mul(args[0], args[1])

@lispy_function("/", ["", ""], "Divising two values")
def div(args):
    return op.truediv(args[0], args[1])

@lispy_function("//", ["", ""], "Getting euclidienne division of two values")
def floordiv(args):
    return op.floordiv(args[0], args[1])

@lispy_function("%", ["", ""], "Getting modulo of two values")
def mod(args):
    return op.mod(args[0], args[1])

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
        