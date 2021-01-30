def list_create(*args):
    return list(args)

def list_join(*args):
    if len(args) == 1:
        return " ".join(map(str, args[0]))
    else:
        return args[1].join(map(str, args[0]))

def list_first(*args):
    return args[0][0]

def list_last(*args):
    return args[0][-1]

def list_range(*args):
    pas = 1
    from_ = 0
    if len(args) == 1:
        to = args[0]
    elif len(args) == 2:
        to = args[1]
        from_ = args[0]
    elif len(args) == 3:
        to = args[1]
        from_ = args[0]
        pas = args[2]
    return list(range(from_, to, pas))

def list_get(*args):
    if len(args) == 4:
        return args[0][args[1]:args[2]:args[3]]
    elif len(args) == 3:
        return args[0][args[1]:args[2]]
    else:
        return args[0][args[1]]

def list_len(*args):
    return len(args[0])

def list_in(*args):
    return args[0] in args[1]

def list_replace(*args):
    if isinstance(args[0], str):
        return args[0].replace(args[1], args[2])
    else:
        return [args[2] if x == args[1] else x for x in args[0]]

def list_sort(*args):
    if len(args) == 2:
        args[0].sort(reverse=args[1])
    else:
        args[0].sort()
    return args[0]

def list_reverse(*args):
    return args[0].reverse()

def list_clear(*args):
    return args[0].clear()

def list_min(*args):
    return min(args[0])

def list_max(*args):
    return max(args[0])

def list_count(*args):
    return args[0].count(args[1])