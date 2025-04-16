--7. Find all the cards with a defense of at least 2 that have abilities requiring the sacrifice of a creature
-- First, we select cards according to type (Creature), then we check if the activable ability requires sacrifice and if defence is higher than 1
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM card c, activable_ability a, types t
WHERE c.name= t.name
  AND t.type='Creature'
  AND c.defense >1
  AND c.name = a.name
  AND a.sacrifice = true;
