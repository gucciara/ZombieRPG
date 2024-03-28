import pygame
from sprites import *

WIN_WIDTH = 1400
WIN_HEIGHT = 950
TILESIZE = 32
FPS = 60

BLOCKS_LAYER = 2
GROUND_LAYER = 1
PLAYER_LAYER = 3
ENEMY_LAYER = 4
#speed of player is equivalent to pixels moved - we want to use 32 since it's a 32x32 pixel game
PLAYER_SPEED = 32

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BB.................................BBBBB',
    'BBBB...................................B',
    'BBB...................................BB',
    'BBBB.................................BBB',
    'B...................................BBBB',
    'B..................................BBBBB',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B..................................BBBBB',
    'B..BBBB......B.......................B.B',
    'B......................................B',
    'BBBB..............................BBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBBBBBB.........................BBBBBBB',
    'BBBB.........................BBBBBBBBBBB',
    'BBBBBB.........................BBBBBBBBB',
    'BBBB.........................BBBBBBBBBBB',
    'BBBBBBB.........................BBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]