from enums import types, supertypes, subtypes, activable_characteristics, attack_characteristics, constant_characterstics, triggerable_characteristics
from tables import ManaCost, ActivableAbility, Card, Colors, Types, Supertypes, Subtypes, ActivableCharacteristics, AttackCharacteristics, ConstantCharacteristics, TriggerableCharacteristics

def parse_mana_cost(mana_cost: str):
    if mana_cost == "":
        return ManaCost(colorless = 0, red = 0, blue = 0, green = 0, black = 0, white = 0, snow = 0)
    start = 0
    for i, c in enumerate(mana_cost):
        if c != "{":
            continue
        start = i
        break
    mana_cost = mana_cost[start + 1:]

    mana = mana_cost.split("}{")
    if mana[-1][-1] == "}":
        mana[-1] = mana[-1][:-1]

    mana_cost = ManaCost(colorless = 0, red = 0, blue = 0, green = 0, black = 0, white = 0, snow = 0)

    for elm in mana:
        if "/" in elm:
            parts = elm.split("/")
            if "P" not in parts or len(parts) != 2:
                for part in parts:
                    match part:
                        case "R":
                            mana_cost.red += 0.5
                        case "U":
                            mana_cost.blue += 0.5
                        case "G":
                            mana_cost.green += 0.5
                        case "B":
                            mana_cost.black += 0.5
                        case "W":
                            mana_cost.white += 0.5
                        case "P":
                            pass
                continue
            elm = parts[0]
        match elm:
            case "R":
                mana_cost.red += 1
            case "U":
                mana_cost.blue += 1
            case "G":
                mana_cost.green += 1
            case "B":
                mana_cost.black += 1
            case "W":
                mana_cost.white += 1
            case "S":
                mana_cost.snow += 1
            case "C":
                mana_cost.colorless += 1
            case _:
                mana_cost.colorless = 0 if elm == "X" else int(elm)
    return mana_cost
def parse_planeswalker_abilities(name: Card, text: str):
    out = []
    text = text.split("\n")

    for elm in text:
        if elm[0] != "[":
            continue
        elm = elm.split(":")[0]
        out.append(ActivableAbility(name = name, loyalty = int(elm[1:-1].replace("−", "-").replace("X", "0"))))
    return out
def parse_colors(name: Card, _colors: list[str]):
    out = []
    for color in _colors:
        match color:
            case "R":
                out.append(Colors(name = name, color = "Red"))
            case "U":
                out.append(Colors(name = name, color = "Blue"))
            case "G":
                out.append(Colors(name = name, color = "Green"))
            case "B":
                out.append(Colors(name = name, color = "Black"))
            case "W":
                out.append(Colors(name = name, color = "White"))
    return out
def parse_types(name: Card, _types: list[str]):
    out = []
    for type_ in _types:
        if type_ not in types:
            continue
        out.append(Types(name = name, type = type_))
    return out
def parse_supertypes(name: Card, _supertypes: list[str]):
    out = []
    for supertype in _supertypes:
        if supertype not in supertypes:
            continue
        out.append(Supertypes(name = name, supertype = supertype))
    return out
def parse_subtypes(name: Card, _subtypes: list[str]):
    out = []
    for subtype in _subtypes:
        if subtype not in subtypes:
            continue
        out.append(Subtypes(name = name, subtype = subtype))
    return out

def parse_characteristic(name: Card, text: str):
    out = []
    if text == "":
        return out

    for characteristic in activable_characteristics:
        if characteristic in text:
            out.append(ActivableCharacteristics(name = name, characteristic = characteristic))

    for characteristic in attack_characteristics:
        if characteristic in text:
            out.append(AttackCharacteristics(name = name, characteristic = characteristic))

    for characteristic in constant_characterstics:
        if characteristic in text:
            out.append(ConstantCharacteristics(name = name, characteristic = characteristic))

    for characteristic in triggerable_characteristics:
        if characteristic in text:
            out.append(TriggerableCharacteristics(name = name, characteristic = characteristic))

    return out
def parse_sacrifice_ability(name: Card, text: str):
    if "Sacrifice this" in text or "Sacrifice another" in text:
        return ActivableAbility(name = name, sacrifice = True)

def parse_equip_ability(name: Card, text: str):
    if "Equip {" in text:
        text = text.split("Equip {")[1][:2]
        if text[1] == "}":
            text = text[0]
        mana_cost = ManaCost(colorless = int(text), red = 0, blue = 0, green = 0, black = 0, white = 0, snow = 0)
        return mana_cost, ActivableAbility(name = name, mana_cost = mana_cost)
    return None, None
