-- 4. Find all Red\Black enchantments with a 6 Mana Cost
-- We can optimize this query by selecting only the fields we are interested in; using a inner join to avoid too many 'where' clauses; using the view to calculate the total mana cost instead of computing it each tim
EXPLAIN ANALYSE
SELECT DISTINCT c.name
FROM card c
         JOIN tot_mana m
              ON m.id=c.mana_cost AND m.tot= 6
         JOIN types t
              ON t.name=c.name AND t.type='Enchantment'
         JOIN colors cl
              ON cl.name=c.name
WHERE NOT EXISTS(SELECT 1
                 FROM colors cl
                 WHERE c.name=cl.name
                   AND cl.color
                     IN ('Blue', 'Green', 'White'));
