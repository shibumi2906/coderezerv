# -*- coding: utf-8 -*-
import pygame
import sys
import os
import time

class Story_messages():
    def __init__(self, scene_picture, hero_picture, hero_x, hero_y, message):
        self.scene_picture = pygame.transform.scale(pygame.image.load(scene_picture), (800, 600))
        self.hero_picture = pygame.transform.scale(pygame.image.load(hero_picture), (800, 600))
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.message = message

    def screen_blit(self, screen):
#Текст:
        text_color = (230, 230, 230)
        font = pygame.font.Font(None, 28)
        text_surface = font.render(self.message, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (40, 510)
#Подложка под текст:
        obj_surface = pygame.Surface((640, 140))
        obj_surface.fill((0, 0, 0))
        obj_surface.set_alpha(150)

        screen.blit(self.scene_picture, (0, 0))
        screen.blit(self.hero_picture, (self.hero_x, self.hero_y))
        screen.blit(obj_surface, (30, 500))
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

    # Получаем абсолютный путь к файлу звуковой дорожки
    sound_path = os.path.join(os.path.dirname(__file__), 'music', 'sound2.mp3')

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # Воспроизведение на повторении

    global message_index
    message_index = 0

    button_image = "images/forward_button.jpg"
    button = Button(670, 500, button_image, button_action)

    messages = [
        Story_messages('images/s001.png', 'images/p001.png', -300, 200, "Молодой журналист по имени Алекс"),
        Story_messages('images/s001.png', 'images/p001.png', -300, 200,
                       "прибывает в маленький прибрежный городок Хейвенбрук."),
        Story_messages('images/s001.png', 'images/p001.png', -300, 200,
                       "Цель его визита — написать статью о старом маяке, который"),
        Story_messages('images/s001.png', 'images/p001.png', -300, 200,
                       "служит известной достопримечательностью и объектом местных легенд."),
        Story_messages('images/s002.png', 'images/p001.png', -300, 100, "Встреча с продавцом на рынке, Эммой"),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "Добрый день! Я заметил, вы продаете самые свежие морепродукты в городе. Могу я задать вам пару вопросов?"),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "Конечно, спрашивайте, пока я упаковываю эти креветки."),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "Я здесь из-за маяка. Вы не знаете какие-то местные истории или легенды, связанные с ним?"),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "Ах, маяк! Да, есть одна старая легенда о призрачном свете, который видят моряки. Говорят, это душа старого сторожа, который до сих пор не может покинуть свою пост. Но это, конечно, просто байки."),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "Интересно... А как насчет людей, которые сейчас работают в маяке или знают о нем что-то еще?"),
        Story_messages('images/s002.png', 'images/p001.png', -300, 200,
                       "На самом деле, лучше всего спросить у Лиз, она часто бывает в маяке. Или у Марка, владельца кафе. Они могут рассказать вам больше."),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       "Встреча с местным художником, Карлом Алекс замечает Карла, рисующего пейзаж маяка на холсте недалеко от рынка."),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       " Здравствуйте! Ваша картина выглядит потрясающе. Вы часто рисуете маяк?"),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       "  Привет! Да, маяк всегда вдохновлял меня. Его история, атмосфера... этот символ надежды и покровительства для всех мореплавателей."),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       " Я пишу статью о маяке. Не поделитесь, что вас вдохновляет или какие вы слышали истории?"),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       " О, многое. Прежде всего, его неизменность и таинственность. По ночам, когда маяк светится, кажется, будто он живой. Но у меня сложилось впечатление, что там происходят странные вещи. К примеру, недавно один из сторожей, Том, пропал, так и не найден..."),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100, " Пропал? Это должно быть большой историей"),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100,
                       " а, это весьма загадочно. Многие старожилы перешептываются, но точно ничего не знают. Может быть, Марк или Лиз смогут рассказать вам подробнее."),
        Story_messages('images/s003.png', 'images/p001.png', -300, 100, " Спасибо, Карл. Ваша помощь очень ценна."),
        Story_messages('images/s004.png', 'images/p001.png', -300, 100,
                       "Посещение кафе Морской Бриз Взяв на заметку информацию, полученную от Эммы и Карла, Алекс направляется в кафе Морской Бриз для встречи с Марком, чтобы узнать больше о маяке и его тайнах.Алекс заходит в уютное кафе Морской Бриз, расположенное недалеко от порта."),
        Story_messages('images/s004.png', 'images/p004.png', 600, 400,
                       "Внутри царит приятная атмосфера: стены украшены морскими узлами и старинными картами. Алекса встретил владелец, мужчина лет пятидесяти, по имени Марк."),
        Story_messages('images/s004.png', 'images/p004.png', -300, 100,
                       "Здравствуйте! Я слышал, что ваше кафе — лучшее место в городе для кофе. Можно мне чашку капучино?"),
        Story_messages('images/s004.png', 'images/p004.png', 600, 400,
                       "Конечно, сейчас приготовлю. Вы новенький в Хейвенбруке? Не каждый день у нас здесь появляются лица извне."),
        Story_messages('images/s004.png', 'images/p001.png', -300, 100,
                       "Да, я журналист и пишу статью о местном маяке. Знаете что-нибудь интересное о нем?"),
        Story_messages('images/s004.png', 'images/p004.png', 600, 400,
                       " О, маяк! С ним связана целая история. Но недавно случилось что-то странное. Том, который долгие годы был сторожем маяка, пропал без вести."),
        Story_messages('images/s004.png', 'images/p001.png', -300, 100,
                       " Пропал? Это звучит тревожно. Не могли бы вы рассказать подробнее?"),
        Story_messages('images/s004.png', 'images/p004.png', 600, 400,
                       " Конечно. Том был очень надежным человеком. Каждый вечер зажигал маяк, и каждое утро гулял по берегу. Но однажды утром его не нашли дома. Его вещи остались на месте, дверь была не заперта..."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       " Алекс, наделенный решимостью, несмотря на предостережения местных жителей, решает отправиться к маяку , чтобы разгадать его тайны. Он приходит  на берег, где его ждет лодочник, чья роль, по-видимому, не ограничивается лишь перевозкой."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       " Добро пожаловать,молодой человек"),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       " К маяку,пожалуйста. Мне нужно туда срочно."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       " О, маяк? Вы уверены, что вам туда стоит идти? Многие говорят, что это  место проклято."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       "  Я уверен, что там есть что-то, что мне нужно узнать. Меня не остановят слухи и страхи."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       "По пути к маяку,Алекс вспоминает разговоры с разными жителями, которые давали ему различныекусочки информации о маяке и его странных происшествиях. Он вспоминает слова старика-еще одного из смотрителей маяка,  и другиерассказы, которые добавляли элементы лора и мистики в его восприятие места."),
        Story_messages('images/s005-1.png', 'images/p010.png', 1200, 600,
                       "По пути к маяку,Алекс вспоминает разговоры с разными жителями, которые давали ему различныекусочки информации о маяке и его странных происшествиях. Он вспоминает слова старика-еще одного из смотрителей маяка,  и другиерассказы, которые добавляли элементы лора и мистики в его восприятие места."),
        Story_messages('images/s022.png', 'images/p001.png', 1200, 600,
                       "Маяк - это не просто огни на берегу. В нем заключены века истории и морских легенд. Но будьте осторожны, молодой человек. Некоторые тайнылучше оставить нераскрытыми."),
        Story_messages('images/s006.png', 'images/p001.png', -300, 200,
                       " Вот и маяк. Будьтеосторожны там, молодой человек. Море скрывает множество тайн, и не все из нихприятны.Алекс, несмотря на заметное недоверие к лодочнику, решает действовать самостоятельно и начинает свое исследование маяка.."),
        Story_messages('images/s006-1.png', 'images/p001.png', -300, 200,
                       "  Алекс и Лиз встречауются у двери маяка."),
        Story_messages('images/s006-1.png', 'images/p001.png', -300, 200,
                       "Алекс -здравствуйте, меня зовут Алекс. "),
        Story_messages('images/s006-1.png', 'images/p001.png', -300, 200,
                       "Зачем ты приехал? Что  собираешься делать ? "),
        Story_messages('images/s006-1.png', 'images/p001.png', -300, 200,
                       "Алекс: Я... я решил добраться  сюда, чтобы разобраться в том, что произошло с Томом. Ты слышала про его исчезновение? "),
        Story_messages('images/s006-1.png', 'images/p001.png', -300, 200,
                       "Лиз: Да, это было удивительно странно. Многие говорят, что его унесло море во время бури, но я чувствую, что это не все, что произошло. "),
        Story_messages('images/s006-1.png', 'images/p001.png', -500, 200,
                       "Алекс: Том был надежным сторожем, я не могу поверить, что он просто исчез таким образом. Я слышал.... он пытался провести какую-то церемонию, что-то связанное с защитой маяка."),
        Story_messages('images/s006-1.png', 'images/p001.png', -500, 200,
                       " Лиз:Я тоже чувствую, что в этом есть что-то большее. Моя бабушка всегда говорила, что маяк скрывает много тайн."),
        Story_messages('images/s006-1.png', 'images/p001.png', -500, 200,
                       "Алекс:  Мы должны разобраться в этом. Я верю, что ответы находятся здесь, у маяка. "),
        Story_messages('images/s006-1.png', 'images/p001.png', -500, 200,
                       " Лиз:) Хорошо, давайте исследуем это вместе. Вдвоем мы сможем разгадать эту загадку и узнать, что на самом деле произошло с Томом и маяком."),
        Story_messages('images/s006-1.png', 'images/p001.png', -500, 200,
                       "Алекс: (улыбается) Да, давайте начнем сейчас. Вместе мы сильнее.Алекс и Лиз обмениваются решительными взглядами, готовые принять вызов и раскрыть тайны, скрытые в морских волнах и стенах древнего маяка. "),
        Story_messages('images/s007.png', 'images/p001.png', -500, 200,
                       "Проходя через дверь маяка, Алекс замечает, что внутри царит мрак и тишина. Его свет фонарика освещает узкие коридоры и каменные стены, словно молчаливых свидетелей веков.Алекс: (шепотом сам к себе) Здесь действительно что-то странное... "),
        Story_messages('images/s007.png', 'images/p008.png', 600, 400,
                       "Нам нужно больше узнать о маяке. И о том, что происходит здесь на самом деле. Моя бабушка была последним официальным хранителем маяка. Она всегда говорила, что в этом месте есть что-то большее, чем просто каменные стены. Я хочу узнать правду. "),
        Story_messages('images/s007.png', 'images/p001.png', -500, 400,
                       " Алекс: И я. Я чувствую, что здесь есть ответы на множество вопросов."),
        Story_messages('images/s007.png', 'images/p008.png', 600, 400,
                       "Лиз: Но будьте осторожны. В этом маяке есть опасности, о которых мы даже не подозреваем. "),
        Story_messages('images/s007.png', 'images/p001.png', -500, 400,
                       " Алекс: Я не боюсь. Я готов узнать правду, какой бы она ни была."),
        Story_messages('images/s007.png', 'images/p001.png', -500, 400,
                       " Алекс и Лиз обмениваются решительными взглядами, подтверждая свое решение продолжить исследование маяка. Несмотря на предостережения и мистические предчувствия, они двигаются вперед, готовые раскрыть тайны, скрытые в стенах этого древнего сооружения."),
        Story_messages('images/s008.png', 'images/p008.png', 600, 400,
                       "Во время обследования комнат и помещений маяка, Алекс и Лиз столкнулись с неожиданным препятствием. "),
        Story_messages('images/s008.png', 'images/p001.png', -500, 400,
                       "Пока они аккуратно проникали вглубь маяка, разгадывая его тайны, они наткнулись на старую, запечатанную дверь, которая казалась ведущей в неизвестные подземелья или таинственные пещеры под основанием маяка "),
        Story_messages('images/s009.png', 'images/p001.png', -500, 400,
                       " Алекс: (стоя на пороге перед дверью) Лиз, посмотри, что я нашел. Это выглядит как дверь во что-то древнее."),
        Story_messages('images/s009.png', 'images/p008.png', 600, 500,
                       "Лиз: (взглядывает на дверь, с удивлением) Да, это действительно интересно. Но... Я чувствую, что нам следует исследовать это вместе, вдвоем. Это может быть опасно. "),
        Story_messages('images/s009.png', 'images/p001.png', -500, 400,
                       "Алекс: (кивает) Ты права. Давайте вернемся сюда после того, как закончим обследование этажа. "),
        Story_messages('images/s010-1.png', 'images/p001.png', -500, 400,
                       "Несмотря на их решимость, Алекс и Лиз были вынуждены временно разделиться, чтобы эффективно исследовать разные части маяка. "),
        Story_messages('images/s010-1.png', 'images/p001.png', -500, 400,
                       "Алекс решил спуститься вниз, чтобы исследовать подземелья.Они договорились встретиться через некоторое время у двери, чтобы вместе исследовать то, что скрывалось за ней. "),
        Story_messages('images/s010-1.png', 'images/p001.png', -500, 400,
                       "Когда он достигает двери, вдруг начинается странный звук, словно глухой грохот, доносящийся из глубины моря. Сердце Алекса начинает биться сильнее, но его решимость не ослабевает. С силой он прикладывает руку к двери, и внезапно она медленно открывается перед ним. "),
        Story_messages('images/s010-1.png', 'images/p001.png', -500, 400,
                       "Смело шагая вперед, он вдруг ощущает, как земля под ногами начинает дрожать, а стены коридора начинают излучать мистический свет. Он понимает, что попал во что-то невероятное, что скрывалось в глубинах маяка, и что его ждет что-то за пределами его воображения. "),
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

            # words = messages[message_index].message.split()
            # # message_item = messages[message_index]
            # # print(message_item)
            # print(words)


            messages[message_index].screen_blit(screen)

        button.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()

