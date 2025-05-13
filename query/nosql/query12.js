//12. Find dual lands that gives you at least 1 blue mana
db.card.find({types: "Land", colorIdentity: {$size: 2, $in: ['U']}})