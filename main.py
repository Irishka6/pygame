import pygame
from setting import *
from uprovlenie import Player
import math
from map import wor_map

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

    pygame.draw.circle(screen, (0, 255, 0), (int(player.x), int(player.y)), 12)
    pygame.draw.line(screen, (0, 255, 0), (int(player.x), int(player.y)), (player.x + w * math.cos(player.ag),
                                                          player.y + w * math.sin(player.ag)))
    for x, y in wor_map:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(fps)

