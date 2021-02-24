import os
import shutil
from lispy.error import lispy_function

@lispy_function("path:read", ["str"], "Return content of file")
def path_read(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = f.read()
    return result

@lispy_function("path:readlines", ["str"], "Return lines of file")
def path_readlines(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = [i.replace("\n", "") for i in f.readlines()]
    return result

@lispy_function("path:write", ["str", "str"], "Write content to file")
def path_write(args):
    with open(args[0], "w", encoding="utf-8") as f:
        f.write(args[1])

@lispy_function("path:append", ["str", "str"], "Append content to file")
def path_append(args):
    with open(args[0], "a", encoding="utf-8") as f:
        f.write(args[1])

@lispy_function("path:exists", ["str"], "Return if path exists")
def path_exists(args):
    return os.path.exists(args[0])

@lispy_function("path:isdir", ["str"], "Return if path is directory")
def path_isdir(args):
    return os.path.isdir(args[0])

@lispy_function("path:isfile", ["str"], "Return if path is file")
def path_isfile(args):
    return os.path.isfile(args[0])

@lispy_function("path:remove", ["str"], "Remove path")
def path_remove(args):
    if os.path.isdir(args):
        shutil.rmtree(args[0])
    else:
        os.remove(ags[0])

@lispy_function("path:touch", ["str"], "Create empty file")
def path_touch(args):
    with open(args[0], "w") as f:
        f.write("")

@lispy_function("path:rename", ["str", "str"], "Rename file")
def path_rename(args):
    os.rename(args[0], args[1])

@lispy_function("path:listdir", ["str"], "List files from directory")
def path_listdir(args):
    return os.listdir(args[0])

@lispy_function("path:makedirs", ["str"], "Create directory")
def path_makedirs(args):
    os.makedirs(args[0])