import colors
from vector import Vector2d

screen_width = 800
screen_height = 600
max_width = 800
max_height = 600
background_image = 'images/background_1(2, 3, 4).jpg'
screen = 0
process = True

energy = 0
food_energy = 0
snake_energy = 0
max_energy = 100
snake_radius = 5 # Радиус змеи в абсолютных координатах, меняется в процессе игры
radius = 10 # Сколько реальных пикселей занимает радиус змеи (на экране)
center = Vector2d(screen_width // 2, screen_height // 2)
coefficient = 0.5 # Коэффициент для нахождения минимального радиуса по которому может двигаться голова змеи
length = 0

snakes = []
all_food = []