-- SQL script that lists the number of records with the same score
-- The result displays score and number of records
-- Sorted by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;