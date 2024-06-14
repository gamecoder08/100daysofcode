Problem Statement: To find the length of the last word in a string.

For example:

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

Language Used: C++

Algorithm used:

We start with initializing a variable to store length of string and a counter boolean which will track the status of counting. We start a reverse `for` loop from the end of string, and start comparisons. If the char at current iteration is not a blank space, the length gets incremented by 1. If we encounter a blank space, the loop breaks and returns the length as result.

Code Performance:

Runtime: 0ms
Memory: 7.66MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
