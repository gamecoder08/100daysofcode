Problem Statement: To find largest 3 digit number in a string.

For example:

```
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

Language Used: Python

Algorithm used:

First run a loop through the string. Then, concate a string using the i element of a 3 digit number. Now ,the algo test whether this `test_str` is in the input string or not. If it is, it places it's value in a variable `largest_str` denoting largest number string. Then, a final if condition to check if the largest number is present in the input string or not, a test for assurity. If not, it returns an empty string. Else, the function returns the largest string.

Code Performance:

Runtime: 42ms
Memory: 16.57MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
