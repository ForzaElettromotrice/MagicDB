-- 1. Find all legendary Planeswalkers that have loyalty abilities with a minimum cost of -5 and a maximum cost of +1
EXPLAIN ANALYSE
SELECT DISTINCT t.name
FROM types t
         JOIN supertypes st
              ON st.name=t.name AND st.supertype='Legendary'
         JOIN activable_ability a
              ON a.name =t.name AND a.loyalty BETWEEN -5 AND 1
WHERE t.type='Planeswalker';