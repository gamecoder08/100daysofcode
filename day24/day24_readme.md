Problem Statement: To find median of two sorted arrays.

For example:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

Language Used: Python

Algorithm used:

We start with merging both the arrays into a single array using `+` operator. Then, we sort the list using `sort()` function. Then, we store the length of array to find mid point. Now, depending upon length of list, if even, the code returns average of both the mid values of list, and if odd, the code return the mid value as float.

Code Performance:

Runtime: 69ms
Memory: 16.88MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
