Problem Statement: To find maximum product difference between two pairs.

For example:

```
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
```

Language Used: Python

Algorithm used:

In order to maximize the return value, the difference between the both numbers should be great. In order to achieve that, we can subtract the product of two highest integers with the product of the two lowest integers. So, we use the `sort()` function to sort the array. And then the value is returned which is received my the difference of product of last two indices with the product of first two.

Code Performance:

Runtime: 148ms
Memory: 17.90MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
