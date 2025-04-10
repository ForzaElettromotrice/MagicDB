from peewee import *

from enums import types, colors, supertypes, subtypes, activable_characteristics, attack_characteristics, constant_characterstics, triggerable_characteristics

db = PostgresqlDatabase('magic', user = 'f3m', password = '', host = 'localhost', port = 5432)

class UnknownField(object):
    def __init__(self, *_, **__): pass
class UIntField(Field):
    field_type = 'uint'

    def db_value(self, value):
        if value is None:
            return None
        if int(value) < 0:
            raise ValueError("The value must be >= 0.")
        return int(value)

    def python_value(self, value):
        if value is None:
            return None
        return int(value)

class BaseModel(Model):
    class Meta:
        database = db

class ManaCost(BaseModel):
    black = DoubleField()
    blue = DoubleField()
    colorless = UIntField()
    green = DoubleField()
    red = DoubleField()
    snow = UIntField()
    white = DoubleField()
    id = AutoField(primary_key = True)

    class Meta:
        table_name = 'mana_cost'
        indexes = (
            (('colorless', 'red', 'blue', 'green', 'black', 'white', 'snow', 'id'), True),
        )

    def __repr__(self):
        return f"{self.colorless if self.colorless != 0 else ''}{'R' * int(self.red)}{'U' * int(self.blue)}{'G' * int(self.green)}{'B' * int(self.black)}{'W' * int(self.white)}{'S' * int(self.snow)}"
class Card(BaseModel):
    defense = IntegerField(null = True)
    loyalty = UIntField(null = True)
    mana_cost = ForeignKeyField(column_name = 'mana_cost', field = 'id', model = ManaCost)
    name = CharField(primary_key = True)
    power = IntegerField(null = True)
    text = CharField(null = True)

    class Meta:
        table_name = 'card'

    def __repr__(self):
        return f"{self.name.__repr__()}{' (' + self.power.__repr__() + '/' + self.defense.__repr__() + ')' if self.loyalty is None else ''} {self.mana_cost.__repr__()} {'L = ' + self.loyalty.__repr__() if self.loyalty is not None else ''}"

class ActivableAbility(BaseModel):
    discard = BooleanField(null = True)
    life_points = UnknownField(null = True)  # integer
    loyalty = IntegerField(null = True)
    mana_cost = ForeignKeyField(column_name = 'mana_cost', field = 'id', model = ManaCost, null = True)
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)
    sacrifice = BooleanField(null = True)
    tap = BooleanField(null = True)

    class Meta:
        table_name = 'activable_ability'
        indexes = (
            (('mana_cost', 'loyalty', 'life_points', 'sacrifice', 'tap', 'discard'), True),
        )

    def __repr__(self):
        return f"({self.name.__repr__()}, {self.loyalty.__repr__()}, {self.life_points.__repr__()}, {self.sacrifice.__repr__()}, {self.mana_cost.__repr__()}, {self.tap.__repr__()}, {self.discard.__repr__()})"
class ActivableCharacteristics(BaseModel):
    characteristic = CharField(choices = [e for e in activable_characteristics])
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)

    class Meta:
        table_name = 'activable_characteristics'
        indexes = (
            (('name', 'characteristic'), True),
        )
        primary_key = CompositeKey('characteristic', 'name')

class AttackCharacteristics(BaseModel):
    characteristic = CharField(choices = [e for e in attack_characteristics])
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)

    class Meta:
        table_name = 'attack_characteristics'
        indexes = (
            (('name', 'characteristic'), True),
        )
        primary_key = CompositeKey('characteristic', 'name')

class Colors(BaseModel):
    color = CharField(choices = [e for e in colors])
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)

    class Meta:
        table_name = 'colors'
        indexes = (
            (('name', 'color'), True),
        )
        primary_key = CompositeKey('color', 'name')

    def __repr__(self):
        return f"{self.color.__repr__()}"

class ConstantCharacteristics(BaseModel):
    characteristic = CharField(choices = [e for e in constant_characterstics])
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)

    class Meta:
        table_name = 'constant_characteristics'
        indexes = (
            (('name', 'characteristic'), True),
        )
        primary_key = CompositeKey('characteristic', 'name')

class DoubleCard(BaseModel):
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card, primary_key = True)
    subface = ForeignKeyField(backref = 'card_subface_set', column_name = 'subface', field = 'name', model = Card, unique = True)

    class Meta:
        table_name = 'double_card'

class DoubleFaceCard(BaseModel):
    back = ForeignKeyField(column_name = 'back', field = 'name', model = Card, unique = True)
    isfront = BooleanField()
    name = ForeignKeyField(backref = 'card_name_set', column_name = 'name', field = 'name', model = Card, primary_key = True)

    class Meta:
        table_name = 'double_face_card'

class MeldCard(BaseModel):
    first = ForeignKeyField(column_name = 'first', field = 'name', model = Card)
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card, primary_key = True)
    second = ForeignKeyField(backref = 'meld_card_second_set', column_name = 'second', field = 'name', model = Card, null = True)

    class Meta:
        table_name = 'meld_card'

class Subtypes(BaseModel):
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)
    subtype = CharField(choices = [e for e in subtypes])

    class Meta:
        table_name = 'subtypes'
        indexes = (
            (('name', 'subtype'), True),
        )
        primary_key = CompositeKey('name', 'subtype')

    def __repr__(self):
        return f"{self.subtype.__repr__()}"
class Supertypes(BaseModel):
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)
    supertype = CharField(choices = [e for e in supertypes])

    class Meta:
        table_name = 'supertypes'
        indexes = (
            (('name', 'supertype'), True),
        )
        primary_key = CompositeKey('name', 'supertype')

    def __repr__(self):
        return f"{self.supertype.__repr__()}"
class TriggerableCharacteristics(BaseModel):
    characteristic = CharField(choices = [e for e in triggerable_characteristics])
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)

    class Meta:
        table_name = 'triggerable_characteristics'
        indexes = (
            (('name', 'characteristic'), True),
        )
        primary_key = CompositeKey('characteristic', 'name')

class Types(BaseModel):
    name = ForeignKeyField(column_name = 'name', field = 'name', model = Card)
    type = CharField(choices = [e for e in types])

    class Meta:
        table_name = 'types'
        indexes = (
            (('name', 'type'), True),
        )
        primary_key = CompositeKey('name', 'type')

    def __repr__(self):
        return f"{self.type.__repr__()}"
