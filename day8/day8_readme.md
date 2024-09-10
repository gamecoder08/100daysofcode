Problem Statement: To find the second highest distinct salary from the Employee table. If there is no second highest salary, return null.

```
Example:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

```

Technique Used: SQL, `NOT IN`

Approach:

We start from inner query which retrieves the highest salaries from the table. Then, the outer query again reruns it essentially rejecting highest salary using `NOT IN` and thus returning second highest salary.

Performance:

Time Complexity: 221ms
Space Complexity: -

Note: These performances are tracked on online compiler and can vary.
