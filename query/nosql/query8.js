// 8. Find instants with a cost of exactly 1 colored mana grouped by color
// We must use an aggregate function to group by color
// First we search for all records that have 'Instant' among their types; then we must find those that cost exactly one colored mana: the only 'easy' way to do this is by using a regex pattern that covers every possible combination of one-mana costs
// Lastly we group by color and name and sort by color to have all the elements of the same color close (Also by name to have them alphabetically ordered)
// Some elements are missing because in the original cards that can be payed with different colored-mana appear two times in the list, while here only once
db.card.aggregate([{$match: {types: "Instant", manaCost: {$regex: /^(\{X\}\{([WRPBUG]\}|\{([WPRBUG](\/[WRBUGP])*)\})|\{([WPRBUG](\/[WRBUGP])*)\})$/}}},{$group: {_id: {color: "$manaCost", name: "$name"}}}, {$sort: { "_id.color": 1, "_id.name": 1 }}]);