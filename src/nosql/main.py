import json

from src.nosql.parser import parse_planeswalker_abilities, parse_sacrifice_ability, parse_equip_ability

if __name__ == '__main__':
    with open("../../data/AtomicCards.json") as f:
        data = json.load(f)["data"]

    for name, value in data.items():
        for card in value:
            card["abilities"] = []
            if "Planeswalker" in card["types"]:
                card["abilities"].extend(parse_planeswalker_abilities(card["text"]))
            if "text" in card:
                sacrifice = parse_sacrifice_ability(card["text"])
                if sacrifice:
                    card["abilities"].append(sacrifice)
                equip = parse_equip_ability(card["text"])
                if equip:
                    card["abilities"].append(equip)

            if not card["abilities"]:
                del card["abilities"]

            if "power" in card:
                card["power"] = int(card["power"]) if card["power"].isnumeric() else 0
            if "toughness" in card:
                card["toughness"] = int(card["toughness"]) if card["toughness"].isnumeric() else 0
            if "defense" in card:
                card["toughness"] = int(card["defense"]) if card["defense"].isnumeric() else 0
                del card["defense"]

    with open("../../data/Mongo.json", "w") as f:
        for value in data.values():
            for card in value:
                json.dump(card, f)
                f.write("\n")
