Problem Statement: To return display the class with students more than 5.

For example:

```
Input:
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
Output:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
Explanation:
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
```

Language Used: SQL

Algorithm used:

We select all the rows from the table. We filter it using `where` clause and by equating and using `mod()` function to find odd numbers. Then, filtered rows are displayed in descending order based on `id` attribute using `order by` clause.

Code Performance:

Runtime: 382ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
