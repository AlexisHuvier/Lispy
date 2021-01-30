import sys

def show_error(type_, message, must_exit):
    print("ERROR :", type_)
    print(message)
    if must_exit:
        sys.exit(1)