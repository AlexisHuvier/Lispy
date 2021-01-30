from lispy.env import Env
from lispy.parser import Parser
from lispy.objects import Procedure
from lispy.error import show_error

import os
import sys


class Lispy:
    @classmethod
    def lispy_eval_with_parsing(cls, exp, env=Env.standart()):
        return cls.lispy_eval(Parser.parse(exp), env)

    @classmethod
    def get_total_env(cls, env):
        temp = env
        temp.update({
            'if': "built-in function", 'while': "built-in function", 'for': "built-in function", 'def': "built-in function", 'set': "built-in function", 'del': "built-in function",
            'import': "built-in function", 'func': "built-in function", 'ret': "built-in function"
        })
        return temp

    @classmethod
    def lispy_eval(cls, exp, env=Env.standart()):
        if isinstance(exp, str):
            if len(exp) and exp[0] == '"':
                return exp[1:-1]
            else:
                try:
                    return env[exp] 
                except KeyError:
                    show_error("UnknownExpression", f"Expression : {exp}\nEnvironment : {cls.get_total_env(env)}", True)
        elif isinstance(exp, (int, float)):
            return exp
        elif len(exp) == 0:
            return None
        elif all(isinstance(x, list) for x in exp):
            for i in exp:
                if isinstance(i, list) and i[0] == "ret":
                    return cls.lispy_eval(i, env)
                cls.lispy_eval(i, env)
            return None
        op, *args = exp
        if op == 'if':
            test, conseq, alt = args
            exp = (conseq if cls.lispy_eval(test, env) else alt)
            return cls.lispy_eval(exp, env)
        elif op == 'while':
            test, conseq = args
            while cls.lispy_eval(test, env):
                cls.lispy_eval(conseq, env)
            return None
        elif op == "for":
            var, range_, conseq = args
            result = cls.lispy_eval(range_, env)
            for i in result:
                env[var] = i
                cls.lispy_eval(conseq, env)
            return None
        elif op == 'def':
            symbol, exp = args
            env[symbol] = cls.lispy_eval(exp, env)
        elif op == 'set':
            symbol, exp = args
            env[symbol] = cls.lispy_eval(exp, env)
        elif op == 'del':
            del env[args[0]]
        elif op == 'func':
            (parms, body) = args
            return Procedure(parms, body, env)
        elif op == "import":
            env.import_(args[0])
        elif op == "ret":
            return cls.lispy_eval(args[0], env)
        else:
            proc = cls.lispy_eval(op, env)
            vals = [cls.lispy_eval(arg, env) for arg in args]
            try:
                return proc(*vals)
            except Exception as e:
                show_error(e.__class__.__name__, f"Error : {str(e).capitalize()}\nProc : {op} ( {proc} )\nValues : {args} ( {vals} )", True)
                