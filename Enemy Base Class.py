import pygame
import random
import math
import time

# Remember to replace the image file paths ('slow_enemy.png', 'medium_enemy.png', and 'fast_enemy.png') with
# the custom image files being used

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Enemy Spawn Game')

# Base class for all enemies
class Enemy:
    def __init__(self, x, y, speed, damage, health, image_file):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.health = health
        self.image = pygame.image.load(image_file)

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

# Enemy subclasses
class SlowEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, speed=1, damage=10, health=20, image_file='slow_enemy.png')

class MediumEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, speed=3, damage=5, health=15, image_file='medium_enemy.png')

class FastEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, speed=5, damage=1, health=10, image_file='fast_enemy.png')

# Utility functions
def enemy_is_close_to_player(enemy, player, distance_threshold=50):
    distance = math.sqrt((player['x'] - enemy.x) ** 2 + (player['y'] - enemy.y) ** 2)
    return distance <= distance_threshold

def spawn_enemy():
    enemy_type = random.choice([SlowEnemy, MediumEnemy, FastEnemy])
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    return enemy_type(x, y)

# Main game variables
enemies = []
player = {'x': 400, 'y': 300, 'health': 100}  # Simple player representation
last_spawn_time = time.time()
spawn_interval = 5  # Seconds

# Game loop
running = True
while running:
    current_time = time.time()
    if current_time - last_spawn_time >= spawn_interval:
        enemies.append(spawn_enemy())
        last_spawn_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Enemy logic
    for enemy in enemies[:]:
        enemy.move_towards_player(player['x'], player['y'])
        if enemy_is_close_to_player(enemy, player):
            enemy.attack(player)
        screen.blit(enemy.image, (enemy.x, enemy.y))
        # Placeholder for enemy taking damage, replace with actual logic
        if enemy.take_damage(0):  # Currently, enemies do not take damage
            enemies.remove(enemy)

    # Update display
    pygame.display.flip()

pygame.quit()
