import sys
import asyncio

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
                    try:
                        if isinstance(provided[i], globals()[j]):
                            found = True
                            break
                    except KeyError:
                        if provided[i].__class__.__name__ == j:
                            found = True
                            break
                if not found:
                    return False
            else:
                try:
                    print(globals()[expected[i]], isinstance(provided[i], globals()[expected[i]]))
                    if not isinstance(provided[i], globals()[expected[i]]):
                        return False
                        break
                except KeyError:
                    if provided[i].__class__.__name__ != expected[i]:
                        return False
    return True

def lispy_function(name_lispy="", arguments=[], explaination="", must_async=False):
    def decorator(func):
        def inner(*args):
            if (len(arguments) == 1 and arguments[0] == "...") or (len(args) == len(arguments) and type_good(args, arguments)):
                if must_async:
                    if asyncio.get_running_loop() is not None:
                        return asyncio.get_running_loop().create_task(func(args))
                    else:
                        loop = asyncio.get_event_loop()
                        asyncio.set_event_loop(loop)
                        return loop.run_until_complete(func(args))
                else:
                    return func(args)
            else:
                show_error("ArgumentError", f"Function : {name_lispy}\nArguments provided : {args}\nType provided : {[i.__class__.__name__ for i in args]}\nType Expected : {arguments}", True)
        return inner
    return decorator