import operator as op
import os
import sys
import importlib


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
                self.update(importlib.import_module(to_import).module)
            except ModuleNotFoundError:
                print("Unkown python file :", to_import)
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
        from lispy.objects.modules_def import input_advanced, print_advanced
        env = Env()
        env.update({
            '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, '//': op.floordiv, '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, '%': op.mod,
            'display': print_advanced, "exit": sys.exit, 'input': input_advanced, "int": int, "float": float, "str": str, "true": True, "false": False
        })
        return env