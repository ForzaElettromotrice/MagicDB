-- 6. Find adventure cards that require at least 5 mana
EXPLAIN ANALYZE
SELECT d.name, d.subface, SUM(m1.tot + m2.tot) AS cost
FROM double_card d
         JOIN card c1
              ON d.name = c1.name
         JOIN card c2
              ON d.subface = c2.name
         JOIN subtypes t1
              ON c1.name = t1.name AND t1.subtype='Adventure'
         JOIN tot_mana m1
              ON m1.id = c1.mana_cost
         JOIN tot_mana m2
              ON m2.id = c2.mana_cost
GROUP BY d.name, d.subface
HAVING SUM(m1.tot+m2.tot) > 4;

