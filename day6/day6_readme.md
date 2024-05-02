Problem Statement: To find a largest postive number that exists with it's negative counterpart in an array/list. It return `-1` if such number doesn't exist.

For example:

```
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
```

Language Used: Python

Algorithm used:

First, we determine the return value in a variable directly as -1 since that is the least value to return. Then, the list is converted into a set since iterating over a set is efficient than list since sets are applied using hash tables. The code checks if the iterate is greater than zero as well as if it is greater than the current largest. It also checks if the negative counterpart exists in the list or not. After that all, the variable is returned.

Code Performance:

Runtime: 144ms
Memory: 16.75MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
