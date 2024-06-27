Problem Statement: To determine if a number is `ugly`.

Explaination:

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

For example:

```
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
```

Language Used: C++

Algorithm used:

We first filter out the negative numbers and zero, since they cannot be ugly numbers. Then, we create an array of prime numbers: `2,3 and 5`. We run a loop through this array, and divide the number by each and every element. If the number is only divisible by these nums, the number should be reduced to 1. And thus, we check if the final number is 1 or not.

Code Performance:

Runtime: 0ms
Memory: 7.20MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
