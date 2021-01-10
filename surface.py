import pygame
from pygame.locals import *

class SurfaceR(pygame.Surface):
    def __init__(self, size, position):
        pygame.Surface.__init__(self, size)
        self.rect = pygame.Rect(position, size)
        self.position = position
        self.size = size

    def get_rect(self):
        return self.rect


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Screen!?")
    clock = pygame.time.Clock()
    fps = 30

    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    surface = pygame.Surface((70,200))
    surface.fill(red)

    surface_re = SurfaceR((300, 50), (100, 300))
    surface_re.fill(blue)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

        screen.blit(surface, (100,50))
        screen.blit(surface_re, surface_re.position)

        #pygame.draw.rect(screen, white, surface.get_rect())
        #pygame.draw.rect(screen, white, surface_re.get_rect())

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
