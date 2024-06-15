Problem Statement: To find the position of `target` value in an array or where it is supposed to be.

For example:

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

Language Used: C++

Algorithm used:

We start with initialising and finding length of array. We give an initial condition which makes sure if the `target` value is larger than array or not. If it is, it returns the length of array. Then, we start the traversal through the array. If the iterator is equal to the `target` value, it returns the index. Another comparison is done, if the first condition is not fulfilled. We find the first the number which is greated than `target` value and return that index, since that is were the value is supposed to be.

Code Performance:

Runtime: 3ms
Memory: 11.85MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
