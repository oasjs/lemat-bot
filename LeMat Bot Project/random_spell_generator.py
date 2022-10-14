import random
import json

class Lemat:
    def __init__(self):
        self.__list_level = 0      # This determines the level of access to the lists of spells
        self.__spell_list = []      # This is the list of spells that the Lemat generated last long rest

        with open("wild_spell_table.json", "r", encoding='utf-8') as f:
            self.__spell_table = json.load(f) # This is the table of spells that the Lemat can pull from


    @property
    def list_level(self):
        return self.__list_level

    @list_level.setter
    def list_level(self, value: int):
        if value in range(0, 5) and isinstance(value, int):
            self.__list_level = value
            return f'List level set to {value}.'
        else:
            return f'Invalid list level.'

    @property
    def spell_list(self) -> list: 
        return self.__spell_list

    def get_spell_list(self):
        for i, level in enumerate(self.__spell_table):
            if i <= self.__list_level:
                spells = random.sample(self.__spell_table[level], 2)
                self.__spell_list.append(spells)

lemat = Lemat()
lemat.get_spell_list()
print(lemat.spell_list)