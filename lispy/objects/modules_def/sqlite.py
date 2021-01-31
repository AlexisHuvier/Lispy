import sqlite3
from lispy.error import lispy_function


class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
    
    def executewithoutreturn(self, query, tuples=None):
        self.cursor = self.connection.cursor()
        if tuples is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tuples)
        self.connection.commit()
    
    def executewithreturn(self, query, tuples=None):
        self.cursor = self.connection.cursor()
        if tuples is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tuples)
        return self.cursor.fetchall()
    
    def reconnect(self, fichier):
        self.connection = sqlite3.connect(fichier)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()


@lispy_function("sqlite:connect", ["str"])
def sqlite_connect(args):
    return Database(args[0])

@lispy_function("sqlite:executewithreturn", ["Database", "str", "list|NoneType"])
def sqlite_executewithreturn(args):
    if args[2] is not None and len(args[2]):
        return args[0].executewithreturn(args[1], args[2])
    return args[0].executewithreturn(args[1])

@lispy_function("sqlite:executewithoutreturn", ["Database", "str", "list|NoneType"])
def sqlite_executewithoutreturn(args):
    if args[2] is not None and len(args[2]):
        return args[0].executewithoutreturn(args[1], args[2])
    return args[0].executewithoutreturn(args[1])

@lispy_function("sqlite:reconnect", ["Database", "str"])
def sqlite_reconnect(args):
    args[0].reconnect(args[1])

@lispy_function("sqlite:disconnect", ["Database"])
def sqlite_disconnect(args):
    args[0].disconnect()
