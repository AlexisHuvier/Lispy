def input_advanced(args):
    if isinstance(args, list):
        return input(" ".join(map(str, args)))
    else:
        return input(args)


def print_advanced(args):
    if isinstance(args, list):
        return print(" ".join(map(str, args)))
    else:
        return print(args)