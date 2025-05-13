// 10. Find all the creatures with Champion ability ordered by power
// First we select all the records that have 'Champion' among their keywords, then we order by power
// Some records are missing because of an error in parsing the text: they result as having the 'Champion' ability but they actually don't have it
db.card.find({keywords: 'Champion'}, {name: 1, power: 1}).sort({power: -1})