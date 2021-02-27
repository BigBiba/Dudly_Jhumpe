import pygame

all_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('data/mario.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.healh = 3

    def move(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x, pos_y

    def shoot(self):
        pass
