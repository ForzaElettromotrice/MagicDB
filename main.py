import json
import logging
from typing import Any

from peewee import IntegrityError

from parsers import parse_mana_cost, parse_planeswalker_abilities, parse_colors, parse_types, parse_supertypes, parse_subtypes, parse_characteristic, parse_sacrifice_ability, parse_equip_ability
from tables import Card, db, ManaCost, DoubleCard, MeldCard

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
def insert_non_planeswalker(_data: dict[str, Any]):
    mana_cost = parse_mana_cost(_data["mana_cost"])

    _card = Card(name = _data["name"], power = _data["power"], defense = _data["defense"], text = _data["text"], mana_cost = mana_cost)
    characteristics = parse_characteristic(_card, _data["text"])
    colors = parse_colors(_card, _data["colors"])
    types = parse_types(_card, _data["types"])
    supertypes = parse_supertypes(_card, _data["supertypes"])
    subtypes = parse_subtypes(_card, _data["subtypes"])
    sacrifice_ability = parse_sacrifice_ability(_card, _data["text"])
    equip_cost, equip_ability = parse_equip_ability(_card, _data["text"])

    mana_txn = False
    equip_mana_txn = False

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
    if equip_cost is not None:
        with db.atomic():
            try:
                print("EQUIP COST: ", equip_cost.save(force_insert = True))
                equip_mana_txn = True
            except IntegrityError as err:
                if "mana_cost_k" not in str(err).lower():
                    print(err)
                    raise err
                else:
                    print("EQUIP COST DUPLICATED")

    if not mana_txn:
        _card.mana_cost = get_mana_cost_id(mana_cost)

    if not equip_mana_txn and equip_cost is not None:
        equip_ability.mana_cost = get_mana_cost_id(equip_cost)

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
            if sacrifice_ability is not None:
                print("SACRIFICE ABILITY: ", sacrifice_ability.save(force_insert = True))
            if equip_ability is not None:
                print("EQUIP ABILITY: ", equip_ability.save(force_insert = True))

        except IntegrityError as err:
            if "card_pk" not in str(err).lower():
                print(err)
                raise err
            else:
                print("CARD DUPLICATED")
def insert_double_face(_name: str):
    names = _name.split(" // ")

    first = DoubleCard(name = names[0], subface = names[1])
    second = DoubleCard(name = names[1], subface = names[0])

    with db.atomic():
        try:
            print("DOUBLE CARD 1: ", first.save(force_insert = True))
            print("DOUBLE CARD: 2: ", second.save(force_insert = True))
        except IntegrityError as err:
            if "double_card_pk" not in str(err).lower():
                print(err)
                raise err
            else:
                print("DOUBLE CARD DUPLICATED")
