from lispy.error import lispy_function

@lispy_function("str:capitalize", ["str"], "Capitalize string")
def str_capitalize(args):
    return args[0].capitalize()

@lispy_function("str:title", ["str"], "Return title string")
def str_title(args):
    return args[0].title()

@lispy_function("str:endswith", ["str", "str"], "Return if string endswith other string")
def str_endswith(args):
    return args[0].endswith(args[1])

@lispy_function("str:startswith", ["str", "str"], "Return if string startswith other string")
def str_startswith(args):
    return args[0].startswith(args[1])

@lispy_function("str:isalnum", ["str"], "Return if string is alphanumeric")
def str_isalnum(args):
    return args[0].isalnum()

@lispy_function("str:isalpha", ["str"], "Return if string is alphabetic")
def str_isalpha(args):
    return args[0].isalpha()

@lispy_function("str:isascii", ["str"], "Return if string is ascii")
def str_isascii(args):
    return args[0].isascii()

@lispy_function("str:isdecimal", ["str"], "Return if string is decimal")
def str_isdecimal(args):
    return args[0].isdecimal()

@lispy_function("str:isdigit", ["str"], "Return if string is digit")
def str_isdigit(args):
    return args[0].isdigit()

@lispy_function("str:isidentifier", ["str"], "Return if string is identifier")
def str_isidentifier(args):
    return args[0].isidentifier()

@lispy_function("str:islower", ["str"], "Return if string is lower")
def str_islower(args):
    return args[0].islower()

@lispy_function("str:isnumeric", ["str"], "Return if string is numeric")
def str_isnumeric(args):
    return args[0].isnumeric()

@lispy_function("str:isprintable", ["str"], "Return if string is printable")
def str_isprintable(args):
    return args[0].isprintable()

@lispy_function("str:isspace", ["str"], "Return if string is space")
def str_isspace(args):
    return args[0].isspace()

@lispy_function("str:istitle", ["str"], "Return if string is title")
def str_istitle(args):
    return args[0].istitle()

@lispy_function("str:isupper", ["str"], "Return if string is upper")
def str_isupper(args):
    return args[0].isupper()

@lispy_function("str:lower", ["str"], "Return lower string")
def str_lower(args):
    return args[0].lower()

@lispy_function("str:upper", ["str"], "Return upper string")
def str_upper(args):
    return args[0].upper()

@lispy_function("str:split", ["str", "str"], "Return splitted string by other string")
def str_split(args):
    return args[0].split(args[1])

@lispy_function("str:reverse", ["str"], "Return reversed string")
def str_reverse(args):
    args[0].reverse()

@lispy_function("str:sub", ["str", "int", "int"], "Return substring with start index and en index")
def str_sub(args):
    return args[0][args[1]:args[2]]

@lispy_function("str:replace", ["str", "str", "str"], "Replace part of a string by a another string")
def str_replace(args):
    return args[0].replace(args[1], args[2])
