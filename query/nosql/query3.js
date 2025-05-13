// 3. Find the average defense of creatures with Deathtouch but without Reach
// We need to use an aggregate function to find the average
// First we select the records that DON'T have 'Reach' in their keywords but HAVE 'Deathtouch' (they could have something else, too), then we group them and calculate the toughness average
// The results are different because the original query doesn't select every creature so the calculation for the avg is slightly off
db.card.aggregate([{$match: {keywords: {$ne: "Reach", $all: ['Deathtouch']}}}, {$group:{_id: "_id", avg_def:{$avg: "$toughness"}}}]);