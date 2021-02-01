from lispy.error import lispy_function

@lispy_function("list:join", ["list", "str"])
def list_join(args):
    if len(args) == 1:
        return " ".join(map(str, args[0]))
    else:
        return args[1].join(map(str, args[0]))

@lispy_function("list:first", ["list"])
def list_first(args):
    return args[0][0]

@lispy_function("list:list", ["list"])
def list_last(args):
    return args[0][-1]

@lispy_function("list:range", ["int", "int", "int"])
def list_range(args):
    to = args[1]
    from_ = args[0]
    pas = args[2]
    return list(range(from_, to, pas))

@lispy_function("list:get", ["list", "int"])
def list_get(args):
    return args[0][args[1]]

@lispy_function("list:sub", ["list", "int", "int"])
def list_sub(args):
    return args[0][args[1]:args[2]]

@lispy_function("list:len", ["list"])
def list_len(args):
    return len(args[0])

@lispy_function("list:in", ["", "list"])
def list_in(args):
    return args[0] in args[1]

@lispy_function("list:append", ["list", ""])
def list_append(args):
    args[0].append(args[1])

@lispy_function("list:remove", ["list", ""])
def list_remove(args):
    args[0].remove(args[1])

@lispy_function("list:insert", ["list", "int", ""])
def list_insert(args):
    args[0].insert(args[1], args[2])

@lispy_function("list:replace", ["list", "", ""])
def list_replace(args):
    return [args[2] if x == args[1] else x for x in args[0]]

@lispy_function("list:sort", ["list", "bool"])
def list_sort(args):
    args[0].sort(reverse=args[1])
    return args[0]

@lispy_function("list:reverse", ["list"])
def list_reverse(args):
    return args[0].reverse()

@lispy_function("list:clear", ["list"])
def list_clear(args):
    return args[0].clear()

@lispy_function("list:min", ["list"])
def list_min(args):
    return min(args[0])

@lispy_function("list:max", ["list"])
def list_max(args):
    return max(args[0])

@lispy_function("list:count", ["list", ""])
def list_count(args):
    return args[0].count(args[1])

@lispy_function("list:map", ["", "list"])
def list_map(args):
    return list(map(args[0], args[1]))

@lispy_function("list:filter", ["", "list"])
def list_filter(args):
    return list(filter(args[0], args[1]))

@lispy_function("list:zip", ["list", "list"])
def list_zip(args):
    return list(zip(args[0], args[1]))