import pygame
import sys


class Story_messages():
    def init(self, scene_picture, hero_picture, hero_x, hero_y, message):
        # Инициализация сцены и персонажа с их изображениями и позиционированием
        self.scene_picture = pygame.transform.scale(pygame.image.load(scene_picture), (800, 600))
        self.hero_picture = pygame.transform.scale(pygame.image.load(hero_picture), (800, 600))
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.message = message

    def screen_blit(self, screen, font):
        # Рендеринг сцены, персонажа и текста с посимвольным выводом
        screen.blit(self.scene_picture, (0, 0))
        screen.blit(self.hero_picture, (self.hero_x, self.hero_y))

        # Рендеринг текста по буквам с переносом строки
        words = self.message.split()
        x, y = 40, 510  # Начальные координаты для текста
        for word in words:
            for char in word:
                text_surface = font.render(char, True, (230, 230, 230))
                screen.blit(text_surface, (x, y))
                x += text_surface.get_width()  # Сдвигаем x для следующей буквы
                pygame.display.flip()
            x += font.size(' ')[0]  # Добавляем пробел после слова
            if x > 800 - 10:  # Перенос строки, если текст достигает края экрана
                x = 40
                y += font.get_linesize()


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Визуальная Новелла 'Тайны Старого Маяка'")
    font = pygame.font.Font(None, 28)  # Шрифт для рендеринга текста

    # Список сообщений для отображения
    messages = [
        Story_messages('images/s001.png', 'images/p001.png', -300, 200, "Текст сообщения ...")
    ]
    message_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Очистка экрана
        if message_index < len(messages):
            messages[message_index].screen_blit(screen, font)  # Рендеринг текущего сообщения с передачей шрифта

        pygame.display.flip()  # Обновление дисплея

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()