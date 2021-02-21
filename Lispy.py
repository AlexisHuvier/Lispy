from lispy import Lispy
import sys
import os
import time


def to_scheme_readable(exp):
    if isinstance(exp, list):
        return "("+", ".join(map(to_scheme_readable, exp)) + ")"
    else:
        return str(exp)

if __name__ == "__main__":
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[-1] == "--debug"):
        if sys.argv[-1] == "--debug":
            Lispy.debug = True

        prompt = 'lispy> '

        while True:
            try:
                val = Lispy.lispy_eval_with_parsing(input(prompt))
                if val is not None:
                    print(to_scheme_readable(val))
            except SystemExit:
                pass
    else:
        if sys.argv[-1] == "--debug":
            Lispy.debug = True

        if os.path.exists(sys.argv[1]) and sys.argv[1].endswith(".lpy"):
            with open(sys.argv[1], 'r', encoding="utf-8") as f:
                Lispy.lispy_eval_with_parsing(f.read())