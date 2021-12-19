'''
Массив "скин змеи" состоит из цветов, подряд идущих, начиная с головы змеи.
Сколько в массиве элементов будет, столько и цветов будет в цикле. Дальше
цикл повторяется.
Пример: [YELLOW, ORANGE, RED, PURPLE, BLUE, GREEN]
'''

white = (255, 255, 255)
black = (0,0,0)
purple = (110, 24, 196)
green = (36, 181, 43)

yellow_food = (253, 253, 165)
red_food = (253, 96, 107)
green_food = (173, 255, 171)
blue_food = (186, 204, 254)
pink_food = (255, 119, 255)
pink_1_food = (255, 203, 207)
purple_food = (203, 158, 239)
light_blue_food = (184, 254, 254)
orange_food = (252, 185, 131)

green_skin_1 = (84, 254, 139)
green_skin_2 = (37, 254, 107)
green_skin_3 = (13, 254, 89)
green_skin_4 = (1, 245, 81)
green_skin_5 = (1, 228, 75)
green_skin_6 = (1, 220, 72)
green_skin_7 = (1, 207, 68)
green_skin_8 = (1, 194, 64)

red_skin_1 = (255, 104, 107)
red_skin_2 = (255, 96, 100)
red_skin_3 = (255, 91, 96)
red_skin_4 = (255, 81, 85)
red_skin_5 = (255, 72, 77)
red_skin_6 = (255, 62, 67)
red_skin_7 = (255, 51, 56)
red_skin_8 = (255, 43, 48)

yellow_skin_1 = (252, 254, 140)
yellow_skin_2 = (250, 254, 110)
yellow_skin_3 = (249, 254, 76)
yellow_skin_4 = (248, 254, 43)
yellow_skin_5 = (248, 253, 11)
yellow_skin_6 = (235, 241, 1)
yellow_skin_7 = (233, 239, 1)
yellow_skin_8 = (225, 231, 1)
yellow_skin_9 = (219, 224, 1)

bee_skin_1 = (235, 176, 74)
bee_skin_2 = (70, 70, 70)

green_skin = [green_skin_1, green_skin_2, green_skin_3, green_skin_4,
              green_skin_5, green_skin_6, green_skin_7, green_skin_8,
              green_skin_7, green_skin_6, green_skin_5, green_skin_4,
              green_skin_3, green_skin_2]
red_skin = [red_skin_1, red_skin_2, red_skin_3, red_skin_4,
           red_skin_5, red_skin_6, red_skin_7, red_skin_8,
           red_skin_7, red_skin_6, red_skin_5, red_skin_4,
           red_skin_3, red_skin_2]
yellow_skin = [yellow_skin_1, yellow_skin_2, yellow_skin_3, yellow_skin_4,
               yellow_skin_5, yellow_skin_6, yellow_skin_7, yellow_skin_8,
               yellow_skin_9, yellow_skin_8, yellow_skin_7, yellow_skin_6,
               yellow_skin_5, yellow_skin_4, yellow_skin_3, yellow_skin_2]
bee_skin = [bee_skin_1, bee_skin_2, bee_skin_2]

food = [yellow_food, red_food, green_food, blue_food, pink_food,
        pink_1_food, purple_food, light_blue_food, orange_food] # Массив цветов
purple_skin = [purple, black, white]
skins_snake = [red_skin, green_skin, yellow_skin, bee_skin] # Массив массивов скинов змей