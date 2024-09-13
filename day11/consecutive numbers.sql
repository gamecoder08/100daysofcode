-- Leetcode Solution: 

-- SELECT DISTINCT l1.num AS ConsecutiveNums 
-- FROM Logs l1
-- JOIN Logs l2 on l1.id = l2.id-1
-- JOIN Logs l3 on l1.id = l3.id - 2
-- WHERE l1.num = l2.num AND l2.num = l3.num;