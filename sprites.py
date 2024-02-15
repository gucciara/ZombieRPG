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
        self.heigh = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(#on SPRITESHEET THAT I HAVE TO MAKE, PICK COORDINATES FOR BLOCK ON SHEET AND INSERT in X AND Y format, self.width, self.height)
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
        self.heigh = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(#on SPRITESHEET THAT I HAVE TO MAKE, PICK COORDINATES FOR BLOCK ON SHEET AND INSERT in X AND Y; x, y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y