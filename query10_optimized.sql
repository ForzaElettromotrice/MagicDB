-- 10. Find all the creatures with Champion ability ordered by power
-- To optimize this query we only select the fields we are interested in; we avoid selecting distinct couples since there are no duplicates; we do an inner join to avoid 'where' conditions
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query
SELECT c.name, c.power
FROM card c
         JOIN triggerable_characteristics tc
              ON tc.name=c.name AND tc.characteristic='Champion'
         JOIN types t
              ON t.name = c.name AND t.type='Creature'
ORDER BY c.power DESC;
