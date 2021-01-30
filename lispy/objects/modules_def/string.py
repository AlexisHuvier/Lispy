from lispy.error import lispy_function

@lispy_function(name_lispy="str:capitalize", arguments=["str"])
def str_capitalize(args):
    return args[0].capitalize()

@lispy_function(name_lispy="str:title", arguments=["str"])
def str_title(args):
    return args[0].title()

@lispy_function(name_lispy="str:title", arguments=["str", "str"])
def str_endswith(args):
    return args[0].endswith(args[1])

@lispy_function(name_lispy="str:startswith", arguments=["str", "str"])
def str_startswith(args):
    return args[0].startswith(args[1])

@lispy_function(name_lispy="str:isalnum", arguments=["str"])
def str_isalnum(args):
    return args[0].isalnum()

@lispy_function(name_lispy="str:isalpha", arguments=["str"])
def str_isalpha(args):
    return args[0].isalpha()

@lispy_function(name_lispy="str:isascii", arguments=["str"])
def str_isascii(args):
    return args[0].isascii()

@lispy_function(name_lispy="str:isdecimal", arguments=["str"])
def str_isdecimal(args):
    return args[0].isdecimal()

@lispy_function(name_lispy="str:isdigit", arguments=["str"])
def str_isdigit(args):
    return args[0].isdigit()

@lispy_function(name_lispy="str:isidentifier", arguments=["str"])
def str_isidentifier(args):
    return args[0].isidentifier()

@lispy_function(name_lispy="str:islower", arguments=["str"])
def str_islower(args):
    return args[0].islower()

@lispy_function(name_lispy="str:isnumeric", arguments=["str"])
def str_isnumeric(args):
    return args[0].isnumeric()

@lispy_function(name_lispy="str:isprintable", arguments=["str"])
def str_isprintable(args):
    return args[0].isprintable()

@lispy_function(name_lispy="str:isspace", arguments=["str"])
def str_isspace(args):
    return args[0].isspace()

@lispy_function(name_lispy="str:istitle", arguments=["str"])
def str_istitle(args):
    return args[0].istitle()

@lispy_function("str:isupper", ["str"])
def str_isupper(args):
    return args[0].isupper()

@lispy_function("str:lower", ["str"])
def str_lower(args):
    return args[0].lower()

@lispy_function("str:upper", ["str"])
def str_upper(args):
    return args[0].upper()

@lispy_function("str:split", ["str", "str"])
def str_split(args):
    return args[0].split(args[1])
