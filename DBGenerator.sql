create sequence active_ability_id_seq
    as integer;

create type colors_t as enum ('Red', 'Green', 'Blue', 'White', 'Black');

create type types_t as enum ('Artifact', 'Creature', 'Enchantment', 'Instant', 'Land', 'Planeswalker', 'Kindred', 'Tribal', 'Sorcery', 'World');

create type supertypes_t as enum ('Base', 'Snow', 'Legendary');

create type subtypes_t as enum ('Otter', 'Gobakhan', 'Omenpath', 'Chicken', 'Possum', 'Sloth', 'Domri', 'Hamster', 'sECreT', 'Donkey', 'Art', 'Aurochs', 'Homunculus', 'Aetherborn', 'Walrus', 'Ikoria', 'Mountain', 'Slug', 'Spy', 'Tasha', 'Brushwagg', 'Gremlin', 'Hag', 'Mercadia', 'Fire', 'Will', 'Fungus', 'Arkhos', 'Cave', 'Spuzzem', 'Beast', 'Daretti', 'Elder', 'Devil', 'Quintorius', 'Rabbit', 'Surrakar', 'Brainiac', 'Elves', 'Serra’s Realm', 'Kinshala', 'Fractal', 'Champion', 'Ashiok', 'Townsfolk', 'Cartouche', 'Darillium', 'Mirrodin', 'Gus', 'Advisor', 'Ape', 'Lamia', 'Nautilus', 'Kaldheim', 'Elk', 'Szat', 'Lesson', 'Narset', 'Coyote', 'Dryad', 'Sarkhan', 'Homarid', 'Kylem', 'Mount', 'Nahiri', 'Nightstalker', 'Tree', 'Pyrulea', 'Theros', 'Ouphe', 'Bloomburrow', 'Ir', 'Spike', 'Shark', 'Chandra', 'Toy', 'Etiquette', 'Kangaroo', 'Davriel', 'Moonfolk', 'Frog', 'Mole', 'Human?', 'Hyena', 'Drone', 'Giant', 'Bard', 'Liliana', 'Antausia', 'Master', 'Sphinx', 'Leviathan', 'Nymph', 'Saheeli', 'Bolas', 'Deb', 'Zendikar', 'Eldraine', 'Zhalfir', 'Elminster', 'Wanderer', 'Mission', 'Shrine', 'Kandoka', 'Swamp', 'Ravnica', 'Alara', 'Tiefling', 'Mite', 'Kobold', 'Lhurgoyf', 'Fabacin', 'Ally', 'Contraption', 'Moon', 'Byode', 'Svega', 'Dog', 'New Earth', 'Room', 'Siege', 'Mouse', 'Snake', 'Hawk', 'Minotaur', 'Iquatana', 'Kraken', 'Deer', 'Pirate', 'Alien', 'Huatli', 'Antelope', 'Bringer', 'Fiora', 'Robot', 'Hatificer', 'Thunder Junction', 'Mongseng', 'Clown', 'Dragon', 'Tyranid', 'Snail', 'Jared', 'Shade', 'Teyo', 'Rowan', 'Artist', 'Ferret', 'Armadillo', 'Monger', 'Yanling', 'Vampire', 'Chameleon', 'Urza', 'Jellyfish', 'Vronos', 'Teferi', 'Elf', 'Beaver', 'Estrid', 'Jaya', 'Class', 'Salamander', 'Valla', 'Serra', 'Unicorn', 'Masticore', 'Fortification', 'Efreet', 'Grist', 'Cat', 'Praetor', 'Bureaucrat', 'Kor', 'Archon', 'Oko', 'Hydra', 'Mystic', 'Pegasus', 'Ugin', 'Cyborg', 'Rath', 'Segovia', 'Rhino', 'Trenzalore', 'Point', 'Lobster', 'Dovin', 'Gnoll', 'Urza''s', 'Glimmer', 'Curse', 'and/or', 'Alicorn', 'Wraith', 'Elephant', 'Pilot', 'Athlete', 'Gorgon', 'Adventure', 'Citizen', 'Thrull', 'Licid', 'Gnome', 'Plains', 'Dalek', 'Scarecrow', 'Splinter', 'Pangolin', 'Shapeshifter', 'Carrier', 'Food', 'Assembly-Worker', 'Turtle', 'Yanggu', 'Plant', 'Phyrexian', 'Centaur', 'Autobot', 'Serpent', 'Seal', 'Octopus', 'Abian', 'Performer', 'Synth', 'Ulamog''s', 'Warrior', 'of', 'Eldrazi', 'Karn', 'Drake', 'Apalapucia', 'Arlinn', 'Weasel', 'Shadowmoor', 'Moag', 'Cephalid', 'Nixilis', 'Merfolk', 'Cyclops', 'Slith', 'Druid', 'Yeti', 'Skeleton', 'Kithkin', 'Sorin', 'Gate', 'Aminatou', 'Monkey', 'Basri', 'Specter', 'Kirin', 'Tarkir', 'Vryn', 'Lammasu', 'Wildfire', 'Belenon', 'Case', 'Dungeon', 'Rigger', 'Nastiest,', 'Peasant', 'Egg', 'Paratrooper', 'Phoenix', 'Satyr', 'Ersta', 'Gallifrey', 'Jackal', 'Sable', 'Scientist', 'The Abyss', 'Nomad', 'Djinn', 'The Library', 'Capenna', 'Shenmeng', 'Soldier', 'Mutant', 'Calix', 'Treasure', 'Karsus', 'Imp', 'Town', 'Lizard', 'Mammoth', 'Ranger', 'Gamer', 'Dauthi', 'Whale', 'Desert', 'Vampyre', 'Equipment', 'Varmint', 'Fox', 'Astartes', 'Zombie', 'Cridhe', 'Innistrad', 'Cow', 'Kaya', 'Androzani Minor', 'Lorwyn', 'Aura', 'Shaman', 'Reflection', 'Control', 'Spider', 'Time', 'Nephilim', 'New Phyrexia', 'Xerex', 'Myr', 'Wrestler', 'Trap', 'Bobblehead', 'Juggernaut', 'Power-Plant', 'Custodes', 'Saga', 'Bird', 'Dwarf', 'Capybara', 'Thopter', 'Demigod', 'Beeble', 'Pony', 'Venser', 'Zariel', 'Kaito', 'Construct', 'Halfling', 'Incarnation', 'Arcavios', 'Squirrel', 'Azra', 'Garruk', 'Las Vegas', 'Time Lord', 'Golem', 'Judge', 'Kephalai', 'Coward', 'Pest', 'Sponge', 'Phelddagrif', 'Realm', 'Sphere', 'Hero', 'Treefolk', 'Rat', 'Survivor', 'Skunk', 'Hellion', 'Zonian', 'Necron', 'Shandalar', 'Guff', 'Trilobite', 'Attraction', 'Camel', 'Mars', 'Horror', 'Avatar', 'Lukka', 'Bolas''s Meditation Realm', 'Locus', 'Azgol', 'Crocodile', 'Lady', 'Comet', 'Waiter', 'Metathran', 'Ral', 'Raccoon', 'Horse', 'Assassin', 'Volver', 'Elspeth', 'You', 'Dominaria', 'LaIR', 'Omen', 'Designer', 'Thalakos', 'Minion', 'Baddest,', 'Cloud', 'Bear', 'Tezzeret', 'Chimera', 'Gargantikar', 'Angrath', 'Cleric', 'The', 'Hippo', 'Rabiah', 'Jace', 'Zubera', 'Ogre', 'Kolbahan', 'Spawn', 'Vivien', 'Warlock', 'Dreadnought', 'Freyalise', 'Phyrexia', 'Employee', 'Illusion', 'Worm', 'Blind Eternities', 'Inquisitor', 'Ship', 'Gideon', 'Monk', 'Scorpion', 'Villain', 'Tamiyo', 'Beholder', 'Basilisk', 'Kyneth', 'Unknown Planet', 'Wurm', 'Xenagos', 'Goblin', 'Elemental', 'Avishkar', 'Mine', 'Guest', 'Dihada', 'Noggle', 'C''tan', 'Processor', 'Cockatrice', 'Crab', 'Fish', 'Sliver', 'Badger', 'Kamigawa', 'Clamfolk', 'Arcane', 'Forest', 'Gith', 'Orc', 'Knight', 'Sivitri', 'Saproling', 'Chef', 'Demon', 'Vehicle', 'Griffin', 'Biggest,', 'Chicago', 'Vedalken', 'Tower', 'Tibalt', 'Boxer', 'Berserker', 'Duck', 'Powerstone', 'Amsterdam', 'Outside Mutter''s Spiral', 'Necros', 'Mercenary', 'Regatha', 'Samut', 'Human', 'Universia Beyondia', 'Symbiote', 'Proper', 'Troll', 'Orgg', 'Squid', 'Noble', 'Head', 'Scout', 'Chorus', 'Harpy', 'Ooze', 'Igpay', 'Wizard', 'Hippogriff', 'Mordenkainen', 'Primarch', 'Gargoyle', 'Penguin', 'Amonkhet', 'Elemental?', 'Skaro', 'Key', 'MagicCon', 'Kavu', 'Dack', 'Jeska', 'Wrenn', 'Inzerva', 'Rogue', 'Ixalan', 'Kiora', 'Mongoose', 'Equilor', 'Barbarian', 'Quest', 'Samurai', 'Alfava Metraxis', 'Goat', 'Flagbearer', 'Detective', 'Boar', 'Moogle', 'The Dalek Asylum', 'Duskmourn', 'Luvion', 'Kasmina', 'Nissa', 'Vraska', 'Foldaria', 'Tyvar', 'Siren', 'Foundations', 'Lair', 'Ajani', 'Doctor', 'Clamhattan', 'Faerie', 'Spellshaper', 'Island', 'Manticore', 'Echoir', 'Wolf', 'Eye', 'Windgrace', 'Starfish', 'Secret Lair', 'Insect', 'Secret', 'Horsehead Nebula', 'Wall', 'Ellywick', 'Luxior', 'Background', 'Armored', 'Mime', 'Child', 'God', 'Ox', 'Rebel', 'Hell', 'Weird', 'Porcupine', 'Wombat', 'B.O.B.', 'Artificer', 'Oyster', 'Ergamon', 'Mummy', 'Niko', 'Spirit', 'Atog', 'Ulgrotha', 'Clue', 'Bat', 'Nightmare', 'Ninja', 'Spacecraft', 'Minsc', 'Earth', 'Soltari', 'Bahamut', 'Werewolf', 'Muraganda', 'Lolth', 'Cyberman', 'Killbot', 'Grandchild', 'Koth', 'Wolverine', 'Rune', 'Sheep', 'Leech', 'Angel', 'Dinosaur', 'Dakkon', 'Archer');

