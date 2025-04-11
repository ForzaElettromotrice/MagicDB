--8. Find instants with a cost of exactly 1 colored mana grouped by color
EXPLAIN ANALYSE
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
