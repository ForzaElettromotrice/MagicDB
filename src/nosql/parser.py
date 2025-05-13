def parse_planeswalker_abilities(text: str) -> list[dict[str:str]]:
    out = []
    text = text.split("\n")

    for elm in text:
        if elm[0] != "[":
            continue
        elm = elm.split(":")[0]
        out.append({ "cost": int(elm[1:-1].replace("−", "-").replace("X", "0")) })
    return out

def parse_sacrifice_ability(text: str) -> dict[str:str]:
    if "Sacrifice this" in text or "Sacrifice another" in text:
        return { "cost": "Sacrifice" }

def parse_equip_ability(text: str):
    if "Equip {" not in text:
        return
    text = text.split("Equip ")[1].replace("\n", " ").split(" ")[0]

    return { "cost": text }
