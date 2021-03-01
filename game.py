import pygame
from random import randrange
import sys


def main():
    class Player(pygame.sprite.Sprite):
        image = pygame.image.load('data/doodle.png')
        record = 0

        def __init__(self, pos, group):
            super().__init__(group)
            self.image = Player.image
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = pos[0]
            self.rect.y = pos[1]
            self.speed = 30
            self.flag = True

        def left_right(self):
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_LEFT]:
                self.rect.x -= 15
            elif self.keys[pygame.K_RIGHT]:
                self.rect.x += 15

        def update(self):
            if pygame.sprite.spritecollideany(self, all_platforms) and self.speed <= 0:
                self.speed = 30
            if (self.rect.y - self.speed) <= EXTREME_HEIGHT:
                self.flag = False
                Platform.speed = self.speed
            if self.speed <= 0:
                self.flag = True
                Platform.speed = -4
            if self.flag:
                self.rect = self.rect.move(0, -self.speed)
            if self.speed != -8:
                self.speed -= 2

        def kill_before_restart(self):
            self.kill()

    class Platform(pygame.sprite.Sprite):
        image = pygame.image.load('data/platform.png')
        speed = -4

        def __init__(self, pos, group):
            super().__init__(group)
            self.image = Platform.image
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = pos[0]
            self.rect.y = pos[1]

        def update(self):
            self.rect = self.rect.move(0, Platform.speed + 4)
            Player.record += Platform.speed + 4
            if self.rect.bottom > 800:
                self.kill()
            if self.rect.bottom > 0:
                self.remove(areas_platforms)

        def kill_before_restart(self):
            self.kill()

    def new_platforms():
        if len(areas_platforms) != 2:
            rnd_coords = (randrange(0, EX_X), randrange(-200, -10, 1))
            platform = Platform(rnd_coords, (all_sprites, all_platforms))
            if pygame.sprite.spritecollideany(platform, areas_platforms) == None:
                platform.add(areas_platforms)
            else:
                platform.kill()

    def start_platforms():
        for _ in range(30):
            rnd_coords = (randrange(0, EX_X), randrange(0, EX_Y))
            platform = Platform(rnd_coords, all_sprites)
            if pygame.sprite.spritecollideany(platform, all_platforms) == None:
                platform.add(all_platforms)
            else:
                platform.kill()

    def terminate():
        pygame.quit()
        sys.exit()

    def start_screen():
        intro_text = ["DOODLE JHUMPE", "",
                      "Правила игры",
                      "Старайтесь набрать как можно больший счет",
                      "Управляйте стрелками 'влево' и 'вправо'",
                      "Для выхода нажмите ESC",
                      "Для рестарта нажмите 'R'"]
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('blue'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()

    def end_screen():
        intro_text = ["ВЫ ПРОИГРАЛИ", "",
                      "ЭТО ПЕЧАЛЬНО",
                      f"Ваш счет: {Player.record // 100}"]
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        terminate()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        main()
            pygame.display.flip()

    EXTREME_HEIGHT = 390
    WIDTH = 500
    HEIGHT = 800
    EX_X = WIDTH - 53
    EX_Y = HEIGHT - 10
    fon = pygame.image.load('data/fon.png')

    pygame.init()
    pygame.display.set_caption('Дудла')
    size = 500, 800
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('white'))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    all_players = pygame.sprite.Group()
    all_platforms = pygame.sprite.Group()
    areas_platforms = pygame.sprite.Group()
    player = Player((0, 700), (all_sprites, all_players))
    Platform((0, 750), (all_sprites, all_platforms))

    start_platforms()
    start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    main()
        player.left_right()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        if player.rect.y > HEIGHT:
            player.kill()
            end_screen()
        new_platforms()
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()


main()
