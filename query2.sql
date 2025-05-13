-- 2. Find the number of creatures with Flying with a power of at least 6
-- First, we select cards according to type (Creature) and characteristic (Flying), then we check if the creature has a power higher than 5 and we count them
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT count(DISTINCT c.name) AS total
FROM card c, constant_characteristics cc, types t
WHERE c.name=cc.name
  AND t.name=c.name
  AND t.type='Creature'
  AND cc.characteristic = 'Flying'
  AND c.power > 5;
