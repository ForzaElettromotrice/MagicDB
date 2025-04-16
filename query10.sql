-- 10. Find all the creatures with Champion ability ordered by power
-- First, we select cards according to type (Creature) and characteristic (Champion), we order according to power, with the most powerful on top
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM card c, triggerable_characteristics tc, types t
WHERE c.name = tc.name
  AND tc.characteristic = 'Champion'
  AND c.name = t.name
  AND t.type = 'Creature'
ORDER BY c.power DESC;
