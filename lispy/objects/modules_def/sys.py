import sys
from lispy.error import lispy_function


@lispy_function("sys:version", [], "Getting Lispy version")
def sys_version(args):
    return "1.0.0"

@lispy_function("sys:platform", [], "Getting platform")
def sys_platform(args):
    return sys.platform

@lispy_function("sys:pyversion", [], "Getting Python version")
def sys_pyversion(args):
    return sys.version