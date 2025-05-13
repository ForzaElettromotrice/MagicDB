//11. Find all meld cards of which you are the second
//We find the records that have the 'Meld' layout and the 'b' side
db.card.find({layout: "meld", side: "b"}, {name: 1})