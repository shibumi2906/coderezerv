import pygame
import sys
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Вывод текста по буквам и перенос строк в Pygame')

font = pygame.font.Font(None, 36)
text = "Пример текста для вывода по буквам с переноример текста для вывода по буквам с переносом строкиример текста для вывода по буквам с переносом строкисом строки"
words = text.split()

clock = pygame.time.Clock()

x, y = 10, 10
for word in words:
    for char in word:
        text_surface = font.render(char, True, (255, 255, 255))
        screen.blit(text_surface, (x, y))
        pygame.display.flip()
        clock.tick(20)  # Задержка в миллисекундах
        x += text_surface.get_width()
    x += font.size(' ')[0]  # Учитываем пробел между словами
    if x > width - 10:
        x = 10
        y += font.get_linesize()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()