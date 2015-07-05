import pygame
import math
from pygame.locals import *
import board as playBoard

TILESIZE = 100
black = 0, 0, 0

colors = [(255,220,81),(125,42,234 ),(12,184,109),
          (31,32,114),(216,5,37),(66,110,20),
          (105,64,125),(78,124,96 ),(114,120,216),
          (109,203,245),(7,18,59)]
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = TILESIZE*4, TILESIZE*4
        self.board = playBoard.Board()

    def on_init(self):
        pygame.init()
        self.myfont = pygame.font.Font(None,30)
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.board.start()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type is pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.board.moveUp()
            if event.key == pygame.K_LEFT:
                self.board.moveLeft()
            if event.key == pygame.K_RIGHT:
                self.board.moveRight()
            if event.key == pygame.K_DOWN:
                self.board.moveDown()

    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.fill(black)
        for x in range(self.board.sizeX):
            for y in range(self.board.sizeY):
                tile = self.board.tiles[x][y]
                if tile is None:
                    pygame.draw.rect(self._display_surf, (50,50,50),(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE))
                else:
                    txt = "%d" % tile.value
                    label = self.myfont.render(txt, 1, (255,255,255))
                    pygame.draw.rect(self._display_surf, colors[int(math.log(tile.value,2)-1)],(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE))
                    self._display_surf.blit(label, (TILESIZE*x+TILESIZE/2, TILESIZE*y+TILESIZE/2))

        if not self.board.running:
            pygame.draw.rect(self._display_surf, (50,50,50),(TILESIZE-TILESIZE/4, TILESIZE-TILESIZE/4, TILESIZE*2+TILESIZE/2, TILESIZE*2+TILESIZE/2))
            label = self.myfont.render("Game over!", 1, (255,255,0))
            self._display_surf.blit(label, (TILESIZE+TILESIZE/4, TILESIZE*2-TILESIZE/4))

        pygame.display.flip()
        pass
    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()