def insert_melds():
    """Argoth, Sanctum of Nature // Titania, Gaea Incarnate
Brisela, Voice of Nightmares
Bruna, the Fading Light // Brisela, Voice of Nightmares
Chittering Host
Gisela, the Broken Blade // Brisela, Voice of Nightmares
Graf Rats // Chittering Host
Hanweir Battlements // Hanweir, the Writhing Township
Hanweir Garrison // Hanweir, the Writhing Township
Hanweir, the Writhing Township
Midnight Scavengers // Chittering Host
Mishra, Claimed by Gix // Mishra, Lost to Phyrexia
Mishra, Lost to Phyrexia
Phyrexian Dragon Engine // Mishra, Lost to Phyrexia
The Mightstone and Weakstone // Urza, Planeswalker
Titania, Gaea Incarnate
Titania, Voice of Gaea // Titania, Gaea Incarnate
Urza, Lord Protector // Urza, Planeswalker
Urza, Planeswalker"""
    with db.atomic():
        try:
            MeldCard(name = "Argoth, Sanctum of Nature", first = "Titania, Gaea Incarnate").save(force_insert = True)
            MeldCard(name = "Titania, Voice of Gaea", first = "Titania, Gaea Incarnate").save(force_insert = True)
            MeldCard(name = "Titania, Gaea Incarnate", first = "Argoth, Sanctum of Nature", second = "Titania, Voice of Gaea").save(force_insert = True)

            MeldCard(name = "Bruna, the Fading Light", first = "Brisela, Voice of Nightmares").save(force_insert = True)
            MeldCard(name = "Gisela, the Broken Blade", first = "Brisela, Voice of Nightmares").save(force_insert = True)
            MeldCard(name = "Brisela, Voice of Nightmares", first = "Bruna, the Fading Light", second = "Gisela, the Broken Blade").save(force_insert = True)

            MeldCard(name = "Midnight Scavengers", first = "Chittering Host").save(force_insert = True)
            MeldCard(name = "Graf Rats", first = "Chittering Host").save(force_insert = True)
            MeldCard(name = "Chittering Host", first = "Midnight Scavengers", second = "Graf Rats").save(force_insert = True)

            MeldCard(name = "Hanweir Battlements", first = "Hanweir, the Writhing Township").save(force_insert = True)
            MeldCard(name = "Hanweir Garrison", first = "Hanweir, the Writhing Township").save(force_insert = True)
            MeldCard(name = "Hanweir, the Writhing Township", first = "Hanweir Battlements", second = "Hanweir Garrison").save(force_insert = True)

            MeldCard(name = "Mishra, Claimed by Gix", first = "Mishra, Lost to Phyrexia").save(force_insert = True)
            MeldCard(name = "Phyrexian Dragon Engine", first = "Mishra, Lost to Phyrexia").save(force_insert = True)
            MeldCard(name = "Mishra, Lost to Phyrexia", first = "Mishra, Claimed by Gix", second = "Phyrexian Dragon Engine").save(force_insert = True)

            MeldCard(name = "Urza, Lord Protector", first = "Urza, Planeswalker").save(force_insert = True)
            MeldCard(name = "The Mightstone and Weakstone", first = "Urza, Planeswalker").save(force_insert = True)
            MeldCard(name = "Urza, Planeswalker", first = "Urza, Lord Protector", second = "The Mightstone and Weakstone").save(force_insert = True)

        except Exception as err:
            print(err)
            raise err

if __name__ == '__main__':
    data = json.load(open('AtomicCards.json'))
    print(len(data["data"]))

    for name, value in data["data"].items():
        for val in value:
            if "types" in val and "Planeswalker" in val["types"]:
                card = { "name": val["faceName"] if "faceName" in val else name,
                         "power": 0,
                         "defense": 0,
                         "text": val["text"],
                         "mana_cost": val["manaCost"] if "manaCost" in val else "",
                         "loyalty": int(val["loyalty"]) if "loyalty" in val and val["loyalty"] != "X" else 0,
                         "colors": val["colorIdentity"],
                         "subtypes": val["subtypes"] if "subtypes" in val else "",
                         "types": val["types"] if "types" in val else "",
                         "supertypes": val["supertypes"] if "supertypes" in val else "" }

                insert_planeswalker(card)
            else:
                card = {
                    "name": val["faceName"] if "faceName" in val else name,
                    "power": val["power"].replace("?", "0").replace("*", "0").replace("+", "").replace("-", "") if "power" in val else 0,
                    "defense": val["defense"].replace("?", "0").replace("*", "0").replace("+", "").replace("-", "") if "defense" in val else (val["toughness"].replace("*", "0").replace("?", "0").replace("+", "").replace("-", "") if "toughness" in val else 0),
                    "text": val["text"] if "text" in val else "",
                    "mana_cost": val["manaCost"].replace("{D}", "").replace("{L}", "") if "manaCost" in val else "",
                    "colors": val["colorIdentity"],
                    "subtypes": val["subtypes"] if "subtypes" in val else "",
                    "types": val["types"] if "types" in val else "",
                    "supertypes": val["supertypes"] if "supertypes" in val else ""
                }
                insert_non_planeswalker(card)

    for name, value in data["data"].items():
        for val in value:
            if "layout" in val and "adventure" in val["layout"]:
                insert_double_face(name)

    insert_melds()
