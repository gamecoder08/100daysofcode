Problem Statement: To find customers who never order from joining two tables.

For example:

```
Input:
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

Language Used: SQL

Algorithm used:

Here, we will use nested `SELECT`. We start by selecting `customers` from the table customers `where` the `id` is not in the selection (`SELECT`) made of customerid from orders table.

Code Performance:

Runtime: 894ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
