from libraries.lpygame_src.systems import *


class World:
    def __init__(self, window):
        self.window = window
        self.systems = {
            "entity": EntitySystem(self)
        }
    
    def update(self):
        pass

    def show(self):
        pass

    def show_debug(self):
        pass

    def keypress(self, evt):
        pass

    def mousepress(self, evt):
        pass

    def keyup(self, evt):
        pass

    def mousemotion(self, evt):
        pass

    def event(self, evt):
        pass

    def get_system(self, classe):
        if classe in self.systems.keys():
            return self.systems[classe]