create type constant_characteristics_t as enum ('Hexproof', 'Defender', 'Flash', 'Reach', 'Haste', 'Deathtouch', 'Fear', 'Land-walk', 'Protection', 'Shroud', 'Flying', 'Affinity', 'Absorb', 'Banding', 'Changeling', 'Horsemanship', 'Chroma', 'Hellbent', 'Domain', 'Epic', 'Vanishing', 'Phasing', 'Graft', 'Intimidate', 'Shadow', 'Radiance', 'Threshold', 'Delve', 'Sunburst', 'Split Second', 'Modular', 'Ward');

create type attack_characteristics_t as enum ('First strike', 'Vigilance', 'Double strike', 'Lifelink', 'Annihilator', 'Trample', 'Poisonous', 'Wither', 'Exalted', 'Frenzy', 'Rampage', 'Battle cry', 'Provoke', 'Clash');

create type activable_characteristics_t as enum ('Entwine', 'FlashbackEvoke', 'Equip', 'Regeneration', 'Cycling', 'Fortify', 'Channel', 'Morph', 'Multikicker', 'Offering', 'Kicker', 'Forecast', 'Retrace', 'Reinforce', 'Buyback', 'Grandeur', 'Suspend', 'Transfigure', 'Transmute', 'Splice onto Arcane', 'Cumulative upkeep', 'Echo', 'Unearth', 'Aura swap', 'Sweep', 'Madness', 'Conspire', 'Dredge', 'Replicate');

