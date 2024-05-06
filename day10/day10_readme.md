Problem Statement: To return a duplicate email from the a table.

For example:

```

Input:
Person table:
+----+---------+
| id | email |
+----+---------+
| 1 | a@b.com |
| 2 | c@d.com |
| 3 | a@b.com |
+----+---------+
Output:
+---------+
| Email |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.

```

Language Used: SQL

Algorithm used:

The required fields are selected and both tables or relations are joined using `LEFT JOIN` based on `personID` attibute present in both relations.

Code Performance:

Runtime: 841ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
