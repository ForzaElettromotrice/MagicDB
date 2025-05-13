// 1. Find all legendary Planeswalkers that have loyalty abilities with a minimum cost of -5 and a maximum cost of +1
// To avoid duplicates, we use the method 'distinct' on the 'name' field
// We must select the records with 'Legendary' in its supertypes and 'Planeswalker' in its types
// We don't need all abilities to satisfy the rule, so we use the 'elemMatch' operator on the >-5, < 1 criteria. The operator is applied on the value of the dictionary that has 'cost' as key
// We have an extra value because in the sql query the record 'Ayani Goldmane/Ayani Goldmane' is saved separately, so it conflicts with 'Ayani Goldmane' and is not returned
db.card.distinct("name", {supertypes: "Legendary", types: "Planeswalker", abilities: {$elemMatch: {cost: {$gt: -6, $lt: 2}}}});