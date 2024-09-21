Problem Statement: To write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

```

Technique Used: SQL, FUNCTION

Approach:

We start by creating a function to implement the workflow of this problem. It takes an `INT` value `n`, and returns an `INT` value. We then set the value to be `n=n-1` because, it the indexing in tables is from 0, and thus the number should be implemented accordingly. We then write function as `SELECT`ing `DISTINCT(salary)` from the `employee` table, and `order by` salary in `DESC`. This makes sure that there are no duplicate values involved and the table is sorted in descending order. We then set `LIMIT 1 OFFSET n` which fetches the value after skipping `n` places, which would be the required answer.

Performance:

Time Complexity: 367ms
Space Complexity: -

Note: These performances are tracked on online compiler and can vary.
