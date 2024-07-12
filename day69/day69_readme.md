Problem Statement: To implement `pow()` function, without using it.

Explaination:

-

For example:

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

OR

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

Language Used: Python

Algorithm used:

We use recursive approach for this question. First, we return the base case of `n` being `0`, then returning 1 as number. Then, if power `n` is negative, we use exponent operator `**` to calculate the positive power of reciprocal of `x`. Then, the funtion checks if power `n` is odd or even. If it's odd, it again calls the function with power reduced by `1` and returns it after multiplying by `x`. If it's even, the function is called again by half the power and the result is squared and returned. This is done, in order to reduce total no of multiplications required.

Code Performance:

Runtime: 33ms
Memory: 16.66MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
