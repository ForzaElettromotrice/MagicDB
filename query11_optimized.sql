-- 11. Find all meld cards of which you are the second
-- We can optimize this query by selecting only the fields we are interested in; not using distinct since there are no duplicates; and doing an inner join to avoid 'where' conditions
EXPLAIN ANALYSE
SELECT c.name
FROM card c
         JOIN meld_card m ON m.second=c.name