create type triggerable_characteristics_t as enum ('Suspend', 'Graft', 'Epic', 'Vanishing', 'Madness', 'Kinship', 'Imprint', 'Flanking', 'Soulbound', 'Totem Armor', 'Champion', 'Cascade', 'Convoke', 'Conspire', 'Fateseal', 'Devour', 'Undying', 'Modular', 'Soulshift', 'Persist', 'Scry', 'Ripple', 'Recover', 'Replicate', 'Bloodthirst', 'Storm', 'Gravestorm', 'Haunt', 'Landfall', 'Hideaway', 'Amplify', 'Fading');

create domain uint as integer
    constraint positive check (VALUE >= 0);

create table mana_cost
(
    colorless uint             not null,
    red       double precision not null,
    blue      double precision not null,
    green     double precision not null,
    black     double precision not null,
    white     double precision not null,
    snow      uint             not null,
    id        serial
        constraint mana_cost_pk
            primary key,
    constraint mana_cost_k
        unique (colorless, red, blue, green, black, white, snow)
);

create table card
(
    name      varchar not null
        constraint card_pk
            primary key,
    power     integer,
    defense   integer,
    text      varchar,
    mana_cost integer not null
        constraint card_fk
            references mana_cost,
    loyalty   uint
);

create table types
(
    name varchar not null
        constraint types_fk
            references card
            on delete cascade,
    type types_t not null,
    constraint types_pk
        primary key (name, type)
);

