// 6. Find adventure cards that require at least 5 mana
// We need an aggregate function to calculate the totalMana
// First we select the records that have the layout 'Adventure'; then we group the records with the same name (this means they are the two faces of the same card) and sum the faceManaValue to calculate the totalMana; lastly we select only the records that have a totalMana of at least 5
// We have different results because in the original query we check for 'Adventure' subtype, while in this we check for the 'Adventure' layout: some adventure cards do not have the 'Adventure' subtype, but have 'Adventure' layout!
db.card.aggregate([{$match: {layout: "adventure"}}, {$group: {_id: "$name", totalMana: {$sum: "$faceManaValue"}}}, {$match: {totalMana: {$gt: 4}}}])