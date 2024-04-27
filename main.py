# S.G. Mikhaylov

# вариант главного модуля новеллы
# инициализирует основные переменные и осуществляет управление между сценами новеллы
# каждая сцена (отдельный класс) содержит своё управление событиями (отдельный класс)
#

# Импорт игровой библиотеки
import pygame

# импорт модулей новеллы
import story_globals as sgl
import story_events as sev
import story_messages as sm     # требуется доработка
import story_sounds as snd      # требуется доработка
import story_scenes as ssc      # требуется доработка

# инициализация базы # требуется доработка

# Инициализация pygame
pygame.init()
if not pygame.get_init():
  print('Bad initialization of the game library')

# инициализация экранов сцен # требуется доработка
# инициализация изображений # требуется доработка

# Установки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# заголовок окна программы
pygame.display.set_caption("The Story of the Lighthouse")
# инициализация таймера
clock = pygame.time.Clock()

sound_story = snd.StorySound('Story_sound.mp3')
sound_story.sound_on()

# Основной цикл сцены новеллы

events = sev.Story_events(0)
current_scene = ssc.StoryScene(0)   # вход в программу
scene_story = 0

running = True
while running:

    scene_story = current_scene.do_scene(scene_story)   # проигрывание истории

    for event in sev.events():
        if event == sgl.QUIT_STORY_WITH_SAVING:
            running = False
        elif event == sgl.QUIT_STORY_WITHOUT_SAVING:
            scene_story = sgl.SCENE_QUIT_STORY_WITHOUT_SAVING_ID   # ID начальной сцены для следующей загрузки программы
            running = False
        elif event == sgl.HELP_STORY:
            scene_story = sgl.SCENE_HELP_STORY_ID        # ID сцены HELP
        elif event == sgl.ABOUT_STORY:
            scene_story = sgl.SCENE_ABOUT_STORY_ID       # ID сцены 'о программе'
        elif event == sgl.START_STORY:
            scene_story = sgl.SCENE_START_STORY_ID       # ID первой сцены новеллы
        elif event == sgl.CONTINUE_STORY:
            # чтение запомненного ID текущей сцены из БД
            scene_story = sgl.SCENE_CONTINUE_STORY_ID    # ID запомненной сцены
        elif event == sgl.CONTINUE_STORY:
            # чтение запомненного ID предыдущей сцены из БД
            scene_story = sgl.SCENE_PREVIOUS_STORY_ID    # ID запомненной сцены


# закрытие БД       # требуется доработка
# закрытие файлов   # требуется доработка

# выключение звука
sound_story.sound_off()

# Завершение работы pygame
clock.tick(sgl.STORY_FPS)
pygame.quit()

