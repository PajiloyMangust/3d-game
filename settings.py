import math


# game settings
WIDTH = 1200
HEIGTH = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGTH = HEIGTH // 2
TITLE = 100
FPS_POS = (WIDTH - 65, 5)

#minimap
MAP_SCALE = 5
MAP_TILE = TITLE // MAP_SCALE
MAP_POS = (0, 4 * HEIGTH //MAP_SCALE)



#ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2*math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TITLE
SCALE =  WIDTH // NUM_RAYS

# player
player_pos = (HALF_WIDTH, HALF_HEIGTH)
player_angle = 0
player_speed = 1
rotation_speed = 0.015

# colors
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0,)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186 ,255)
YELLOW = (220, 220, 0)

# sound
frequncy = 9100
size = -16
channels = 1
buffer = 512

#texture
TEXTURE_WIDTH = 1200
TEXTURE_HEIGTH = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TITLE
