Problem Statement: To find the only number with the single occurence in a from an array.

For example:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

Language Used: C++

Algorithm used:

We use bitwise operator `XOR` to solve this problem. The property when any number XORed with `0` is number itself and any number XORed with itself is `0` is used here. We start with declaring necessary variables. Then, we run a `for` loop and apply `XOR` to each and every element. At the end, the number which is of single occurence is left since all others cancel each other out.

Code Performance:

Runtime: 11ms
Memory: 19.12MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
