-- 1. Find all legendary Planeswalkers that have loyalty abilities with a minimum cost of -5 and a maximum cost of +1
EXPLAIN ANALYSE
SELECT DISTINCT c.*
FROM card c, types t, supertypes st, activable_ability a
WHERE c.name=t.name
  AND c.name=st.name
  AND t.type='Planeswalker'
  AND st.supertype='Legendary'
  AND a.name=c.name
  AND a.loyalty > -6
  AND a.loyalty < 2;
