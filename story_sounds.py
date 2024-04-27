# Юрий, S.G. Mikhaylov
# 27/04 15:00 ГОТОВ

# организует и осуществляет вывод и остановку звукового сопровождения во время исполнеия новеллы
# звук один на всем протяжении новеллы проигрывается по кольцу до команды остановки
# - инициализация звукового сопровождения
# - запуск звука
# - остановка звука

import story_globals as sgl
import story_messages as sms
import pygame


class StorySound():

    def __init__(self, sound_file):
        # Инициализация библиотеки pygame и её компонентов для работы со звуком
        pygame.init()
        pygame.mixer.init()
        # Загрузка звукового файла
        self.sound = pygame.mixer.Sound(sound_file)

    def sound_on(self):
        # запуск воспроизведения звука в бесконечном режиме
        self.sound.play(loops=-1)

    def sound_off(self):
        # остановка воспроизведения звука
        self.sound.stop()


# отладка модуля

if __name__ == '__main__':

    sound_story = StorySound(sgl.STORY_SOUND)
    sound_story.sound_on()

    # простейший цикл игры
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    mess = "Мой дядя самых честных правил"
    story_message = sms.StoryMessage(screen, mess, 100, 300, 600, 100, 20)

    while not done:
        story_message.put_message()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

    sound_story.sound_off()
    pygame.quit()
