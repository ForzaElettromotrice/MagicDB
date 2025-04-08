from tables import ManaCost, ActivableAbility, Card, Colors, Types, Supertypes, Subtypes

types = { 'Artifact', 'Creature', 'Enchantment', 'Instant', 'Land', 'Planeswalker', 'Kindred', 'Tribal', 'Sorcery', 'World' }
supertypes = { 'Base', 'Snow', 'Legendary' }
subtypes = { 'Otter', 'Gobakhan', 'Omenpath', 'Chicken', 'Possum', 'Sloth', 'Domri', 'Hamster', 'sECreT', 'Donkey', 'Art', 'Aurochs', 'Homunculus', 'Aetherborn', 'Walrus', 'Ikoria', 'Mountain', 'Slug', 'Spy', 'Tasha', 'Brushwagg', 'Gremlin', 'Hag', 'Mercadia', 'Fire', 'Will', 'Fungus', 'Arkhos', 'Cave', 'Spuzzem', 'Beast', 'Daretti', 'Elder', 'Devil', 'Quintorius', 'Rabbit', 'Surrakar', 'Brainiac', 'Elves', 'Serra’s Realm', 'Kinshala', 'Fractal', 'Champion', 'Ashiok', 'Townsfolk', 'Cartouche', 'Darillium', 'Mirrodin', 'Gus', 'Advisor', 'Ape', 'Lamia', 'Nautilus', 'Kaldheim', 'Elk', 'Szat', 'Lesson', 'Narset', 'Coyote', 'Dryad', 'Sarkhan', 'Homarid', 'Kylem', 'Mount', 'Nahiri', 'Nightstalker', 'Tree', 'Pyrulea', 'Theros', 'Ouphe', 'Bloomburrow', 'Ir', 'Spike', 'Shark', 'Chandra', 'Toy', 'Etiquette', 'Kangaroo', 'Davriel', 'Moonfolk', 'Frog', 'Mole', 'Human?', 'Hyena', 'Drone', 'Giant', 'Bard', 'Liliana', 'Antausia', 'Master', 'Sphinx', 'Leviathan', 'Nymph', 'Saheeli', 'Bolas', 'Deb',
             'Zendikar', 'Eldraine', 'Zhalfir', 'Elminster', 'Wanderer', 'Mission', 'Shrine', 'Kandoka', 'Swamp', 'Ravnica', 'Alara', 'Tiefling', 'Mite', 'Kobold', 'Lhurgoyf', 'Fabacin', 'Ally', 'Contraption', 'Moon', 'Byode', 'Svega', 'Dog', 'New Earth', 'Room', 'Siege', 'Mouse', 'Snake', 'Hawk', 'Minotaur', 'Iquatana', 'Kraken', 'Deer', 'Pirate', 'Alien', 'Huatli', 'Antelope', 'Bringer', 'Fiora', 'Robot', 'Hatificer', 'Thunder Junction', 'Mongseng', 'Clown', 'Dragon', 'Tyranid', 'Snail', 'Jared', 'Shade', 'Teyo', 'Rowan', 'Artist', 'Ferret', 'Armadillo', 'Monger', 'Yanling', 'Vampire', 'Chameleon', 'Urza', 'Jellyfish', 'Vronos', 'Teferi', 'Elf', 'Beaver', 'Estrid', 'Jaya', 'Class', 'Salamander', 'Valla', 'Serra', 'Unicorn', 'Masticore', 'Fortification', 'Efreet', 'Grist', 'Cat', 'Praetor', 'Bureaucrat', 'Kor', 'Archon', 'Oko', 'Hydra', 'Mystic', 'Pegasus', 'Ugin', 'Cyborg', 'Rath', 'Segovia', 'Rhino', 'Trenzalore', 'Point', 'Lobster', 'Dovin', 'Gnoll', 'Urza''s', 'Glimmer', 'Curse',
             'and/or', 'Alicorn', 'Wraith', 'Elephant', 'Pilot', 'Athlete', 'Gorgon', 'Adventure', 'Citizen', 'Thrull', 'Licid', 'Gnome', 'Plains', 'Dalek', 'Scarecrow', 'Splinter', 'Pangolin', 'Shapeshifter', 'Carrier', 'Food', 'Assembly-Worker', 'Turtle', 'Yanggu', 'Plant', 'Phyrexian', 'Centaur', 'Autobot', 'Serpent', 'Seal', 'Octopus', 'Abian', 'Performer', 'Synth', 'Ulamog''s', 'Warrior', 'of', 'Eldrazi', 'Karn', 'Drake', 'Apalapucia', 'Arlinn', 'Weasel', 'Shadowmoor', 'Moag', 'Cephalid', 'Nixilis', 'Merfolk', 'Cyclops', 'Slith', 'Druid', 'Yeti', 'Skeleton', 'Kithkin', 'Sorin', 'Gate', 'Aminatou', 'Monkey', 'Basri', 'Specter', 'Kirin', 'Tarkir', 'Vryn', 'Lammasu', 'Wildfire', 'Belenon', 'Case', 'Dungeon', 'Rigger', 'Nastiest,', 'Peasant', 'Egg', 'Paratrooper', 'Phoenix', 'Satyr', 'Ersta', 'Gallifrey', 'Jackal', 'Sable', 'Scientist', 'The Abyss', 'Nomad', 'Djinn', 'The Library', 'Capenna', 'Shenmeng', 'Soldier', 'Mutant', 'Calix', 'Treasure', 'Karsus', 'Imp', 'Town', 'Lizard',
             'Mammoth', 'Ranger', 'Gamer', 'Dauthi', 'Whale', 'Desert', 'Vampyre', 'Equipment', 'Varmint', 'Fox', 'Astartes', 'Zombie', 'Cridhe', 'Innistrad', 'Cow', 'Kaya', 'Androzani Minor', 'Lorwyn', 'Aura', 'Shaman', 'Reflection', 'Control', 'Spider', 'Time', 'Nephilim', 'New Phyrexia', 'Xerex', 'Myr', 'Wrestler', 'Trap', 'Bobblehead', 'Juggernaut', 'Power-Plant', 'Custodes', 'Saga', 'Bird', 'Dwarf', 'Capybara', 'Thopter', 'Demigod', 'Beeble', 'Pony', 'Venser', 'Zariel', 'Kaito', 'Construct', 'Halfling', 'Incarnation', 'Arcavios', 'Squirrel', 'Azra', 'Garruk', 'Las Vegas', 'Time Lord', 'Golem', 'Judge', 'Kephalai', 'Coward', 'Pest', 'Sponge', 'Phelddagrif', 'Realm', 'Sphere', 'Hero', 'Treefolk', 'Rat', 'Survivor', 'Skunk', 'Hellion', 'Zonian', 'Necron', 'Shandalar', 'Guff', 'Trilobite', 'Attraction', 'Camel', 'Mars', 'Horror', 'Avatar', 'Lukka', 'Bolas''s Meditation Realm', 'Locus', 'Azgol', 'Crocodile', 'Lady', 'Comet', 'Waiter', 'Metathran', 'Ral', 'Raccoon', 'Horse',
             'Assassin', 'Volver', 'Elspeth', 'You', 'Dominaria', 'LaIR', 'Omen', 'Designer', 'Thalakos', 'Minion', 'Baddest,', 'Cloud', 'Bear', 'Tezzeret', 'Chimera', 'Gargantikar', 'Angrath', 'Cleric', 'The', 'Hippo', 'Rabiah', 'Jace', 'Zubera', 'Ogre', 'Kolbahan', 'Spawn', 'Vivien', 'Warlock', 'Dreadnought', 'Freyalise', 'Phyrexia', 'Employee', 'Illusion', 'Worm', 'Blind Eternities', 'Inquisitor', 'Ship', 'Gideon', 'Monk', 'Scorpion', 'Villain', 'Tamiyo', 'Beholder', 'Basilisk', 'Kyneth', 'Unknown Planet', 'Wurm', 'Xenagos', 'Goblin', 'Elemental', 'Avishkar', 'Mine', 'Guest', 'Dihada', 'Noggle', 'C''tan', 'Processor', 'Cockatrice', 'Crab', 'Fish', 'Sliver', 'Badger', 'Kamigawa', 'Clamfolk', 'Arcane', 'Forest', 'Gith', 'Orc', 'Knight', 'Sivitri', 'Saproling', 'Chef', 'Demon', 'Vehicle', 'Griffin', 'Biggest,', 'Chicago', 'Vedalken', 'Tower', 'Tibalt', 'Boxer', 'Berserker', 'Duck', 'Powerstone', 'Amsterdam', 'Outside Mutter''s Spiral', 'Necros', 'Mercenary', 'Regatha', 'Samut',
             'Human', 'Universia Beyondia', 'Symbiote', 'Proper', 'Troll', 'Orgg', 'Squid', 'Noble', 'Head', 'Scout', 'Chorus', 'Harpy', 'Ooze', 'Igpay', 'Wizard', 'Hippogriff', 'Mordenkainen', 'Primarch', 'Gargoyle', 'Penguin', 'Amonkhet', 'Elemental?', 'Skaro', 'Key', 'MagicCon', 'Kavu', 'Dack', 'Jeska', 'Wrenn', 'Inzerva', 'Rogue', 'Ixalan', 'Kiora', 'Mongoose', 'Equilor', 'Barbarian', 'Quest', 'Samurai', 'Alfava Metraxis', 'Goat', 'Flagbearer', 'Detective', 'Boar', 'Moogle', 'The Dalek Asylum', 'Duskmourn', 'Luvion', 'Kasmina', 'Nissa', 'Vraska', 'Foldaria', 'Tyvar', 'Siren', 'Foundations', 'Lair', 'Ajani', 'Doctor', 'Clamhattan', 'Faerie', 'Spellshaper', 'Island', 'Manticore', 'Echoir', 'Wolf', 'Eye', 'Windgrace', 'Starfish', 'Secret Lair', 'Insect', 'Secret', 'Horsehead Nebula', 'Wall', 'Ellywick', 'Luxior', 'Background', 'Armored', 'Mime', 'Child', 'God', 'Ox', 'Rebel', 'Hell', 'Weird', 'Porcupine', 'Wombat', 'B.O.B.', 'Artificer', 'Oyster', 'Ergamon', 'Mummy', 'Niko',
             'Spirit', 'Atog', 'Ulgrotha', 'Clue', 'Bat', 'Nightmare', 'Ninja', 'Spacecraft', 'Minsc', 'Earth', 'Soltari', 'Bahamut', 'Werewolf', 'Muraganda', 'Lolth', 'Cyberman', 'Killbot', 'Grandchild', 'Koth', 'Wolverine', 'Rune', 'Sheep', 'Leech', 'Angel', 'Dinosaur', 'Dakkon', 'Archer' }

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
            case _:
                mana_cost.colorless = 0 if elm == "X" else elm
    return mana_cost
