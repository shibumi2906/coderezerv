import pygame
import sys

class StoryScene():
    def __init__(self, background_image, options):
        self.background_image = pygame.image.load(background_image)
        self.options = options  # Список кнопок с вариантами ответов

    def render(self, screen):
        screen.blit(self.background_image, (0, 0))
        for option in self.options:
            option.draw(screen)

class OptionButton():
    def __init__(self, x, y, text, action):
        self.image = pygame.Surface((200, 50))
        self.image.fill((0, 0, 128))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, text_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

def option_action_1():
    print("Option 1 selected")
    # Добавить сценарий для первого выбора

def option_action_2():
    print("Option 2 selected")
    # Добавить сценарий для второго выбора

def option_action_3():
    print("Option 3 selected")
    # Добавить сценарий для третьего выбора

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Визуальная Новелла")

    options = [
        OptionButton(300, 200, "Option 1", option_action_1),
        OptionButton(300, 300, "Option 2", option_action_2),
        OptionButton(300, 400, "Option 3", option_action_3)
    ]
    scene = StoryScene('path/to/your/background.jpg', options)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for option in options:
                option.handle_event(event)

        screen.fill((0, 0, 0))
        scene.render(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
