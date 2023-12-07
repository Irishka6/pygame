import math

import pygame
from setting import *
from map import wor_map

def ray_casting(sc, player_coor, player_ag):
    cur_ang = player_ag - half_fov
    xo, yo = player_coor
    for ray in range(num_rays):
        sina = math.sin(cur_ang)
        cosa = math.cos(cur_ang)
        for delta in range(max_deph):
            x = xo + delta * cosa
            y = yo + delta * sina
            # pygame.draw.line(sc, (100, 100, 100), player_coor, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in wor_map:
                delta *= math.cos(player_ag - cur_ang)
                prj = proj_coeff / (delta + 1)
                c = 255 / (1 + delta * delta * 0.00001)
                color = (c, c, c)
                pygame.draw.rect(sc, color, (ray * SCALE, half_height - prj // 2, SCALE, prj))
                break
        cur_ang += delta_angal