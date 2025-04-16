-- 6. Find adventure cards that require at least 5 mana
-- First, we select double cards according to subtype (Adventure), then we calculate the total mana value for each face, uniting them in a single table, and then we calculate the sum of the values, checking if it's higher than 4
-- To sum correctly, we group by face and subface, and order by cost
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT d.*, SUM(t.value) as cost
FROM double_card d, card c1, card c2, subtypes t1,
     LATERAL (
         SELECT m1.blue + m1.colorless + m1.green + m1.snow + m1.white + m1.black + m1.red AS value
         FROM mana_cost m1
         WHERE m1.id = c1.mana_cost
         UNION ALL
         SELECT m2.blue + m2.colorless + m2.green + m2.snow + m2.white + m2.black + m2.red AS value
         FROM mana_cost m2
         WHERE m2.id = c2.mana_cost
         ) AS t
WHERE d.name = c1.name
  AND d.subface = c2.name
  AND c1.name = t1.name

  AND t1.subtype = 'Adventure'
GROUP BY d.name, d.subface
HAVING SUM(t.value) > 4
ORDER BY cost;

