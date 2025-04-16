-- 5. Find the equippable artifact(s) with the highest mana cost
-- We can optimize this query by calculating the total mana cost with the view; using a inner join instead of multiple 'where' clauses; and instead of doing a nested query we can order by higher mana cost and just select the first element
EXPLAIN ANALYSE
SELECT c.name, m.tot as cost
FROM card c
    JOIN types t
        ON t.name=c.name AND t.type = 'Artifact'
    JOIN activable_characteristics a
        ON a.name=c.name AND a.characteristic='Equip'
    JOIN tot_mana m
        ON m.id=c.mana_cost
ORDER BY cost DESC
LIMIT 1;
