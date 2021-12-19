import pygame
import colors
import random
import math

import config
from ball import Ball
from vector import Vector2d
from head import Head
from food import Food

'''
Задачи:
1) Прописать уменьшение размеров змеи при ускорении и появление новой еды

Не решенные задачи:
1) Генерирование змеи вдали от других змей
5) Все числовые значения буду подгонять по красоте
7) Как сделать чтобы экран всегда в центре держал голову змеи
'''


class Snake():
    def __init__(self, color=colors.skins_snake, name=0):
        ''' Создает новую змею в случайном месте, длиной 50 шариков.
        Координатой змеи считаются координаты центра головы. '''
        '''
        Не готово:
        1) Имя змеи
        '''
        if color == colors.skins_snake:
            self.colors = random.choice(colors.skins_snake)
        else:
            self.colors = color
        self.num = len(self.colors)
        self.name = name
        self.energy = 0

        self.x = 500
        self.y = 500
        self.coords = Vector2d(self.x, self.y)
        self.r = 5
        config.snake_radius = self.r
        self.length = 0
        self.life = 1

        self.balls = []
        head = Head(color=self.colors[0], x=self.x, y=self.y)
        self.balls += [head]
        self.length += 1
        for i in range(9):
            color = self.colors[(i + 1) % self.num]
            new_ball = Ball(x=self.x, y=self.y, color=color, r=5)
            self.balls += [new_ball]
            self.length += 1
        self.energy = self.length
        self.speed_timer = 0

    def move(self, speeding=1):
        ''' Двигает змею, начиная с последнего шарика, меняяя его координаты
        на координаты предыдущего. Для головы движение прописано в отдельном классе.
        Speeding принимает значение либо 1, либо 2-4, когда зажата кнопка мыши. '''
        if len(self.balls) > 9:
            for i in range(speeding):
                for b in reversed(self.balls):
                    if self.balls.index(b) > 0:
                        b.move(self.balls[(self.balls.index(b) - 1)])
                    else:
                        b.move(speeding)
                        self.x = b.x
                        self.y = b.y
                        self.coords = Vector2d(self.x, self.y)
                self.hit()
                self.eat()
            if speeding != 1:
                self.speed_timer += 1
            else:
                self.speed_timer = 0
            if self.speed_timer >= 4:
                self.speed_timer = 0
                self.energy -= 1
                self.reduction()
        else:
            for b in reversed(self.balls):
                if self.balls.index(b) > 0:
                    b.move(self.balls[(self.balls.index(b) - 1)])
                else:
                    b.move(speeding)
                    self.x = b.x
                    self.y = b.y
                    self.coords = Vector2d(self.x, self.y)
            self.hit()
            self.eat()
        if self.x - self.r < 0 or self.x + self.r > config.max_width or self.y + self.r > config.max_height or self.y - self.r < 0:
            self.destroyed()

    def hit(self):
        ''' Проверяет не столкнулась ли змея с другой змеей. Если столкнулась, то
        уничтожает змею, создает на ее месте много больших шариков еды'''

        for other in config.snakes:
            if config.snakes.index(other) != config.snakes.index(self):
                for b in other.balls:
                    if other.balls.index(b) != 0:
                        if abs(self.coords - b.coords) < self.r + b.r:
                            self.destroyed()
                    else:
                        delta_r2 = self.coords - other.coords
                        delta_r1 = other.coords - self.coords
                        self_alfa = (delta_r1.x * self.x + delta_r1.y * self.y) / abs(self.coords) / abs(delta_r1)
                        other_alfa = (delta_r2.x * self.other + delta_r2.y * self.other) / abs(other.coords) / abs(
                            delta_r2)
                        if other_alfa < self_alfa:
                            other.destroyed()
                        elif self_alfa < other_alfa:
                            self.destroyed()
                        else:
                            if config.snakes.index(self) < config.snakes.index(other):
                                self.destroyed()
                            else:
                                other.destroyed()
                        # Сравнивает углы под которыми было соударение к линии, соединяющей центры. Выживает штука с наибольшим углом. При равных, выживает случайная

    def eat(self):
        '''Чекает столкнулась ли башка с едой, создает новый шарик, убивает еду'''

        for f in config.all_food:
            if f.r + self.r > abs(self.coords - f.coords):
                self.energy += f.energy
                config.food_energy -= f.energy
                config.snake_energy += f.energy
                del config.all_food[config.all_food.index(f)]
        self.grow()

    def grow(self):
        '''
        Тут смотрится сколько энергии в змее и если ее значение больше чем сколько-то,
        то появляется новый шарик и увеличивается радиуc
        '''

        length = self.energy // 1
        while len(self.balls) < length:
            color = self.colors[len(self.balls) % self.num]
            new_ball = Ball(x=self.balls[len(self.balls) - 1].x, y=self.balls[len(self.balls) - 1].y, color=color,
                            r=self.r)
            self.balls += [new_ball]
            self.length += 1

            for b in self.balls:
                b.r += 0.01
            self.r += 0.01
            config.snake_radius += 0.01

    def reduction(self):

        length = self.energy // 1
        while len(self.balls) > length:
            new_food = Food(r=2, x=self.balls[len(self.balls) - 1].x, y=self.balls[len(self.balls) - 1].y)
            config.all_food += [new_food]
            config.food_energy += 1
            config.snake_energy -= 1
            del self.balls[len(self.balls) - 1]
            self.length -= 1
            self.r -= 0.01
            config.snake_radius -= 0.01

    def destroyed(self):
        '''
        Тут уничтожается змея, превращается в большую еду каждый шарик змейки
        ждет некоторое время и выкидывает на экран геймовера.
        '''

        if len(self.balls) % 3 == 0:
            config.snake_energy += 2
        if len(self.balls) % 3 == 1:
            config.snake_energy += 1
        for b in self.balls:
            if self.balls.index(b) % 3 == 0:
                dr = random.uniform(0, self.r - 2)
                dx = random.uniform(0 - dr, dr)
                sign = random.choice([-1, 1])
                dy = math.sqrt(dr ** 2 - dx ** 2) * sign

                new_food = Food(r=5, x=b.x + dx, y=b.y + dy)
                config.all_food += [new_food]
                config.food_energy += 2.5
                config.snake_energy -= 2
                del self.balls[self.balls.index(b)]
        del config.snakes[config.snakes.index(self)]
        self.life = 0

    def draw(self):
        '''
        Вызывается каждый раз, когда нужно отрисовать змею.
        '''

        for b in reversed(self.balls):
            b.draw(self.coords)