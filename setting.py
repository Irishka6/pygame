# setting
import math

w = 1200
h = 800
half_windth = w // 2
half_height = h // 2
fps = 60
TILE = 100

# ray
fov = math.pi / 3
half_fov = fov / 2
num_rays = 300
max_deph = 800
delta_angal = fov / num_rays
DIST = num_rays / (2 * math.tan(half_fov))
proj_coeff = 3 * DIST * TILE
SCALE = w //num_rays

#mini map
coof = 5
map_tile = TILE // coof

#plaer
plaer_coor = (half_windth, half_height)
plaer_angele = 0
plaer_speed = 2