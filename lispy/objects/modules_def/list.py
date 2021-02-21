from lispy.error import lispy_function

@lispy_function("list:join", ["list", "str"], "Join list with a separator")
def list_join(args):
    if len(args) == 1:
        return " ".join(map(str, args[0]))
    else:
        return args[1].join(map(str, args[0]))

@lispy_function("list:first", ["list"], "Return first element of list")
def list_first(args):
    return args[0][0]

@lispy_function("list:last", ["list"], "Create last element of list")
def list_last(args):
    return args[0][-1]

@lispy_function("list:range", ["int", "int", "int"], "Create list from range")
def list_range(args):
    to = args[1]
    from_ = args[0]
    pas = args[2]
    return list(range(from_, to, pas))

@lispy_function("list:get", ["list", "int"], "Getting element from list")
def list_get(args):
    return args[0][args[1]]

@lispy_function("list:sub", ["list", "int", "int"], "Getting sublist from list")
def list_sub(args):
    return args[0][args[1]:args[2]]

@lispy_function("list:len", ["list"], "Return length of list")
def list_len(args):
    return len(args[0])

@lispy_function("list:in", ["", "list"], "Return if element in list")
def list_in(args):
    return args[0] in args[1]

@lispy_function("list:append", ["list", ""], "Append element in list")
def list_append(args):
    args[0].append(args[1])

@lispy_function("list:remove", ["list", ""], "Remove element in list")
def list_remove(args):
    args[0].remove(args[1])

@lispy_function("list:insert", ["list", "int", ""], "Insert element at index in list")
def list_insert(args):
    args[0].insert(args[1], args[2])

@lispy_function("list:replace", ["list", "", ""], "Replace element in list")
def list_replace(args):
    return [args[2] if x == args[1] else x for x in args[0]]

@lispy_function("list:sort", ["list", "bool"], "Sort list with a boolean for reverse sort")
def list_sort(args):
    args[0].sort(reverse=args[1])
    return args[0]

@lispy_function("list:reverse", ["list"], "Reverse list")
def list_reverse(args):
    return args[0].reverse()

@lispy_function("list:clear", ["list"], "Clear list")
def list_clear(args):
    return args[0].clear()

@lispy_function("list:min", ["list"], "Return minimum of list")
def list_min(args):
    return min(args[0])

@lispy_function("list:max", ["list"], "Return maximum of list")
def list_max(args):
    return max(args[0])

@lispy_function("list:count", ["list", ""], "Return count of element in list")
def list_count(args):
    return args[0].count(args[1])

@lispy_function("list:map", ["", "list"], "Apply function to elements of list")
def list_map(args):
    return list(map(args[0], args[1]))

@lispy_function("list:filter", ["", "list"], "Apply filter to elements of list")
def list_filter(args):
    return list(filter(args[0], args[1]))

@lispy_function("list:zip", ["list", "list"], "Zip lists together")
def list_zip(args):
    return list(zip(args[0], args[1]))