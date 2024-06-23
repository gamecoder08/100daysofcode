Problem Statement: To find the score of a string.

Explaination:

The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

For example:

```
Input: s = "hello"
Output: 13
Explanation:
The ASCII values of the characters in s are: `'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
```

Language Used: C++

Algorithm used:

We use C++ internal property of `int()` function to obtain ASCII value of characters. We declare necessary variables, such as `length`, `score`, etc. We start loop traversal through `index = 1` to last index. This is to avoid, out of scope/range error. We then obtain ASCII values of element on ith index and i-1th index, substract it, and add the positive value to `score` variable, initially initialized as `0`. We then return the `score` variable.

Code Performance:

Runtime: 0ms
Memory: 7.98MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
