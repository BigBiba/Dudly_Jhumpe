import pygame
import os
import sys


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('data/mario.png')

    def __init__(self, pos):
        super().__init__(all_sprites, all_players)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 30

    def left_right(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            self.rect.x -= 15
        elif self.keys[pygame.K_RIGHT]:
            self.rect.x += 15

    def update(self):
        if pygame.sprite.spritecollideany(self, all_platforms) and player.speed <= 0:
            player.speed = 30
        player.rect = player.rect.move(0, -player.speed)
        if player.speed != -6:
            player.speed -= 2


class Platform(pygame.sprite.Sprite):
    image = pygame.image.load('data/platform.png')

    def __init__(self, pos):
        super().__init__(all_sprites, all_platforms)
        self.image = Platform.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


pygame.init()
pygame.display.set_caption('Дудла')
size = 500, 800
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('white'))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_platforms = pygame.sprite.Group()
player = Player((0, 700))
Platform((0, 750))
Platform((50, 650))
Platform((200, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.K_DOWN:
    player.left_right()
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(30)
    pygame.draw.line(screen, pygame.Color('red'), (0, 382), (500, 382))  # потом удалить
    pygame.display.flip()
pygame.quit()
