Problem Statement: To find sum of square of two numbers.

For example:

```
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
```

Language Used: C++

Algorithm used:

We start with running a `for` loop from 0 till square is lesser or equal to `c`. This loop runs one of the numbers `a` as an interator, making sure it is valid. Then, we calculate b by reversing the formula `a^² + b² = c` as `sqrt(c - a² * a²)`. Then, we run a condition to check if `b` is integer or not. If it is, the code returns `true`. Else, after the loop ends, the code returns `false` if anything hasn't been returned.

Code Performance:

Runtime: 0ms
Memory: 6.98MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
