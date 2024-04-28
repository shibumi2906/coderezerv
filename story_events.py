# S.G. Mikhaylov
# 27/04 15:00 ГОТОВ

import story_globals as sgl

# класс событий новеллы
def events():
    return [sgl.QUIT_STORY_WITHOUT_SAVING,
            sgl.QUIT_STORY_WITH_SAVING,
            sgl.HELP_STORY,
            sgl.ABOUT_STORY,
            sgl.START_STORY,
            sgl.CONTINUE_STORY]

class StoryEvents():

    def __init__(self, scene_story):
        self.scene_story = scene_story

    def set_story(self, current_story):
        self.scene_story = current_story

    def get_story(self):
        return self.scene_story

# Создаем экземпляр класса Constants
# events_obj = Story_events(0)
# Получаем список констант
# print('список констант ', events_obj.get_events())
#  Получаем ID истории
# print('ID истории ', events_obj.get_story())
