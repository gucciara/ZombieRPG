import pygame
from sprites import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 32
FPS = 60

BLOCKS_LAYER = 2
GROUND_LAYER = 1
PLAYER_LAYER = 3  # Adjust layer for the player
#speed of player is equivalent to pixels moved - we want to use 32 since it's a 32x32 pixel game
PLAYER_SPEED = 32

BLACK = (0, 0, 0)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'BB.................B',
    'BBBB...............B',
    'BBB...............BB',
    'BBBB.............BBB',
    'B...............BBBB',
    'B..............BBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..............BBBBB',
    'B..BBBB..........B.B',
    'B..................B',
    'BB................BB',
    'BBB..............BBB',
    'BBBBBBBBBBBBBBBBBBBB',
]
