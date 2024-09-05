Problem Statement: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Write an algorithm with O(log n) runtime complexity.

```
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

Technique Used: Binary Search

Approach:

We start by calculating size of the vector. Then, we initialise two pointers, pointing `s` start and `e` end of search area respectively. Then, we start a `while()` loop until `s <=e`. We then find, the `mid` middle point. We check if the number at `mid` index is value or not, if it is, `mid` is returned, `else if` the `mid` is greater than the number, we shift `e` to `mid-1`, or `else` we shift `s` to `mid+1`. If nothing is returned until the loop ends, `-1` is returned.

Performance:

Time Complexity: 22ms
Space Complexity: 30.16MB

Note: These performances are tracked on online compiler and can vary.
