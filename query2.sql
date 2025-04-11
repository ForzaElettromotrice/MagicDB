-- 2. Find the number of creatures with Flying with a power of at least 6
EXPLAIN ANALYSE
SELECT count(DISTINCT c.name) AS total
FROM card c, constant_characteristics cc, types t
WHERE c.name=cc.name
  AND t.name=c.name
  AND t.type='Creature'
  AND cc.characteristic = 'Flying'
  AND c.power > 5;