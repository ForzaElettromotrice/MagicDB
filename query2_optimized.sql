-- 2. Find the number of creatures with Flying with a power of at least 6
EXPLAIN ANALYSE
SELECT count(c.name) AS total
FROM card c
         JOIN constant_characteristics cc
              ON cc.name=c.name AND cc.characteristic='Flying'
         JOIN types t
              ON t.name=c.name AND t.type='Creature'
WHERE c.power > 5;