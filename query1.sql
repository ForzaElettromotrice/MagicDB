-- 1. Find all legendary Planeswalkers that have loyalty abilities with a minimum cost of -5 and a maximum cost of +1
-- First, we select cards according to type (Planeswalker) and supertype (Legendary), then we select the correct loyalty value the creature must have
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM card c, types t, supertypes st, activable_ability a
WHERE c.name=t.name
  AND c.name=st.name
  AND t.type='Planeswalker'
  AND st.supertype='Legendary'
  AND a.name=c.name
  AND a.loyalty > -6
  AND a.loyalty < 2;
