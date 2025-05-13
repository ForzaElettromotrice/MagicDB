// 2. Find the number of creatures with Flying with a power of at least 6
db.card.find({types: "Creature", keywords: "Flying", power: { $gt: 5 }}).count()