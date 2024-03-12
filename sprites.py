from configuration import *
import pygame

#use this as a template for every class. You will be replacing the x and y coordinate in coordination w/ spritesheet
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game=game
        self._layer=BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(31,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game=game
        self._layer=GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        image_to_load = pygame.image.load("/Users/Tone/PycharmProjects/ZombieRPG/character.png")
        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey(BLACK)
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def handle_event(self, event):
        # Handle player movement events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change -= PLAYER_SPEED
                self.facing = 'left'
            elif event.key == pygame.K_RIGHT:
                self.x_change += PLAYER_SPEED
                self.facing = 'right'
            elif event.key == pygame.K_UP:
                self.y_change -= PLAYER_SPEED
                self.facing = 'up'
            elif event.key == pygame.K_DOWN:
                self.y_change += PLAYER_SPEED
                self.facing = 'down'

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0