def parse_planeswalker_abilities(name: Card, text: str):
    out = []
    text = text.split("\n")

    for elm in text:
        if elm[0] != "[":
            continue
        elm = elm.split(":")[0]
        out.append(ActivableAbility(name = name, loyalty = elm[1:-1]))
    return out
def parse_colors(name: Card, colors: list[str]):
    out = []
    for color in colors:
        match color:
            case "R":
                out.append(Colors(name = name, color = "red"))
            case "U":
                out.append(Colors(name = name, color = "blue"))
            case "G":
                out.append(Colors(name = name, color = "green"))
            case "B":
                out.append(Colors(name = name, color = "black"))
            case "W":
                out.append(Colors(name = name, color = "white"))
    return out
def parse_types(name: Card, _types: list[str]):
    out = []
    for type_ in _types:
        if type_ not in types:
            continue
        out.append(Types(name = name, color = type_))
    return out
def parse_supertypes(name: Card, _supertypes: list[str]):
    out = []
    for supertype in _supertypes:
        if supertypes not in supertypes:
            continue
        out.append(Supertypes(name = name, color = supertype))
    return out
def parse_subtypes(name: Card, _subtypes: list[str]):
    out = []
    for subtype in _subtypes:
        if subtype not in subtypes:
            continue
        out.append(Subtypes(name = name, color = subtype))
    return out
