import pygame
import sys
import os

class Story_messages():
    def __init__(self, scene_picture, hero_picture, hero_x, hero_y, message):
        self.scene_picture = pygame.image.load(scene_picture)
        self.hero_picture = pygame.image.load(hero_picture)
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.message = message

    def screen_blit(self, screen):
        text_color = (230, 230, 230)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.message, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (100, 550)

        obj_surface = pygame.Surface((600, 100))
        obj_surface.fill((0, 0, 0))
        obj_surface.set_alpha(150)

        screen.blit(self.scene_picture, (0, 0))
        screen.blit(self.hero_picture, (self.hero_x, self.hero_y))
        screen.blit(obj_surface, (50, 500))
        screen.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y, image_path, action):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.action()

def button_action():
    global message_index
    message_index += 1  # Transition to the next message on button press

def main_loop():
    pygame.init()
    pygame.mixer.init()  # Инициализация микшера для работы со звуком
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Визуальная Новелла 'Тайны Старого Маяка'")

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(-1)  # Воспроизведение на повторении

    global message_index
    message_index = 0

    button_image = "images/forward_button.jpg"
    button = Button(650, 530, button_image, button_action)

    messages = [
        Story_messages('images/s001.png', 'images/p001.png', -300, 200, "Молодой журналист по имени Алекс"),
        # Добавьте другие сообщения по аналогии
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button.handle_event(event)

        screen.fill((0, 0, 0))
        if message_index < len(messages):
            messages[message_index].screen_blit(screen)

        button.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
