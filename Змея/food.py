import pygame
import colors
import random
from vector import Vector2d
import config

'''
Не сделан класс большой еды. Остальное вроде готово.
'''

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


class Big_food(Food):
    def __init__(self):
        # может быть будет зависеть от чего-то другого, не знаю. В общем если кнопка мыши зажата, он выдет 3 (например)
        # если не зажата, то просто 1. Это коэффециент, на который будет умножаться наша конечная скорость.
        # Выглядит как большая еда, которая еще и двигается как-то интересно
        pass

    def move(self):
        # Она там как-то быстро движется, надо подумать как
        pass

    def something(self):
        # хз что это за штука
        pass

    def eaten(self, event):
        # Говорит скоко новых шариков создавать. Это число сильно больше чем при обычной еде.
        pass

    def draw(self, center, r):
        '''
        Рисует шарик еды в случае, если он попадает на экран.
        Пересчитывает свои "глобальные" координаты в координаты экрана.
        '''
        alfa = config.radius / r
        new_coords = (self.coords - center) * alfa + config.center
        new_r = self.r * alfa

        pygame.draw.circle(config.screen, self.color, (new_coords.x, new_coords.y), new_r)