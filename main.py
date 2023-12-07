import pygame
from setting import *
from uprovlenie import Player
import math
from map import wor_map
from ray_cost import ray_casting

pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill((0, 0, 0))

    ray_casting(screen, (int(player.x), int(player.y)), player.ag)

    pygame.display.flip()
    clock.tick(fps)

