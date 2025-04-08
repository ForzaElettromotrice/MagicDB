import json
from typing import AnyStr

from parsers import parse_mana_cost, parse_planeswalker_abilities, parse_colors, parse_types, parse_supertypes, parse_subtypes
from tables import Card

def insert_planeswalker(_data: dict[str, AnyStr]):
    mana_cost = parse_mana_cost(_data["mana_cost"])

    _card = Card(name = _data["name"], power = _data["power"], defense = _data["defense"], text = _data["text"], mana_cost = mana_cost, loyalty = _data["loyalty"])
    abilities = parse_planeswalker_abilities(_card, _data["text"])
    colors = parse_colors(_card, _data["colors"])
    types = parse_types(_card, _data["types"])
    supertypes = parse_supertypes(_card, _data["supertypes"])
    subtypes = parse_subtypes(_card, _data["subtypes"])

    print(mana_cost.__repr__())
    mana_cost.save()

if __name__ == '__main__':
    data = json.load(open('/home/f3m/Documents/AtomicCards.json'))
    data2 = json.load(open('/home/f3m/Documents/AtomicCards.backup.json'))
    print(len(data["data"]))

    for name, value in data["data"].items():
        for i, val in enumerate(value):
            if "types" in val and "Planeswalker" in val["types"]:
                # print(val)
                card = { "name": val["faceName"] if "faceName" in val else name,
                         "power": 0,
                         "defense": 0,
                         "text": val["text"],
                         "mana_cost": val["manaCost"] if "manaCost" in val else "",
                         "loyalty": int(data2["data"][name][i]["loyalty"]) if "loyalty" in data2["data"][name][i] and data2["data"][name][i]["loyalty"] != "X" else 0,
                         "colors": val["colors"],
                         "subtypes": val["subtypes"] if "subtypes" in val else "",
                         "types": val["types"] if "types" in val else "",
                         "supertypes": val["supertypes"] if "supertypes" in val else "" }

                insert_planeswalker(card)
