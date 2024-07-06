Problem Statement: To guess the number is higher or lower.

For example:

To guess from a number from 1 to `n` using a pre - defined function, `guess()`.
The function returns:

    -1: guess is higher than the number(i.e. num > pick).
    1: guess is lower than the number(i.e. num < pick).
    0: guess is equal to the number(i.e. num == pick).

```
Input: n = 10, pick = 6
Output: 6
```

Language Used: C++

Algorithm used:

We use two pointer approach and binary search for this question. We start with a pointer at the bottom of list, one at a top and a variable at the middle of both the pointers. We start a `while` loop until the middle variable `num` is equal to `0`. We check if the guess() returns `-1`. If it does, we decrease value of higher pointer, else if it returns `1`, we increase value of higher pointer. Thus, changing mid again and again until it equal to picked number and while loop is exited. When the loop exits, we return the middle `num` variable.

Code Performance:

Runtime: 0ms
Memory: 7.11MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
