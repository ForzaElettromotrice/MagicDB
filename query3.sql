-- 3. Find the average defense of creatures with Deathtouch but without Reach
EXPLAIN ANALYSE
SELECT AVG(c.defense) as avg_defense
FROM card c
         JOIN constant_characteristics cc1
              ON c.name=cc1.name
         LEFT JOIN constant_characteristics cc2
                   ON c.name = cc2.name
                       AND cc2.characteristic = 'Reach'
WHERE cc1.characteristic = 'Deathtouch'
  AND cc2.name IS NULL;
