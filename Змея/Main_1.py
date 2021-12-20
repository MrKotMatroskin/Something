import pygame
from place import Place
import config
from food import Food
from snake import Snake
import colors



class Main():
    def __init__(self):
        pygame.init()
        background = pygame.display.set_mode((config.screen_width, config.screen_height))
        background.fill(colors.black)

        # инструкции
        f_instr = pygame.font.Font(None, 30)
        text1 = f_instr.render('Eat to grow longer!', 1, (colors.white))
        text2 = f_instr.render("Don't run into other players!", 1, (colors.white))
        background.blit(text1, (270, 230))  # фиксить координаты
        background.blit(text2, (250, 260))  # фиксить координаты

        # счёт
        f_score = pygame.font.Font(None, 14)
        text_score = f_score.render('RECORD SCORE:' + str(config.length), 1, (colors.white))
        background.blit(text_score, (350, 300))  # фиксить координаты

        # поверхность, на которой будет отображаться название игры
        name = pygame.Surface((360, 80))
        name.fill(colors.white)
        name.set_alpha(0)  # прозрачность
        background.blit(name, (220, 120))
        # текст названия игры
        f_name = pygame.font.Font(None, 125)
        text_name1 = f_name.render('slither', 1, (colors.green))
        text_name2 = f_name.render('.io', 1, (colors.purple))
        background.blit(text_name1, (220, 120))
        background.blit(text_name2, (480, 120))

        # куда прилепим кнопку play
        pl = pygame.Surface((160, 80))
        pl.fill(colors.green)
        pl.set_alpha(200)  # прозрачность
        background.blit(pl, (320, 400))
        # слово плэй
        f_pl = pygame.font.Font(None, 80)  # ыыыы
        text_pl = f_pl.render('Play!', 2, (colors.white))
        background.blit(text_pl, (325, 410))

        pygame.display.update()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # тип события - нажимание на крестик
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # тип события - опускание кнопки мыши
                    if event.button == 1:  # тип кнопки - левая
                        if 320 < event.pos[0] < 480 and 400 < event.pos[1] < 480:  # вроде должно
                            self.game()

    def game(self):  # после нажатия на кнопку play начинаем играть
        pygame.init()
        config.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        config.screen.fill(colors.white)
        new_snake = Snake()
        config.snakes += [new_snake]
        place = Place()

        config.process = True

        while config.process:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                speeding = 2
            else:
                speeding = 1
            for s in config.snakes:
                s.move(speeding)
            while config.food_energy + config.snake_energy < config.max_energy:  # Ну или сколько там
                new_food = Food()
                config.all_food += [new_food]
            config.screen.fill(colors.black)
            for f in config.all_food:
                f.draw(new_snake.coords)
            for s in config.snakes:
                s.draw()
            place.draw(new_snake.coords)
            pygame.display.update()
            pygame.time.delay(40)
            if new_snake.life == 0:
                if config.length < new_snake.length:
                    # print(new_snake.length)
                    config.length = new_snake.length
                new_game = Main()


if __name__ == "__main__":
    new_game = Main()