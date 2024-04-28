import pygame
import sys

class StoryScene():
    def __init__(self, background_image, options):
        # Загрузка фонового изображения и инициализация опций (кнопок)
        self.background_image = pygame.image.load(background_image)
        self.options = options

    def render(self, screen):
        # Отображение фона и кнопок на экране
        screen.blit(self.background_image, (0, 0))
        for option in self.options:
            option.draw(screen)

class OptionButton():
    def __init__(self, x, y, text, action):
        # Инициализация кнопки с текстом и действием
        self.image = pygame.Surface((200, 50))  # Создание поверхности для кнопки
        self.image.fill((0, 0, 128))  # Заливка кнопки цветом
        self.rect = self.image.get_rect(topleft=(x, y))  # Позиционирование кнопки
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)  # Шрифт текста
        text_surface = self.font.render(text, True, (255, 255, 255))  # Создание текстовой поверхности
        text_rect = text_surface.get_rect(center=self.rect.center)  # Позиционирование текста
        self.image.blit(text_surface, text_rect)  # Вставка текста на кнопку

    def draw(self, screen):
        # Отрисовка кнопки на экран
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        # Обработка событий (нажатия на кнопку)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()  # Выполнение действия, связанного с кнопкой

def option_action_1():
    print("Option 1 selected")
    # Действие для первого выбора

def option_action_2():
    print("Option 2 selected")
    # Действие для второго выбора

def option_action_3():
    print("Option 3 selected")
    # Действие для третьего выбора

def main_loop():
    pygame.init()  # Инициализация Pygame
    pygame.mixer.init()  # Инициализация аудиомиксера Pygame
    screen = pygame.display.set_mode((800, 600))  # Настройка размера окна
    pygame.display.set_caption("Визуальная Новелла")  # Заголовок окна

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load('path/to/your/music.mp3')
    pygame.mixer.music.play(-1)  # Повторение музыки

    # Создание кнопок с опциями
    options = [
        OptionButton(300, 200, "Option 1", option_action_1),
        OptionButton(300, 300, "Option 2", option_action_2),
        OptionButton(300, 400, "Option 3", option_action_3)
    ]
    scene = StoryScene('path/to/your/background.jpg', options)

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for option in options:
                option.handle_event(event)  # Обработка нажатий на кнопки

        screen.fill((0, 0, 0))  # Очистка экрана
        scene.render(screen)  # Отрисовка сцены
        pygame.display.flip()  # Обновление экрана

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
