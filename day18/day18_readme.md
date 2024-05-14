Problem Statement: To return display the class with students more than 5.

For example:

```
Input:
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output:
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation:
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
```

Language Used: SQL

Algorithm used:

We group the table by class and then count the student and filter using `having` clause. Then, we display the class from Courses table.

Code Performance:

Runtime: 617ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
