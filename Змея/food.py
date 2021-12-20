import pygame
import colors
import random
from vector import Vector2d
import config

class Food():
    def __init__(self, r=0, x=0, y=0, color=colors.food):
        '''
        Создается 1 шарик еды, с заданными координатами, радиусом, цвет выбирается случайно из списка цветов.
        '''
        self.x = x
        self.y = y
        self.r = r
        if color == colors.food:
            self.color = random.choice(color)
        else:
            self.color = color
        if self.r == 0:
            self.r = random.uniform(1, 5)
        self.energy = 0.5 * self.r
        config.food_energy += self.energy
        if self.x == 0 and self.y == 0:  # Создает шарик еды в случайном месте
            self.x = random.uniform(5, config.max_width - 5)
            self.y = random.uniform(5, config.max_height - 5)
        self.coords = Vector2d(self.x, self.y)

    def draw(self, center):
        '''
        Рисует шарик еды в случае, если он попадает на экран.
        Пересчитывает свои "глобальные" координаты в координаты экрана.
        '''
        alfa = config.radius / config.snake_radius
        new_coords = (self.coords - center) * alfa + config.center
        new_r = int(self.r * alfa)

        pygame.draw.circle(config.screen, self.color, (int(new_coords.x), int(new_coords.y)), new_r)
