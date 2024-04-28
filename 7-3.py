import pygame
import sys

# Класс для отображения сцены
class StoryScene():
    def __init__(self, background_image, hero_image, hero_pos, options):
        self.background_image = background_image  # Задний фон сцены
        self.hero_image = hero_image  # Изображение героя
        self.hero_pos = hero_pos  # Позиция героя
        self.options = options  # Список кнопок с вариантами ответов

    def render(self, screen):
        # Отрисовка фона, героя и кнопок на экране
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.hero_image, self.hero_pos)
        for option in self.options:
            option.draw(screen)

# Класс для отображения кнопок вариантов
class OptionButton():
    def __init__(self, x, y, text, action):
        self.image = pygame.Surface((200, 50))  # Поверхность кнопки
        self.image.fill((0, 0, 128))  # Цвет кнопки
        self.rect = self.image.get_rect(topleft=(x, y))  # Расположение кнопки
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)
        text_surface = self.font.render(text, True, (255, 255, 255))  # Текст на кнопке
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, text_rect)

    def draw(self, screen):
        # Отрисовка кнопки на экране
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        # Обработка событий нажатия на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()  # Выполнение действия при нажатии на кнопку

# Функции для действий, связанных с кнопками
def option_action_1():
    print("Исследовать маяк ночью.")
    # Здесь будет код перехода к следующей сцене

def option_action_2():
    print("Проанализировать архивные записи.")
    # Здесь будет код перехода к следующей сцене

def option_action_3():
    print("Провести ночь в кафе 'Морской Бриз'.")
    # Здесь будет код перехода к следующей сцене

# Главный цикл программы
def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Визуальная Новелла")

    # Загрузка изображений
    background_image = pygame.image.load('imige/resized_image.png')
    hero_image = pygame.image.load('imige/p001.png')
    hero_pos = (0, 600 - hero_image.get_height())  # Герой в нижнем левом углу

    # Создание кнопок
    options = [
        OptionButton(300, 200, "1. Исследовать маяк ночью.", option_action_1),
        OptionButton(300, 300, "2. Проанализировать записи.", option_action_2),
        OptionButton(300, 400, "3. Провести ночь в кафе.", option_action_3)
    ]

    # Инициализация сцены
    scene = StoryScene(background_image, hero_image, hero_pos, options)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for option in options:
                option.handle_event(event)

        screen.fill((0, 0, 0))
        scene.render(screen)  # Отрисовка сцены на экране
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
