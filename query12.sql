-- 12. Find dual lands that gives you at least 1 blue mana
-- First, we select cards according to type (Land), then we count the colors of each land card and only select those that have two; lastly we check if at least one of the two colors is blue with the 'Exists' operator
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
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
