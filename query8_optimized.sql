--8. Find instants with a cost of exactly 1 colored mana grouped by color
-- We can optimize this query by only selecting the fields we are interested in; not using 'distinct' since there are no duplicates; using the view to calculate the total mana cost and inner joins instead of multiple 'where' clauses
EXPLAIN ANALYSE
SELECT cl.color, c.name
FROM card c
         JOIN types t
              ON c.name=t.name AND t.type='Instant'
         JOIN colors cl
              ON c.name=cl.name
         JOIN mana_cost m
              ON c.mana_cost=m.id AND m.colorless=0 AND m.black+ m.blue+ m.green+ m.red+ m.snow+ m.white=1
GROUP BY cl.color, c.name;
