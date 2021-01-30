import sys

def show_error(type_, message, must_exit):
    print("ERROR :", type_)
    print(message)
    if must_exit:
        sys.exit(1)

def type_good(provided, expected):
    for i in range(len(provided)):
        if expected[i] != "":
            if "|" in expected[i]:
                found = False
                for j in expected[i].split("|"):
                    if provided[i].__class__.__name__ == j:
                        found = True
                        break
                if not found:
                    return False
            else:
                if provided[i].__class__.__name__ != expected[i]:
                    return False
    return True

def lispy_function(name_lispy="", arguments=[]):
    def decorator(func):
        def inner(*args):
            if len(args) == len(arguments) and type_good(args, arguments):
                return func(args)
            else:
                show_error("ArgumentError", f"Function : {name_lispy}\nArguments provided : {args}\nType provided : {[i.__class__.__name__ for i in args]}\nType Expected : {arguments}", True)
        return inner
    return decorator