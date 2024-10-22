Problem Statement: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

```
Example:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

Technique Used: HashSet

Approach:

We start by initialising a hashset with values of `nums1`. We create an empty vector, `res` to return as result. Now, we start a loop over `nums2` using ranged `for()` loop. Inside it, we check if each element already exists in the set or not. If it is, we `push_back()` it into `res` and `erase()` that element from set to avoid duplicates. At last, return `res`.

Performance:

Time Complexity: 0ms
Space Complexity: 13.62MB

Note: These performances are tracked on online compiler and can vary.
