-- 5. Find the equippable artifact(s) with the highest mana cost
EXPLAIN ANALYSE
SELECT c.name, (m.red + m.black + m.white + m.snow + m.green + m.colorless + m.blue) AS cost
FROM mana_cost m, card c, types t, activable_characteristics a
WHERE m.id=c.mana_cost
  AND t.name=c.name
  AND a.name = c.name
  AND t.type = 'Artifact'
  AND a.characteristic = 'Equip'
  AND (m.red + m.black + m.white + m.snow + m.green + m.colorless + m.blue) = (
  SELECT MAX(m2.red + m2.black + m2.white + m2.snow + m2.green + m2.colorless + m2.blue)
  FROM mana_cost m2, card c2, types t2, activable_characteristics a2
  WHERE c2.mana_cost=m2.id
    AND t2.name=c2.name
    AND a2.name=c2.name
    AND t2.type = 'Artifact'
    AND a2.characteristic = 'Equip'
);
