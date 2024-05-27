Problem Statement: To find all employee who have a bonus less than 1000.

For example:

```
Input:
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
Output:
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
```

Language Used: SQL

Algorithm used:

We select employee name from the table `Employee` and bonus from `Bonus` table. We then `LEFT JOIN` both the tables on condition `empID` present in both tables. Then, we filter using `WHERE` clause where Bonus is either less than `1000` or `NULL`.

Code Performance:

Runtime: 1581ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
