import pygame
import pygame.locals as pgconst
import os
from libraries.lpygame_src.utils import Font, Color
from libraries.lpygame_src.world import World

pygame.init()


class Window:
    def __init__(self, title, size, color=Color.from_name("BLACK")):

        self.fps = 60
        self.debug = False
        self.color = color
        self.size = size

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size.coords())

        self.clock = pygame.time.Clock()
        self.is_running = False
        self.debug_font = Font("arial", 15, True, False, False, Color.from_name("ORANGE"), None, False)
        self.world = World(self)
    
    def stop(self):
        self.is_running = False
    
    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)

            self.world.update()
            self.screen.fill(self.color.get_rgba())

            self.world.show()

            if self.debug:
                self.world.show_debug()
                try:
                    fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())))
                except OverflowError:
                    fps_label = self.debug_font.render("FPS : Infinity")
                self.screen.blit(fps_label, (10, 10))
            
            self.clock.tick(self.fps)
            pygame.display.update()
        pygame.quit()
                
    def process_event(self, evt):
        if evt.type == pgconst.QUIT:
            self.stop()
        elif evt.type == pgconst.KEYDOWN:
            self.world.keypress(evt)
        elif evt.type == pgconst.MOUSEBUTTONDOWN:
            self.world.mousepress(evt)
        elif evt.type == pgconst.KEYUP:
            self.world.keyup(evt)
        elif evt.type == pgconst.MOUSEMOTION:
            self.world.mousemotion(evt)
        else:
            self.world.event(evt)