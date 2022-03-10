import os
TITLE = 'PLATFORMER'
TILE_SIZE = 18
GRAVITY = .5
SPEED = 5
JUMP = 10
# Colors
LIGHT_BLUE = (173, 227, 240)
GREY = (50, 50, 50)
SMOKEY_GREEN = (44, 94, 69)
# PATH Settings
GAME_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(GAME_DIR, 'images')
BRICK = os.path.join(IMG_DIR, 'brick.png')
LEVEL1 = os.path.join(GAME_DIR, 'level1.txt')
#ENEMY Settings
ENEMY_SPEED = 3