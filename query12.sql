-- 12. Find dual lands that gives you at least 1 blue mana
EXPLAIN ANALYSE
SELECT c.*
FROM card c, types t
WHERE c.name=t.name
  AND t.type = 'Land'
  AND (SELECT COUNT(cl.color)
       FROM colors cl
       WHERE c.name = cl.name
       GROUP BY c.name)=2
  AND EXISTS(SELECT *
             FROM colors cl
             WHERE c.name=cl.name
               AND cl.color='Blue');
