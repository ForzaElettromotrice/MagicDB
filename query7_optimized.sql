--7. Find all the cards with a defense of at least 2 that have abilities requiring the sacrifice of a creature
EXPLAIN ANALYSE
SELECT c.name, c.defense
FROM card c
         JOIN activable_ability a
              ON c.name=a.name AND a.sacrifice=true
         JOIN types t
              ON c.name=t.name AND t.type = 'Creature'
WHERE c.defense >1;