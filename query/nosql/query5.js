// 5. Find the equippable artifact(s) with the highest mana cost
db.card.find({types: "Artifact", subtypes: "Equipment"}, {name: 1, manaValue: 1}).sort({manaValue: -1}).limit(1)