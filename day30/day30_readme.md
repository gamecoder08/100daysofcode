Problem Statement: To find all dates where the temperature is higher than previous day.

For example:

```
Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation:
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
```

Language Used: SQL

Algorithm used:

We select `id` from the table and join the table from the second table using `JOIN` clause and then we filter using `WHERE` clause and using `DATEDIFF` function to find the difference between dates `AND` comparing both temperatures.

Code Performance:

Runtime: 778ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
