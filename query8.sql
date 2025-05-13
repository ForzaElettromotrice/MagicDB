--8. Find instants with a cost of exactly 1 colored mana grouped by color
-- First, we select cards according to type (Instant), then we calculate the total mana cost and check if it's equal to 1 and if it's not colorless, lastly we group by color
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT cl.color, c.*
FROM card c, types t, colors cl
WHERE c.name=t.name
  AND cl.name=c.name
  AND t.type='Instant'
  AND (SELECT m.black+ m.blue+ m.colorless+ m.green+ m.red+ m.snow+ m.white
       FROM mana_cost m
       WHERE m.id = c.mana_cost
         AND m.colorless = 0) = 1
GROUP BY cl.color, c.name;
