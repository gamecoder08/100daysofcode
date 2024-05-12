Problem Statement: To return a the largest number from the single appearing numbers.

For example:

```
Input:
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation:
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order.
So the result is customer_number 3.
```

Language Used: SQL

Algorithm used:

We group the table by customer number and then count the customer orders. After sorting it in descending order, we print the value.

Code Performance:

Runtime: 798ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
