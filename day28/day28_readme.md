Problem Statement: To write a solution to find managers with at least five direct reports.

```
Example:

Input:
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output:
+------+
| name |
+------+
| John |
+------+

```

Technique Used: SQL, HAVING, COUNT

Approach:

We start by creating an inner query where we `select` `managerId` from `Employee` table `grpup by` managerId `HAVING` no of managerId greater than 4. This retrieves the `managerId`, which appears at least 5 times in the table, meaning 5 people under that person with that `managerId`. Then using outer query, we `select`, the `name` of employee whose `id` is equal to `managerId`.

Performance:

Time Complexity: 315ms
Space Complexity: -

Note: These performances are tracked on online compiler and can vary.
