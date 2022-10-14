import json
import re

wild_spell_table = {
    "first": [],
    "second": [],
    "third": [],
    "fourth": [],
    "fifth": []
}

spells = []
counter = 0

with open("./unformatted_spells.txt", "r") as f:
    spell_list = f.read().splitlines()
    for spell in spell_list:
        if spell == '':
            counter += 1
            continue

        spell = re.split('1|2|3|4|5', spell)

        if counter == 0:
            wild_spell_table["first"].append(spell[0])
        elif counter == 1:
            wild_spell_table["second"].append(spell[0])
        elif counter == 2:
            wild_spell_table["third"].append(spell[0])
        elif counter == 3:
            wild_spell_table["fourth"].append(spell[0])
        elif counter == 4:
            wild_spell_table["fifth"].append(spell[0])

with open('wild_spell_table.json', 'w') as f:
    json.dump(wild_spell_table, f, indent=4)
    print(f)
