Problem Statement: To delete duplicate e-mails from a table.

For example:

```
Input:
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
```

Language Used: SQL

Algorithm used:

We are using the `delete()` function in SQL in the table `person` if the condition mentioned with `where()` clause is fulfilled and if id is different.

Code Performance:

Runtime: 1380ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
