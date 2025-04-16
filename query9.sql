-- 9. Find all creatures with power higher than defense, green with Trample, Vigilance and cost >= 3
-- First, we select cards according to type (Creature) and characteristics (Trample and Vigilance), then we check if one of the colors is green, calculate the total mana cost and check if it's higher than 2
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM card c, types t, colors cl, attack_characteristics ac1, attack_characteristics ac2
WHERE c.name=t.name
  AND t.type='Creature'
  AND c.power>c.defense
  AND c.name=ac1.name
  AND ac1.characteristic='Trample'
  AND ac2.name = c.name
  AND ac2.characteristic='Vigilance'
  AND cl.name=c.name
  AND cl.color='Green'
  AND (SELECT m.black+ m.blue+ m.colorless+ m.green+ m.red+ m.snow+ m.white
       FROM mana_cost m
       WHERE m.id = c.mana_cost) > 2;
