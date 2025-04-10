import json
import logging
from typing import Any

from peewee import IntegrityError

from parsers import parse_mana_cost, parse_planeswalker_abilities, parse_colors, parse_types, parse_supertypes, parse_subtypes, parse_characteristic
from tables import Card, db, ManaCost

logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def get_mana_cost_id(mana_cost: ManaCost):
    out = ManaCost.select(ManaCost.id).where(ManaCost.colorless == mana_cost.colorless,
                                             ManaCost.white == mana_cost.white,
                                             ManaCost.blue == mana_cost.blue,
                                             ManaCost.black == mana_cost.black,
                                             ManaCost.red == mana_cost.red,
                                             ManaCost.green == mana_cost.green,
                                             ManaCost.snow == mana_cost.snow).get()
    return out

def insert_planeswalker(_data: dict[str, Any]):
    mana_cost = parse_mana_cost(_data["mana_cost"])

    _card = Card(name = _data["name"], power = _data["power"], defense = _data["defense"], text = _data["text"], mana_cost = mana_cost, loyalty = _data["loyalty"])
    abilities = parse_planeswalker_abilities(_card, _data["text"])
    colors = parse_colors(_card, _data["colors"])
    types = parse_types(_card, _data["types"])
    supertypes = parse_supertypes(_card, _data["supertypes"])
    subtypes = parse_subtypes(_card, _data["subtypes"])

    mana_txn = False

    with db.atomic():
        try:
            print("MANA COST: ", mana_cost.save(force_insert = True))
            mana_txn = True
        except IntegrityError as err:
            if "mana_cost_k" not in str(err).lower():
                print(err)
                raise err
            else:
                print("MANA VALUE DUPLICATED")

    if not mana_txn:
        _card.mana_cost = get_mana_cost_id(mana_cost)

    with db.atomic():
        try:
            print("CARD: ", _card.save(force_insert = True))
            for _i, ability in enumerate(abilities, 1):
                print(f"ABILITY {_i}: ", ability.save(force_insert = True))
            for _i, color in enumerate(colors, 1):
                print(f"COLOR {_i}: ", color.save(force_insert = True))
            for _i, type_ in enumerate(types, 1):
                print(f"TYPE {_i}: ", type_.save(force_insert = True))
            for _i, subtype in enumerate(subtypes, 1):
                print(f"SUBTYPE {_i}: ", subtype.save(force_insert = True))
            for _i, supertype in enumerate(supertypes, 1):
                print(f"SUPERTYPE {_i}: ", supertype.save(force_insert = True))

        except IntegrityError as err:
            if "card_pk" not in str(err).lower():
                print(err)
                raise err
            else:
                print("CARD DUPLICATED")
def insert_creature(_data: dict[str, Any]):
    mana_cost = parse_mana_cost(_data["mana_cost"])

    _card = Card(name = _data["name"], power = _data["power"], defense = _data["defense"], text = _data["text"], mana_cost = mana_cost)
    characteristics = parse_characteristic(_card, _data["text"])
    colors = parse_colors(_card, _data["colors"])
    types = parse_types(_card, _data["types"])
    supertypes = parse_supertypes(_card, _data["supertypes"])
    subtypes = parse_subtypes(_card, _data["subtypes"])

    mana_txn = False

    with db.atomic():
        try:
            print("MANA COST: ", mana_cost.save(force_insert = True))
            mana_txn = True
        except IntegrityError as err:
            if "mana_cost_k" not in str(err).lower():
                print(err)
                raise err
            else:
                print("MANA VALUE DUPLICATED")

    if not mana_txn:
        _card.mana_cost = get_mana_cost_id(mana_cost)

    with db.atomic():
        try:
            print("CARD: ", _card.save(force_insert = True))
            for _i, characteristic in enumerate(characteristics, 1):
                print(f"CHARACTERISTIC {_i}: ", characteristic.save(force_insert = True))
            for _i, color in enumerate(colors, 1):
                print(f"COLOR {_i}: ", color.save(force_insert = True))
            for _i, type_ in enumerate(types, 1):
                print(f"TYPE {_i}: ", type_.save(force_insert = True))
            for _i, subtype in enumerate(subtypes, 1):
                print(f"SUBTYPE {_i}: ", subtype.save(force_insert = True))
            for _i, supertype in enumerate(supertypes, 1):
                print(f"SUPERTYPE {_i}: ", supertype.save(force_insert = True))

        except IntegrityError as err:
            if "card_pk" not in str(err).lower():
                print(err)
                raise err
            else:
                print("CARD DUPLICATED")

if __name__ == '__main__':
    data = json.load(open('AtomicCards.json'))
    print(len(data["data"]))

    for name, value in data["data"].items():
        for val in value:
            if "types" in val and "Planeswalker" in val["types"]:
                # print(val)
                card = { "name": val["faceName"] if "faceName" in val else name,
                         "power": 0,
                         "defense": 0,
                         "text": val["text"],
                         "mana_cost": val["manaCost"].replace("D", "") if "manaCost" in val else "",
                         "loyalty": int(val["loyalty"]) if "loyalty" in val and val["loyalty"] != "X" else 0,
                         "colors": val["colors"],
                         "subtypes": val["subtypes"] if "subtypes" in val else "",
                         "types": val["types"] if "types" in val else "",
                         "supertypes": val["supertypes"] if "supertypes" in val else "" }

                insert_planeswalker(card)
            elif "types" in val and "Creature" in val["types"]:
                card = {
                    "name": val["faceName"] if "faceName" in val else name,
                    "power": val["power"].replace("*", "0").replace("X", "0").replace("+", "") if "power" in val else 0,
                    "defense": val["defense"].replace("*", "0").replace("X", "0") if "defense" in val else 0,
                    "text": val["text"] if "text" in val else "",
                    "mana_cost": val["manaCost"] if "manaCost" in val else "",
                    "colors": val["colors"],
                    "subtypes": val["subtypes"] if "subtypes" in val else "",
                    "types": val["types"] if "types" in val else "",
                    "supertypes": val["supertypes"] if "supertypes" in val else "" }
                insert_creature(card)
