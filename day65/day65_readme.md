Problem Statement: To reverse an integer or return `0` if the number or output is outside 32 bit integer range.

Explaination:

Range: [0,900]
Input: 359 #Acceptable input
Output: 953 #Out of range output. Should return `0`.

For example:

```
Input: x = 123
Output: 321
```

Language Used: C++

Algorithm used:

We will use `while()` loop to reverse the integer and at each point, we will check the overflow. We start with initializing a variable `result` equal to zero. We start traversal through the input number. We check if the current `result` is after `INT_MAX` OR below `INT_MIN`. If it is, we return `0`. Then, we slice the number and take the digit at one's position and add it in result. Then, we slice the input number and continue with the loop. After the loop, if `0` is not returned, we return the number `result`.

Code Performance:

Runtime: 0ms
Memory: 7.58MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
