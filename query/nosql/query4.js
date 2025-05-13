// 4. Find all Red\Black enchantments with a 6 Mana Cost
db.card.distinct("name", {types: "Enchantment", colorIdentity: { $in: ["R", "B"], $size: 1 }, "$or": [{manaValue: 6}, {faceManaValue: 6}]})