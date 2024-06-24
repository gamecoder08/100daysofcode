Problem Statement: To find first login of players from Acitivity table.

For example:

```
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```

Language Used: SQL

Algorithm used:

We take normal rows and columns approach. We `select` the playe id and the `min` of event date as first login from the `Activity` table and grouping by player_id.

Code Performance:

Runtime: 531ms
Memory: NA

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
