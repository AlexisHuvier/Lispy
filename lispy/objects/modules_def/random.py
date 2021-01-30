import random
from lispy.error import lispy_function

@lispy_function("rand:choice", ["list"])
def random_choice(args):
    return random.choice(args[0])

@lispy_function("rand:randint", ["int", "int"])
def random_randint(args):
    return random.randint(args[0], args[1])

@lispy_function("rand:randrange", ["int", "int", "int"])
def random_randrange(args):
    return random.randrange(args[0], args[1], args[2])

@lispy_function("rand:random")
def random_random(args):
    return random.random()

@lispy_function("rand:uniform", ["int", "int"])
def random_uniform(args):
    return random.uniform(args[0], args[1])
