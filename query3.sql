-- 3. Find the average defense of creatures with Deathtouch but without Reach
EXPLAIN ANALYSE
SELECT AVG(c.defense) as avg_defense
FROM card c, constant_characteristics cc
WHERE c.name=cc.name
  AND cc.characteristic='Deathtouch'
  AND c.name NOT IN (SELECT c1.name
                     FROM constant_characteristics c1
                     WHERE c.name=c1.name
                       AND c1.characteristic='Reach');