from sprites import *
from config import *
import pygame
import random
import asyncio
import datetime


class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()

    def get_image(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)

        return sprite


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('tiles_spritesheet.png')
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
        font = pygame.font.Font(None, 100)
        text_surface = font.render(str(self.player.hunger), True, WHITE)
        text_area = text_surface.get_rect()
        text_area.center = (WIN_WIDTH - 60, WIN_HEIGHT - 60)
        self.screen.blit(text_surface, text_area)
        pygame.display.update()

    """
        hunger is supposed to decrease when the player is in the overworld but NOT during battle. Bool parameter should 
        be set to 'True' for when you want this function to be active.
    """

    async def decrease_hunger(self) -> int:
        last_tick = datetime.datetime.now()
        while self.player.hunger > 0:
            await asyncio.sleep(0.25)
            if datetime.datetime.now() - last_tick > datetime.timedelta(seconds=0.25):
                print(self.player.hunger)
                self.player.hunger -= 1
                last_tick = datetime.datetime.now()

        if self.player.hunger <= 0:
            raise Exception("Player died of hunger", self)
        return self.player.hunger

    async def game_loop(self):
        asyncio.create_task(self.decrease_hunger())  # Start async operation
        while self.running:
            self.events()
            self.update()
            self.draw()
            await asyncio.sleep(0.01)

    def main(self):
        asyncio.run(self.game_loop())


def start_pygame():
    game = Game()
    game.create()
    # Spawn initial enemies
    for _ in range(5):
        game.spawn_enemy()
    game.main()
    pygame.quit()

if __name__ == '__main__':
    start_pygame()