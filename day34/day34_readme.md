Problem Statement: To find the followers of a user according to the following id provided.

For example:

```
Input:
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
Output:
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
Explanation:
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}
```

Language Used: SQL

Algorithm used:

We are selecting the user's id and counting follower's id as `followers_count` using `count()` function from the table `FOLLOWERS`. Then, we are grouping by `user_id` and ordering by the same in order to filter out duplications from the table.
Code Performance:

Runtime: 1096ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
