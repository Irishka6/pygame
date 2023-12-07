import pygame
from setting import *
from ray_cost import ray_casting
from map import mini_map

class Drowing:
    def __init__(self, sc, sc_mini):
        self.sc, self.sc_mini = sc, sc_mini

    def fon(self):
        pygame.draw.rect(self.sc, ('#4d8fac'), (0, 0, w, half_height))
        pygame.draw.rect(self.sc, ('#947966'), (0, half_height, w, half_height))

    def word(self, player_coor, player_ag):
        ray_casting(self.sc, player_coor, player_ag)

    def mini(self, player):
        self.sc_mini.fill((255, 255, 0))
        pygame.draw.line(self.sc, (0, 255, 0), (int(player.x // coof), int(player.y // coof)), ((player.x // coof) + 12 * math.cos(player.ag),
                                                                               (player.y // coof) + 12 * math.sin(player.ag)))
        pygame.draw.circle(self.sc, (0, 255, 255), (int(player.x // coof), int(player.y // coof)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc, (0, 255, 100), (x, y , map_tile, map_tile))
        self.sc_mini.blit(self.sc, (0, h - h // map_tile))
