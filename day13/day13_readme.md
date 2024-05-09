Problem Statement: To return the product of the two highest integers` - 1` from a list.

For example:

```
Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
```

Language Used: Python

Algorithm used:

Python's `sort()` function is used to sort the list, then the two highest numbers from the last two indices in the sorted list are returned after subtraction and multiplication.

Code Performance:

Runtime: 50ms
Memory: 16.62MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
