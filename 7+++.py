import pygame
import sys
import os


class Story_messages():
    def __init__(self, scene_picture, hero_picture, hero_x, hero_y, message):
        self.scene_picture = pygame.transform.scale(pygame.image.load(scene_picture), (800, 600))
        self.hero_picture = pygame.transform.scale(pygame.image.load(hero_picture), (800, 600))
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.message = message

    def screen_blit(self, screen, font):
        # Рендеринг текста по буквам с учётом переноса строки
        words = self.message.split()
        x, y = 40, 510  # начальные координаты текста
        screen.blit(self.scene_picture, (0, 0))
        screen.blit(self.hero_picture, (self.hero_x, self.hero_y))

        for word in words:
            for char in word:
                text_surface = font.render(char, True, (230, 230, 230))
                screen.blit(text_surface, (x, y))
                x += text_surface.get_width()  # сдвигаем x для следующей буквы
                pygame.display.flip()
            x += font.size(' ')[0]  # добавляем пробел после слова
            if x > 800 - 10:  # проверяем, не выходит ли текст за границы экрана
                x = 40
                y += font.get_linesize()


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Визуальная Новелла 'Тайны Старого Маяка'")
    font = pygame.font.Font(None, 28)  # Шрифт для текста

    message_index = 0
    messages = [Story_messages('path/to/image.jpg', 'path/to/hero_image.jpg', -300, 200, "Текст сообщения ...")]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Очистка экрана
        if message_index < len(messages):
            messages[message_index].screen_blit(screen, font)  # Рендеринг текущего сообщения

        pygame.display.flip()  # Обновление дисплея

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()
