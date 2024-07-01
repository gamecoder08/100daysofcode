Problem Statement: To find the employees whose manager left the company

For example:

```
Input:
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
Output:
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

Explanation:
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel's manager is employee 11, who is still in the company (Joziah).
Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
```

Language Used: SQL

Algorithm used:

We use nested `SELECT` in this approach. We start by selecting `employee_id` from the `employees` table of those employees whose salaray is lesser than 30000 `and` whose `manager_id` is `not in` employee_id selected from `employees`. The result is ordered by employee_id.
Code Performance:

Runtime: 268ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
