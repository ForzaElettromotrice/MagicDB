-- 3. Find the average defense of creatures with Deathtouch but without Reach
-- First, we select cards with Deathtouch; then, to avoid those with Reach, we do a left join: this way, if the creature does not have Reach, its name will be null, thus we can select it. In the end, we calculate the average defence
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT AVG(c.defense) as avg_defense
FROM card c
         JOIN constant_characteristics cc1
              ON c.name=cc1.name
         LEFT JOIN constant_characteristics cc2
                   ON c.name = cc2.name
                       AND cc2.characteristic = 'Reach'
WHERE cc1.characteristic = 'Deathtouch'
  AND cc2.name IS NULL;
