Problem Statement: To display the names of Customered who are not referred by ID `2`.

For example:

```
Input:
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

Language Used: SQL

Algorithm used:

We select the customer's name from the table `Customer` using `SELECT` clause and then filter using `WHERE` clause. The condition to filter is if `reference_id` is either not equal to `2` or is `NULL`.

Code Performance:

Runtime: 894ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
