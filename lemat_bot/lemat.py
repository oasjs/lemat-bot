import random
import json

class Lemat:
    def __init__(self):
        self.__list_level = 5 # Determines the level of access to the lists of spells

        with open("wild_spell_table.json", "r", encoding='utf-8') as f:
            self.__spell_table = json.load(f) # Table of spells that Lemat can pull from


    @property
    def list_level(self) -> int:
        return self.__list_level

    @list_level.setter
    def list_level(self, value: int):
        try:
            if value in range(1, 6):
                self.__list_level = value
                return f'List level set to {value}.'
            else:
                return 'List level must be between 1 and 5.'
        except TypeError:
            return 'List level must be an integer.'
            
    # Returns a list of tuples containing a pair of spells of the same level
    def __get_spell_list(self) -> list:

        spell_list = []
        for i, level in enumerate(self.__spell_table):
            if i <= self.__list_level:
                spells = random.sample(self.__spell_table[level], 2)
                spell_list.append(spells)
            else:
                break

        return spell_list

    # Returns a string of the spell list to be sent on chat
    def formatted_spell_list(self) -> str:
        table_content = '**Wild Spell Table:**\n'
        for i, pair in enumerate(self.__get_spell_list()):
            table_content += f'{i+1} - {pair[0]}, {pair[1]}\n'

        return table_content
