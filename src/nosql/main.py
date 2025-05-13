import json

if __name__ == '__main__':
    with open("../../data/AtomicCards.json") as f:
        data = json.load(f)["data"]

    for name, value in data.items():
        for card in value:
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
