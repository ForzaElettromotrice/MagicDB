-- 9. Find all creatures with power higher than defense, green with Trample, Vigilance and cost >= 3
EXPLAIN ANALYSE
SELECT c.name
FROM card c
         JOIN types t
              ON c.name=t.name AND t.type='Creature'
         JOIN colors cl
              ON cl.name=c.name AND cl.color='Green'
         JOIN attack_characteristics ac1
              ON ac1.name=c.name AND ac1.characteristic='Trample'
         JOIN attack_characteristics ac2
              ON ac2.name=c.name AND ac2.characteristic='Vigilance'
         JOIN tot_mana m
              ON m.id=c.mana_cost AND m.tot > 2
WHERE c.power>c.defense;