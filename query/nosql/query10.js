// 10. Find all the creatures with Champion ability ordered by power
db.card.find({keywords: 'Champion'}, {name: 1}).sort({power: -1})