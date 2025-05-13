-- 1. Find all legendary Planeswalkers that have loyalty abilities with a minimum cost of -5 and a maximum cost of +1
-- To optimize this query, we can remove the Card table since the name can be inferred by the type; we only select the fields we are interested in; we use inner joins to avoid too many 'where' conditions; and we use the 'between' operator instead of two separate checks
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT t.name
FROM types t
         JOIN supertypes st
              ON st.name=t.name AND st.supertype='Legendary'
         JOIN activable_ability a
              ON a.name =t.name AND a.loyalty BETWEEN -5 AND 1
WHERE t.type='Planeswalker';







