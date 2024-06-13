Problem Statement: To find the sum of two numbers from an array equal to a target value.

For example:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Language Used: C++

Algorithm used:

We start with finding the length of array and storing it an initialized variable. Then, we run a double loop and find the summation of two values equal to the `target` value. The range for the inner loop starts with `i+1` instead of `0` to avoid multiple repeated comparisons saving time.

Code Performance:

Runtime: 45ms
Memory: 12.42MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
