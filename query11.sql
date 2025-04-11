-- 11. Find all meld cards of which you are the second
EXPLAIN ANALYSE
SELECT DISTINCT c.*
FROM meld_card m1, card c
WHERE m1.second=c.name;

