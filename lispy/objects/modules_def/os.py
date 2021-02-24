import os
import shutil
from lispy.error import lispy_function


@lispy_function("os:name", [], "Getting OS Name")
def os_name(args):
    return os.name

@lispy_function("os:getpid", [], "Getting processus id")
def os_getpid(args):
    return os.getpid()

@lispy_function("os:terminalsize", [], "Getting size of terminal")
def os_terminalsize(args):
    return (shutil.get_terminal_size().columns, shutil.get_terminal_size().lines)

@lispy_function("os:chdir", ["str"], "Change current warking directory")
def os_chdir(args):
    os.chdir(args[0])

@lispy_function("os:getcwd", [], "Getting current working directory")
def os_getcwd(args):
    return os.getcwd()