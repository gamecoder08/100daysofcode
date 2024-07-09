Problem Statement: To determine if a number is a perfect square or not.

Explaination:

-

For example:

```
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
```

Language Used: C++

Algorithm used:

We will use binary search for this question using logic that perfect root of a perfect square would be between the range `1` to `num`. So, we create two variables, pointing to lower end and higher end of range. We then find `mid` of range. We convert the mutiplication from `int*int` mulitplication to `long*long` mulitplication to avoid overflow. Then, we compare the `mid` and `num`. If they are equal, we return `true`. If it's not, in case of `mid` being greater we increase lower pointer with respect to `mid`, and in case of `mid` being smaller than `num`, we lower the value of higher pointer with respect to `mid`. The loop continues. If nothing is returned before completion of loop, we return `false`.

Code Performance:

Runtime: 0ms
Memory: 6.97MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
