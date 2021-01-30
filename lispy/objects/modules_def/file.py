def file_read(*args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = f.read()
    return result

def file_readlines(*args):
    with open(args[0], "r", encoding="utf-8") as f:
        result = [i.replace("\n", "") for i in f.readlines()]
    return result

def file_write(*args):
    with open(args[0], "w", encoding="utf-8") as f:
        f.write(args[1])

def file_append(*args):
    with open(args[0], "a", encoding="utf-8") as f:
        f.write(args[1])
