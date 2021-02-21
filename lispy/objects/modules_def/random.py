import random
from lispy.error import lispy_function

@lispy_function("rand:choice", ["list"], "Return random choice from a list")
def random_choice(args):
    return random.choice(args[0])

@lispy_function("rand:randint", ["int", "int"], "Return random integer value between arg1 and arg2")
def random_randint(args):
    return random.randint(args[0], args[1])

@lispy_function("rand:randrange", ["int", "int", "int"], "Return random integer value from range")
def random_randrange(args):
    return random.randrange(args[0], args[1], args[2])

@lispy_function("rand:random", [], "Return random value between 0 and 1")
def random_random(args):
    return random.random()

@lispy_function("rand:uniform", ["int", "int"], "Return random real value between arg1 and arg2")
def random_uniform(args):
    return random.uniform(args[0], args[1])
