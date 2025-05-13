//12. Find dual lands that gives you at least 1 blue mana
// We find all records that have 'Land' among their types and a colorIdentity of size 2 (since lands don't cost mana, colorIdentity will only have the color mana they give you). This color must be 'Blue' for at least one element, so we use the 'all' operator
db.card.find({types: "Land", colorIdentity: {$size: 2, $all: ['U']}}, {name: 1})