Problem Statement: To return a the largest number from the single appearing numbers.

For example:

```
Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output:
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6. Since 6 is the largest single number, we return it.
```

Language Used: SQL

Algorithm used:

We create a common table expresion(CTE) to filter out the numbers which are appearing one time only. From among that, the main query selects the maximum number.

Code Performance:

Runtime: 616ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
