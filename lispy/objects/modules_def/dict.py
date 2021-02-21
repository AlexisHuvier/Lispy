from lispy.error import lispy_function

@lispy_function("dict:get", ["dict", ""], "Getting value from dict")
def dict_get(args):
    return args[0][args[1]]

@lispy_function("dict:haskey", ["dict", ""], "Return if dict has key")
def dict_haskey(args):
    return args[1] in args[0].keys()

@lispy_function("dict:hasvalue", ["dict", ""], "Return if dict has value")
def dict_hasvalue(args):
    return args[1] in args[0].values()

@lispy_function("dict:set", ["dict", "", ""], "Setting value to dict")
def dict_set(args):
    args[0][args[1]] = args[2]

@lispy_function("dict:keys", ["dict"], "Return keys from dict")
def dict_keys(args):
    return list(args[0].keys())

@lispy_function("dict:values", ["dict"], "Return values from dict")
def dict_values(args):
    return list(args[0].values())

@lispy_function("dict:items", ["dict"], "Return items from dict")
def dict_items(args):
    return list(args[0].items())
