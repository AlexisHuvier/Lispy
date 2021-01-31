import pygame
import pygame.locals as pgconst
import os
from libraries.lpygame_src.utils import Font, Color

pygame.init()


class Window:
    def __init__(self, title, size, color):

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
    
    def stop(self):
        """
            Stop Window
        """
        self.is_running = False
    
    def run(self):
        """
            Launch Window
        """
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill(self.color.get_rgba())

            if self.debug:
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