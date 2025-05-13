-- 11. Find all meld cards of which you are the second
-- It's enough to join a card and a meld card on the 'second' field
-- Distinct is used to avoid duplicates
EXPLAIN ANALYSE -- This command is used to examine the efficiency of the query 
SELECT DISTINCT c.*
FROM meld_card m1, card c
WHERE m1.second=c.name;

