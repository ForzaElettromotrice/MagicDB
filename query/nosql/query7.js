// 7. Find all the cards with a defense of at least 2 that have abilities requiring the sacrifice of a creature
// First we select all the records that have 'Creature' among their types and a toughness greater that 1
// We use the 'elemMatch' operator on the 'Sacrifice' criteria to find at least one ability that requires a sacrifice. The operator is applied on the value of the dictionary that has 'cost' as key
// We have an extra value because in the sql query the record 'Grimgrin, Corpse-Born // Grimgrin, Corpse-Born' is saved separately, so it conflicts with 'Grimgrin, Corpse-Born' and is not returned
db.card.find({types: "Creature", toughness: {$gt: 1}, abilities: {$elemMatch: {cost: "Sacrifice"}}}, {name: 1, toughness: 1})