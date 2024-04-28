Problem Statement: To return an array answer[i] according to the following index conditions:

```
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
```

For example:

```
Input: n = 3
Output: ["1","2","Fizz"]
```

Language Used: Python

Algorithm used:

Runs a loop till the nth number with `i` as variable. Checks whether `i+1` follows any of the above conditions. According to the fulfilled condition, the string is appended in an empty list.

Note: The arrangement of if conditions can change the answer drastically.

Code Performance:

Runtime: 45ms
Memory: 17.75MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
