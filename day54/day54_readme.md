Problem Statement: To fix the casing of names in the table `Users`.

For example:

```
Input:
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

Language Used: SQL

Algorithm used:

We start by selecting user_id, and concacting the two substrings extracted from the `name` column by `lower` and `upper` casing the names, as seen appropriate, also using `ORDER BY` clause to arrange the orders.

Code Performance:

Runtime: 618ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
