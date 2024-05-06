Problem Statement: To return a duplicate email from the a table.

For example:

```
Input:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.

```

Language Used: Python

Algorithm used:

Email is grouped by using email and is selected from the table based on the sql function `count()`. The function is implemented as `count(email)>1`.

Code Performance:

Runtime: 621ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
