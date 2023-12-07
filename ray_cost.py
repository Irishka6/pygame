import math

import pygame
from setting import *
from map import wor_map


def mxy(xm, ym):
    return (xm // TILE) * TILE, (ym // TILE) * TILE
def ray_casting(sc, player_coor, player_ag):
    xo, yo = player_coor
    xm, ym = mxy(xo, yo)
    cur_ang = player_ag - half_fov
    for ray in range(num_rays):
        sina = math.sin(cur_ang)
        cosa = math.cos(cur_ang)

        # vertical
        x, dx = (xm + TILE, 1) if cosa >= 0 else (xm, -1)
        for i in range(0, w, TILE):
            depth_v = (x - xo) /cosa
            y = yo + depth_v * sina
            if mxy(x + dx, y) in wor_map:
                break
            x += dx * TILE

        # gorizont
        y, dy = (ym + TILE, 1) if sina >= 0 else (ym, -1)
        for i in range(0, h, TILE):
            depth_h = (y - yo) / sina
            x = xo + depth_h * cosa
            if mxy(x, y + dy) in wor_map:
                break
            y += dy * TILE

        delta = depth_v if depth_v < depth_h else depth_h
        delta *= math.cos(player_ag - cur_ang)
        delta = max(delta, 0.00001)
        prj = min(int(proj_coeff / (delta + 1)), 2 * h)
        c = 255 / (1 + delta * delta * 0.00002)
        color = (c // 2, c // 2, c // 3)
        pygame.draw.rect(sc, color, (ray * SCALE, half_height - prj // 2, SCALE, prj))
        cur_ang += delta_angal


