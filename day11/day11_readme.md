Problem Statement: To find all numbers that appear at least three times consecutively from `Logs` table.

```
Example:

Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

```

Technique Used: SQL, JOIN

Approach:

We start by `SELECT`ing num column from table `LOG L1` using `DISTINCT` keyword. This avoides selecting repeating values. We create three aliases of `Log` table as L1, L2, L3 and `JOIN` them, to make sure we have three consecutive rows and in same value. Then, we use `li.num = l2.num AND l1.num = l3.num` condition to make sure all three rows have same values. This way we select three consecutive rows with same values.

Performance:

Time Complexity: 461ms
Space Complexity: -

Note: These performances are tracked on online compiler and can vary.
