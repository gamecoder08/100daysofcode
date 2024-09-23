Problem Statement: To write a solution to find employees who have the highest salary in each of the departments.

```
Example:

Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

```

Technique Used: SQL, JOIN

Approach:

We start by `SELECT`ing the department name, employee name and salary from the tables, `Employee` and `Department` after `JOIN`ing them with department id as reference. From which, we filter out using `WHERE` clause the highest salary.
Performance:

Time Complexity: 557ms
Space Complexity: -

Note: These performances are tracked on online compiler and can vary.
