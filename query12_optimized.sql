-- 12. Find dual lands that gives you at least 1 blue mana
-- 8. Find dual lands that gives you at least 1 blue mana
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