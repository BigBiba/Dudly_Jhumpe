import pygame
import sys
from ships import *


def main():
    pygame.init()
    pygame.display.set_caption("Space Ranger")
    player = Player()
    screen = pygame.display.set_mode((500, 500))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.move(event.pos)
    all_sprites.draw(screen)
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
