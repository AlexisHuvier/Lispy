from lispy.error import lispy_function

@lispy_function("file:read", ["str"])
def file_read(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = f.read()
    return result

@lispy_function("file:readlines", ["str"])
def file_readlines(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = [i.replace("\n", "") for i in f.readlines()]
    return result

@lispy_function("file:write", ["str", "str"])
def file_write(args):
    with open(args[0], "w", encoding="utf-8") as f:
        f.write(args[1])

@lispy_function("file:append", ["str", "str"])
def file_append(args):
    with open(args[0], "a", encoding="utf-8") as f:
        f.write(args[1])