create table supertypes
(
    name      varchar      not null
        constraint supertypes_fk
            references card
            on delete cascade,
    supertype supertypes_t not null,
    constraint supertypes_pk
        primary key (name, supertype)
);

create table subtypes
(
    name    varchar    not null
        constraint subtypes_fk
            references card
            on delete cascade,
    subtype subtypes_t not null,
    constraint subtypes_pk
        primary key (name, subtype)
);

create table colors
(
    name  varchar  not null
        constraint colors_fk
            references card
            on delete cascade,
    color colors_t not null,
    constraint colors_pk
        primary key (name, color)
);

create table constant_characteristics
(
    name           varchar                    not null
        constraint constant_characteristic_fk
            references card
            on delete cascade,
    characteristic constant_characteristics_t not null,
    constraint constant_characteristic_pk
        primary key (name, characteristic)
);

create table attack_characteristics
(
    name           varchar                  not null
        constraint attack_characteristics_fk
            references card
            on delete cascade,
    characteristic attack_characteristics_t not null,
    constraint attack_characteristics_pk
        primary key (name, characteristic)
);

create table triggerable_characteristics
(
    name           varchar                       not null
        constraint triggerable_characteristics_fk
            references card,
    characteristic triggerable_characteristics_t not null,
    constraint triggerable_characteristics_pk
        primary key (name, characteristic)
);

create table activable_characteristics
(
    name           varchar                     not null
        constraint activable_characteristics_fk
            references card
            on delete cascade,
    characteristic activable_characteristics_t not null,
    constraint activable_characteristics_pk
        primary key (name, characteristic)
);

create table activable_ability
(
    name        varchar                                                    not null
        constraint active_ability_fk
            references card
            on delete cascade,
    loyalty     integer,
    life_points uint,
    sacrifice   boolean,
    mana_cost   integer
        constraint active_ability_fk_2
            references mana_cost,
    tap         boolean,
    discard     boolean,
    id          integer default nextval('active_ability_id_seq'::regclass) not null
        constraint activable_ability_pk
            primary key,
    constraint active_ability_k
        unique (name, loyalty, life_points, sacrifice, mana_cost, tap, discard)
);

