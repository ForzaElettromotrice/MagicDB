// 4. Find all Red\Black enchantments with a 6 Mana Cost
// To avoid duplicates, we use the method 'distinct' on the 'name' field
// First we select the records that have 'Enchantment' among their types; then we check if the 'colorIdentity' is Red OR Black (we check if the value is 1 and if it's among one of the letters), then we check if the manaValue is 6 (for simple cards) or if the faceManaValue is 6 (for double cards)
// Results may look different but they're actually the same, just in a different order
db.card.distinct("name", {types: "Enchantment", colorIdentity: {$in: ["R", "B"], $size: 1 }, "$or": [{manaValue: 6}, {faceManaValue: 6}]})