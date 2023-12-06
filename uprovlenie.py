from setting import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = plaer_coor
        self.ag = plaer_angele

    def coor(self):
        return (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        sina = math.sin(self.ag)
        cosa = math.cos(self.ag)
        if keys[pygame.K_w]:
            self.x += plaer_speed * cosa
            self.y += plaer_speed * sina
        if keys[pygame.K_s]:
            self.x += -plaer_speed * cosa
            self.y += -plaer_speed * sina
        if keys[pygame.K_d]:
            self.x += -plaer_speed * sina
            self.y += plaer_speed * cosa
        if keys[pygame.K_a]:
            self.x += plaer_speed * sina
            self.y += -plaer_speed * cosa
        if keys[pygame.K_LEFT]:
            self.ag -= 0.02
        if keys[pygame.K_RIGHT]:
            self.ag += 0.02
