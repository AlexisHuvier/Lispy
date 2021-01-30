import operator as op
from lispy.error import lispy_function
import sys


def input_advanced(*args):
    return input(" ".join(map(str, args)))

def print_advanced(*args):
    return print(" ".join(map(str, args)))

@lispy_function("+", ["", ""])
def add(args):
    return op.add(args[0], args[1])

@lispy_function("-", ["", ""])
def sub(args):
    return op.sub(args[0], args[1])

@lispy_function("*", ["", ""])
def mul(args):
    return op.mul(args[0], args[1])

@lispy_function("/", ["", ""])
def div(args):
    return op.div(args[0], args[1])

@lispy_function("//", ["", ""])
def floordiv(args):
    return op.floordiv(args[0], args[1])

@lispy_function("%", ["", ""])
def mod(args):
    return op.mod(args[0], args[1])

@lispy_function(">", ["", ""])
def gt(args):
    return op.gt(args[0], args[1])

@lispy_function("<", ["", ""])
def lt(args):
    return op.lt(args[0], args[1])

@lispy_function(">=", ["", ""])
def ge(args):
    return op.ge(args[0], args[1])

@lispy_function("<=", ["", ""])
def le(args):
    return op.le(args[0], args[1])

@lispy_function("%", ["", ""])
def eq(args):
    return op.eq(args[0], args[1])

@lispy_function("exit", ["int"])
def exit(args):
    sys.exit(args[0])

@lispy_function("int", [""])
def int_(args):
    return int(args[0])

@lispy_function("float", [""])
def float_(args):
    return float(args[0])

@lispy_function("str", [""])
def str_(args):
    return str(args[0])

def list_(*args):
    return list(args)