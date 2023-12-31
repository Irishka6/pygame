from setting import *

text_map = ['wwwwwwwwwwww',
            'w----www---w',
            'w-w--------w',
            'w----www---w',
            'w-----w----w',
            'w---w------w',
            'w---w--w---w',
            'wwwwwwwwwwww'
            ]

wor_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'w':
            wor_map.add((i * TILE, j * TILE))
            mini_map.add((i * map_tile, j * map_tile))
