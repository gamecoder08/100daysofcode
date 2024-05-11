
-- Leetcode Code: 

WITH filtersinglenums as (
    SELECT *
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
SELECT MAX(num) AS num FROM filtersinglenums