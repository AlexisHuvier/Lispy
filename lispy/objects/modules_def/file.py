import os
import shutil
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

@lispy_function("file:exists", ["str"])
def file_exists(args):
    return os.path.exists(args[0])

@lispy_function("file:isdir", ["str"])
def file_isdir(args):
    return os.path.isdir(args[0])

@lispy_function("file:isfile", ["str"])
def file_isfile(args):
    return os.path.isfile(args[0])

@lispy_function("file:remove", ["str"])
def file_remove(args):
    if os.path.isdir(args):
        shutil.rmtree(args[0])
    else:
        os.remove(ags[0])

@lispy_function("file:touch", ["str"])
def file_touch(args):
    with open(args[0], "w") as f:
        f.write("")

@lispy_function("file:rename", ["str", "str"])
def file_rename(args):
    os.rename(args[0], args[1])

@lispy_function("file:listdir", ["str"])
def file_listdir(args):
    return os.listdir(args[0])