alter sequence active_ability_id_seq owned by activable_ability.id;

create table double_face_card
(
    name    varchar not null
        constraint double_face_card_pk
            primary key
        constraint double_face_card_fk
            references card
            on delete cascade,
    back    varchar not null
        constraint double_face_card_k
            unique
        constraint double_face_card_fk_2
            references card,
    isfront boolean not null
);

create table double_card
(
    name    varchar not null
        constraint double_card_pk
            primary key
        constraint double_card_fk
            references card,
    subface varchar not null
        constraint double_card_k
            unique
        constraint double_card_fk_2
            references card
);

create table meld_card
(
    name   varchar not null
        constraint meld_card_pk
            primary key
        constraint meld_card_fk
            references card,
    first  varchar not null
        constraint meld_card_fk_2
            references card,
    second varchar
        constraint meld_card_fk_3
            references card
);

create function bidirectionaldoublefacecard() returns trigger
    language plpgsql
as
$$
DECLARE
    front boolean;

BEGIN

    SELECT isfront
    into front
    FROM double_face_card
    WHERE name = NEW.back
      AND back = NEW.name;

    IF FOUND THEN
        IF front = NEW.isfront THEN
            RAISE EXCEPTION 'This pair of cards does not have a front or has 2 fronts!';
        END IF;
    ELSE
        RAISE EXCEPTION 'The back of this card does not exist!';
    END IF;

    RETURN NEW;
END;
$$;

create trigger triggerdoublefacecard
    after insert
    on double_face_card
    for each row
execute procedure bidirectionaldoublefacecard();

create function bidirectionaldoublecard() returns trigger
    language plpgsql
as
$$
BEGIN
    IF NOT EXISTS(SELECT 1
                  FROM double_card
                  WHERE name = NEW.subface
                    AND subface = NEW.name) THEN
        RAISE EXCEPTION 'The subface of this card does not exist!';
    END IF;
    RETURN NEW;
END;
$$;

create function bidirectionalmeldcard() returns trigger
    language plpgsql
as
$$
DECLARE
    results int;
BEGIN

    IF NEW.second IS NULL THEN
        IF NOT EXISTS(SELECT 1
                      FROM meld_card
                      WHERE name = NEW.first
                        AND (first = NEW.name OR second = NEW.name)
                        AND second IS NOT NULL) THEN
            RAISE EXCEPTION 'The meld version of this card does not exist!';
        END IF;
    ELSE
        SELECT COUNT(name)
        INTO results
        FROM meld_card
        WHERE first = NEW.name
          AND second IS NULL
          AND (NEW.first = name OR NEW.second = name);

        IF results != 2 THEN
            RAISE EXCEPTION 'This meld card has not exactly 2 fronts!';
        END IF;
    END IF;
    RETURN NEW;
END;
$$;

create function checkplaneswalkerintegrity() returns trigger
    language plpgsql
as
$$
BEGIN

    IF NEW.loyalty IS NOT NULL AND NOT EXISTS(SELECT loyalty
                                              FROM activable_ability
                                              WHERE name = NEW.name
                                                AND loyalty IS NOT NULL) THEN
        RAISE EXCEPTION 'This planeswalker has no loyalty ability!';
    END IF;

    RETURN NEW;
END;
$$;

create function checkisplaneswalker() returns trigger
    language plpgsql
as
$$
BEGIN

    IF NEW.loyalty IS NOT NULL AND NOT EXISTS(SELECT loyalty
                                              FROM card
                                              WHERE name = NEW.name
                                                AND loyalty IS NOT NULL) THEN
        RAISE EXCEPTION 'This card has loyalty ability but it isn''t a Planeswalker!';
    END IF;

    RETURN NEW;
END;
$$;

create trigger triggeractivableabilityplaneswalker
    after insert
    on activable_ability
    for each row
execute procedure checkisplaneswalker();

