//11. Find all meld cards of which you are the second
db.card.find({layout: "meld", side: "b"}, {name: 1})