import pygame
from settings import *
from map import world_map
import math

def mapping(a, b):
    return ((a // TITLE) * TITLE, (b // TITLE) * TITLE)

def ray_casting(sc, player_pos, player_angle, textures):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        #verticals
        x, dx = (xm + TITLE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TITLE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TITLE

        #horisontals
        y, dy = (ym + TITLE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WIDTH, TITLE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TITLE

        #projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TITLE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.000001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGTH)

        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGTH)
        wall_column = pygame.transform.scale(wall_column,(SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGTH - proj_height // 2))

        cur_angle += DELTA_ANGLE





