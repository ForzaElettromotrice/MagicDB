--7. Find all the cards with a defense of at least 2 that have abilities requiring the sacrifice of a creature
EXPLAIN ANALYSE
SELECT DISTINCT c.*
FROM card c, activable_ability a, types t
WHERE c.name= t.name
  AND t.type='Creature'
  AND c.defense >1
  AND c.name = a.name
  AND a.sacrifice = true;