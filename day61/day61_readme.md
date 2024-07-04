Problem Statement: To find the a number is a power of `4` or not.

For example:

```
Input: n = 16
Output: true
```

Language Used: C++

Algorithm used:

We will use recursive approach for this question. First to filter out base cases, we check if the number is either equal to `1` or is even divisible to `4` or not, and return `true` and `false` accordingly. Also, for final case, we check if number is lesser than `8`, and if it is equal to `4`, then return `true`, else return `false`. Now, we initialise a variable with dividing the number by `4`, and then call the function again with the initialised variable as the new argument. The code check if the number is power of two or not by recursive division.

Code Performance:

Runtime: 0ms
Memory: 7.19MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
