import pygame
from setting import *
from uprovlenie import Player
import math
from map import wor_map
from ray_cost import ray_casting
from dowin import Drowing

pygame.init()
screen = pygame.display.set_mode((w, h))
screen_mini = pygame.Surface((w // coof, h // coof))
clock = pygame.time.Clock()
player = Player()
dr = Drowing(screen, screen_mini)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill((0, 0, 0))
    screen_mini.fill((255, 255, 0))
    dr.fon()
    dr.word((int(player.x), int(player.y)), player.ag)
    dr.mini(player)
    pygame.display.flip()
    clock.tick(fps)

