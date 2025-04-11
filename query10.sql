-- 10. Find all the creatures with Champion ability ordered by power
EXPLAIN ANALYSE
SELECT DISTINCT c.*
FROM card c, triggerable_characteristics tc, types t
WHERE c.name = tc.name
  AND tc.characteristic = 'Champion'
  AND c.name = t.name
  AND t.type = 'Creature'
ORDER BY c.power DESC;
