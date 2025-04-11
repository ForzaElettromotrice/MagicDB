-- 11. Find all meld cards of which you are the second
EXPLAIN ANALYSE
SELECT c.name
FROM card c
         JOIN meld_card m ON m.second=c.name