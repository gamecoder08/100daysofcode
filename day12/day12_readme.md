Problem Statement: Given an integer array nums, find the subarray with the largest sum, and return its sum.

```
Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

Technique Used: Largest Subarray, Kadane's Algorithm

Approach:

We start by initialising two integers `res` and `total`. `res` tracks the sum of max. subarray, while `total` tracks sum of current subarray. We then loop through the array `nums`. We then initially check if `total` is less than `0`, if it, we reset it back to `0` since, sum from negative number cannot yield max. subarray sum. Then, we add current element from `nums` to total. Then, from among `res` and `total`, whichever has greater value, it gets stored in `res`. At the end of loop, `res` is returned.

Performance:

Time Complexity: 63ms
Space Complexity: 70.39MB

Note: These performances are tracked on online compiler and can vary.
