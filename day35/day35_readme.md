Problem Statement: To find name of employee who earn more than their manager.

For example:

```
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
```

Language Used: SQL

Algorithm used:

We start by selecting `name` as `Employee` from table `Employee` stated as `e1`. Then, e1 is `INNER JOIN` with Employee table again as `e2` using `ON` clause for condition as `e1.id=e2.managerID`. Then, filtering is done using `WHERE` clause based on condition `e1.salary<e2.salary;`.
Code Performance:

Runtime: 680ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
