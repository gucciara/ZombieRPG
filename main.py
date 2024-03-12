from sprites import *
from configuration import *
import pygame
import random
import sys

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()

    def get_image(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet, (0,0), (x,y,width,height))
        sprite.set_colorkey(BLACK)

        return sprite

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('/Users/Tone/PycharmProjects/ZombieRPG/tiles_spritesheet.png')
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.Group()  # Group for enemies

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)

    def create(self):
        self.createTileMap()
        self.player = Player(self, 1, 2)
        self.all_sprites.add(self.player)

    def spawn_enemy(self):
        enemy_type = random.choice([SlowEnemy, MediumEnemy, FastEnemy])
        x = random.randint(0, WIN_WIDTH)
        y = random.randint(0, WIN_HEIGHT)
        enemy = enemy_type(self, x, y)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Pass player events to player class
            self.player.handle_event(event)

    def update(self):
        self.all_sprites.update()
        self.enemies.update()  # Update enemies

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

game = Game()
game.create()

# Spawn initial enemies
for _ in range(5):
    game.spawn_enemy()

game.main()

pygame.quit()
sys.exit()
