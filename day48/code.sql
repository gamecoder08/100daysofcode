
-- Leetcode Code: 

SELECT name as customers from customers where id not in (SELECT customerid from orders)