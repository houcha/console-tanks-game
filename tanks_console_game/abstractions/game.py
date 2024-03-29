"""Game module"""

from tanks_console_game.objects import field
from tanks_console_game.configs import gamename
from collections import defaultdict


class Game:
    def __init__(self):
        self.field = None
        self.main_player = None
        self.players = dict()
        # dict {type --> list_of_objects}
        # every object meets once in object_types' bypass while in object_groups it might locate in different groups
        self.classes = defaultdict(list)
        self.groups = {gamename.HEALTH_OBJECTS: list(),
                       gamename.MOVE_OBJECTS: list()}

    def create_field(self, width, height):
        self.field = field.Field(width, height)

    def draw_objects(self):
        for obj in self.objects_array():
            self.field.draw_object(obj)

    def add_player(self, player):
        self.main_player = player
        self.players[player.name] = player

    def add_bot(self, bot):
        self.players[bot.name] = bot

    def objects_array(self):
        for object_list in self.classes.values():
            for obj in object_list:
                yield obj
