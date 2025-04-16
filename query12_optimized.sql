-- 12. Find dual lands that gives you at least 1 blue mana
-- We can optimize this query by selecting only the fields we are interested in; using an inner join to avoid too many 'where' conditions; not using the Card table since we can infer the name from the color; and counting distinct colors in the having clause instead of using a nested query
EXPLAIN ANALYSE
SELECT cl.name
FROM colors cl
         JOIN types t
              ON t.name = cl.name AND t.type='Land'
WHERE EXISTS (
    SELECT 1
    FROM colors sub_cl
    WHERE sub_cl.name = cl.name
      AND sub_cl.color = 'Blue'
)
GROUP BY cl.name
HAVING COUNT(DISTINCT cl.color) = 2;
