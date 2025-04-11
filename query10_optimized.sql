-- 10. Find all the creatures with Champion ability ordered by power
EXPLAIN ANALYSE
SELECT c.name, c.power
FROM card c
         JOIN triggerable_characteristics tc
              ON tc.name=c.name AND tc.characteristic='Champion'
         JOIN types t
              ON t.name = c.name AND t.type='Creature'
ORDER BY c.power DESC;