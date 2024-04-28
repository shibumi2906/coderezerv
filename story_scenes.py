# S.G. Mikhaylov

# Класс сцены
# - отображает заданную числовым номером сцену и выводит  фразу диалога
# - выполняет цикл цикл работы внутри сцены:
#   вывод изображения сцены и изображения действующего лица диалога, выбор варианта действия,
#   и собственно действия на текущей сцене
# - по результату выполнения цикла системных событий выводит номер следующей сцены для обработки,
#   которая может быть любой по порядку

# Импорт библиотеки для работы с игровыми элементами
# import pygame


import Story_global as sgl
import story_message as sms

def info_on_screen(screen, info, start_x, start_y, width, height):
    # функция вывода HELP и Info about program на экран screen
    # выводит текст info методом класса StoryMessage в указанные координаты указанного размера
    return 0
def choice_of_mouse(mouse_xy, cases_choice):
    # после события нажатия кнопки мышки анализирует, попало нажатие на области принятия решений
    # mouse_xy - координаты мышки, где произошло нажатие
    # cases_choice - список прямоугольников подконтрольных зон
    # возвращает
    # case_on_off - признак попадания в зону принятия решений
    # case_number - номер зоны принятия решений
    return case_on_off, case_number

# функция вывода HELP и Info about program


class StoryScene(current_screen):
    # Класс сцены
    # отображает заданную числовым номером сцену и выводит фразу диалога
    # выполняет цикл цикл работы внутри сцены: смена изображений,
    # проведение диалога, выбор варианта действия
    # по результату выполнения цикла меняет глобальные переменные, указывающие на следующую сцену

    def __init__(self, current_scene):
        self.current_screen = current_screen
        self.current_scene = current_scene
        self.next_scene = self.current_scene
        # инициализация переменных сцены из БД

    def draw_scene(self):
        # отрисовывает сцену
        return 0


    def do_scene(self, current_scene):

        draw_scene()

        # Основной цикл сцены
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    next_scene = self.current_scene
                    running = False


            # ЛОГИКА СЦЕНЫ - в ней next_scene считывается из БД ID следующей сцены


            # Обновление экрана
            pygame.display.flip()

        # чтение ID next_scene из БД и возврат дальше в программу # требуется доработка
        return next_scene


if __name__ == '__main__':
    print('do_scene')