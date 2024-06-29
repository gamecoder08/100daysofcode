Problem Statement: To repeatedly add all the digits of a number until the result has only one digit, and return it.

Explaination:

-

For example:

```
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
```

Language Used: C++

Algorithm used:

We will take the recursive approach for this question. Another function `sum` is created which would be called upon recursion until main condition is fulfilled. We start a while loop through the input number, and add it's digit to a `summ` variable initially initialized as `0`. Then, we check if `summ` is a single digit number or not. If it is, we return it, else the function is again called.

Code Performance:

Runtime: 0ms
Memory: 7.26MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
