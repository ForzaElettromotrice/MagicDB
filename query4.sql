-- 4. Find all Red\Black enchantments with a 6 Mana Cost
-- First, we select cards according to type (Enchantment); then we calculate the total mana value summing the colors present in mana cost, and only select those equal to 6; then we check if the color of a card is either black or red; lastly we check if there aren't colors other than black and\or red
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM card c, types t, colors cl1, colors cl2
WHERE c.name=t.name
  AND t.type = 'Enchantment'
  AND
    (SELECT m.black+ m.blue+ m.colorless+ m.green+ m.red+ m.snow+ m.white
     FROM mana_cost m
     WHERE m.id = c.mana_cost) = 6
  AND cl1.name = c.name
  AND cl2.name=cl1.name
  AND (cl1.color = 'Black'
  OR cl2.color = 'Red')
  AND NOT EXISTS(SELECT 1
                 FROM colors cl
                 WHERE c.name=cl.name
                   AND cl.color
                     IN ('Blue', 'Green', 'White'));
