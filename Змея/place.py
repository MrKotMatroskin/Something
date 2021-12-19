from vector import Vector2d
import config
import colors
import pygame

'''
Штука, рисующая рамку
'''

class Place:
    def __init__(self):
        self.coords_1 = Vector2d(0, 0)
        self.coords_2 = Vector2d(0, config.max_height)
        self.coords_3 = Vector2d(config.max_width, config.max_height)
        self.coords_4 = Vector2d(config.max_width, 0)
    def draw(self, center):
        alfa = config.radius / config.snake_radius
        new_coords1 = (self.coords_1 - center) * alfa + config.center
        new_coords2 = (self.coords_2 - center) * alfa + config.center
        new_coords3 = (self.coords_3 - center) * alfa + config.center
        new_coords4 = (self.coords_4 - center) * alfa + config.center
        pygame.draw.lines(config.screen, colors.red_skin_8, True, [[new_coords1.x, new_coords1.y],
                                                 [new_coords2.x, new_coords2.y],
                                                 [new_coords3.x, new_coords3.y],
                                                 [new_coords4.x, new_coords4.y]], 4)