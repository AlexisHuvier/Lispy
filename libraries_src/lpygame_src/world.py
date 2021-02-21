from libraries_src.lpygame_src.systems import *


class World:
    def __init__(self, window):
        self.window = window
        self.systems = {
            "entity": EntitySystem(self)
        }
    
    def update(self):
        self.systems["entity"].update()

    def show(self):
        self.systems["entity"].show()

    def show_debug(self):
        self.systems["entity"].show_debug()

    def keypress(self, evt):
        self.systems["entity"].keypress(evt)

    def mousepress(self, evt):
        self.systems["entity"].mousepress(evt)

    def keyup(self, evt):
        self.systems["entity"].keyup(evt)

    def mousemotion(self, evt):
        self.systems["entity"].mousemotion(evt)

    def event(self, evt):
        self.systems["entity"].event(evt)

    def get_system(self, classe):
        if classe in self.systems.keys():
            return self.systems[classe]