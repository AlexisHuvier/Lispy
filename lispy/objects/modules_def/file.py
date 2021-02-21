import os
import shutil
from lispy.error import lispy_function

@lispy_function("file:read", ["str"], "Return content of file")
def file_read(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = f.read()
    return result

@lispy_function("file:readlines", ["str"], "Return lines of file")
def file_readlines(args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = [i.replace("\n", "") for i in f.readlines()]
    return result

@lispy_function("file:write", ["str", "str"], "Write content to file")
def file_write(args):
    with open(args[0], "w", encoding="utf-8") as f:
        f.write(args[1])

@lispy_function("file:append", ["str", "str"], "Append content to file")
def file_append(args):
    with open(args[0], "a", encoding="utf-8") as f:
        f.write(args[1])

@lispy_function("file:exists", ["str"], "Return if path exists")
def file_exists(args):
    return os.path.exists(args[0])

@lispy_function("file:isdir", ["str"], "Return if path is directory")
def file_isdir(args):
    return os.path.isdir(args[0])

@lispy_function("file:isfile", ["str"], "Return if path is file")
def file_isfile(args):
    return os.path.isfile(args[0])

@lispy_function("file:remove", ["str"], "Remove path")
def file_remove(args):
    if os.path.isdir(args):
        shutil.rmtree(args[0])
    else:
        os.remove(ags[0])

@lispy_function("file:touch", ["str"], "Create empty file")
def file_touch(args):
    with open(args[0], "w") as f:
        f.write("")

@lispy_function("file:rename", ["str", "str"], "Rename file")
def file_rename(args):
    os.rename(args[0], args[1])

@lispy_function("file:listdir", ["str"], "List files from directory")
def file_listdir(args):
    return os.listdir(args[0])