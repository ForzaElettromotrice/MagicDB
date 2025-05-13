// 2. Find the number of creatures with Flying with a power of at least 6
// First we select the records with 'Creature' in their types, 'Flying' in their keywords and with a power > 5, then we count them
// There is a creature missing because it was saved differently: 'Haunting Apparition's power is equal to 1 plus the number of green creature cards in the chosen player's graveyard.', so in the nosql db it has a power of 0 (starting power), while in the sql db it has a power of 10 (placeholder value)
db.card.find({types: "Creature", keywords: "Flying", power: { $gt: 5 }}).count()