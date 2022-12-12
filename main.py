import pygame
from settings import *
from player import Player
from drawing import Drawing
from sound import music

FPS = 60

pygame.mixer.pre_init(frequncy, size, channels, buffer)
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGTH))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGTH // MAP_SCALE))
s = pygame.mixer.Sound("sound/shagi.ogg")
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
S = music(s, [0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    S.Shagi(player.pos)
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()
