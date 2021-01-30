class Procedure:
    def __init__(self, parms, body, env):
        self.parms = parms
        self.body = body
        self.env = env
    
    def __call__(self, *args):
        from lispy.lispy import Lispy
        self.env.update(zip(self.parms, args))
        return Lispy.lispy_eval(self.body, self.env)