import os
import importlib
from lispy.objects.modules_def.standard import *
from lispy.error import show_error


class Env(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        if outer is not None:
            self.update(outer)

    def import_(self, to_import):
        from lispy.objects.modules import modules
        if to_import.split(":")[0] == "python":
            to_import = to_import.split(":")[1]
            try:
                self.update(importlib.import_module("libraries."+to_import).module)
            except ModuleNotFoundError as e:
                show_error("ModuleError", str(e), True)
        elif to_import in modules.keys():
            self.update(modules[to_import])
        else:
            to_import = to_import.replace(".", os.path.sep)
            if os.path.exists(to_import+".lpy"):
                with open(to_import+'.lpy', 'r', encoding="utf-8") as f:
                    from lispy.lispy import Lispy
                    Lispy.lispy_eval_with_parsing(f.read(), self)
            else:
                print("Unknown file or module :", to_import)

    def __str__(self):
        return str({k: v if str(type(v)) != "<class 'function'>" else "function" for k, v in self.items()})


    @classmethod
    def standart(cls):
        env = Env()
        env.update({
            '+':add, '-':sub, '*':mul, '/':div, '//': floordiv, '>':gt, '<':lt, '>=':ge, '<=':le, '=':eq, '%': mod, '!': not_, 'none': None, "dict": dict_, "assert": assert_,
            'display': print_advanced, "exit": exit, 'input': input_advanced, "int": int_, "float": float_, "str": str_, "list": list_, "true": True, "false": False, "type": type_
        })
        return env