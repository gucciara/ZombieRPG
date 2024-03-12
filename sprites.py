from configuration import *
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = BLOCKS_LAYER
        self.game = game

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(31, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = GROUND_LAYER
        self.game = game

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = PLAYER_LAYER
        self.game = game

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
        self.image.blit(image_to_load, (0, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

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

class SlowEnemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = ENEMY_LAYER
        self.game = game

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.speed = 4
        self.damage = 10
        self.health = 20

        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load('/Users/Tone/PycharmProjects/ZombieRPG/pyro.jpg')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def move_towards_player(self, player_x, player_y):
        direction = pygame.math.Vector2(player_x - self.x, player_y - self.y).normalize()
        self.x += direction.x * self.speed
        self.y += direction.y * self.speed

    def attack(self, player):
        player['health'] -= self.damage  # Assuming player is a dict with a health attribute

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return True
        return False

class MediumEnemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = ENEMY_LAYER
        self.game = game

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.speed = 8
        self.damage = 5
        self.health = 15

        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load('/Users/Tone/PycharmProjects/ZombieRPG/jack.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    # Implement methods: move_towards_player, attack, take_damage

class FastEnemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game.all_sprites)
        self._layer = ENEMY_LAYER
        self.game = game

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.speed = 16
        self.damage = 1
        self.health = 10

        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load('/Users/Tone/PycharmProjects/ZombieRPG/ripper.jpg')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
