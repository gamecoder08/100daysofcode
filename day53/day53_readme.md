Problem Statement: To determine if two same numbers in two different are apart by `k` difference.

For example:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Language Used: C++

Algorithm used:

We use unordered map to track any index which have appeared previously and it's value. We start a loop to traverse through the array. We do a comparison check if the current index num appeared anywhere in the array. If, it does appear and we find a value from the list satisfying the interval, we return `true`. If condition is not fulfilled, we add the num to the unordered_list. After the whole loop traversal, if nothing is returned, the algo returns `false`.

Code Performance:

Runtime: 116ms
Memory: 80.74MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
