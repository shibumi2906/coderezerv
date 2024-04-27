# S.G. Mikhaylov

# организует и осуществляет вывод текстовых сообщений на текущий экран истории в выделенном прямоугольнике
# входными данными являются :
# screen - окно программы
# screen_x, screen_y, background_width, background_height - координаты и размер прямоугольника
# background_color - бэкграунд изображение прямоугольника
# font, font_size - используемый фонт и его характеристики
# text - текст сообщения

import pygame
import story_globals as sgl


class StoryMessage():

    def __init__(self, story_screen, message,
                 background_x, background_y,
                 background_width, background_height,
                 font_size):
        self.story_screen = story_screen
        self.message = message
        self.background_x = background_x
        self.background_y = background_y
        self.background_width = background_width
        self.background_height = background_height
        self.font_size = font_size

    # инициализация вывода текста # требуется доработка

    def put_message(self):
        # именить на полупрозрачный вывод и добавить обработку вывода строки
        pygame.draw.rect(self.story_screen, sgl.STORY_BACKGROUND_COLOR,
                         pygame.Rect(self.background_x, self.background_y,
                                     self.background_width, self.background_height))
        story_font = pygame.font.SysFont(sgl.FONT, self.font_size)
        text = story_font.render(self.message, True, sgl.STORY_MESSAGE_COLOR)
        x = self.background_x + self.background_width // 2 - text.get_width() // 2
        y = self.background_y + self.background_height // 2 - text.get_height() // 2
        self.story_screen.blit(text, (x, y))
        pygame.display.flip()


# отладка модуля

if __name__ == '__main__':
    mess = "Мой дядя самых честных правил"
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.draw.rect(screen, (100, 100, 0), pygame.Rect(0, 0, 400, 600))
    story_message = StoryMessage(screen, mess, 100, 300,
                             600, 100, 20)
    done = False
    while not done:

        story_message.put_message()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

    pygame.quit()
