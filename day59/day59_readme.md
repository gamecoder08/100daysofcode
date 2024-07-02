Problem Statement: To find the a number is a power of `3` or not.

For example:

```
Input: n = 27
Output: true
Explanation: 27 = 33
```

Language Used: C++

Algorithm used:

We will use recursive approach for this question. First to filter out base cases, we check if the number is either equal to `1` or is even divisible to `3` or not, and return `true` and `false` accordingly. Also, for final case, we check if number is lesser than `4`, and if it is equal to `3`, then return `true`, else return `false`. Now, we initialise a variable with dividing the number by `3`, and then call the function again with the initialised variable as the new argument. The code check if the number is power of two or not by recursive division.

Code Performance:

Runtime: 7ms
Memory: 8.08MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
