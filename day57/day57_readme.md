Problem Statement: To find the missing integer from the array[0, n] of size `n`.

Explaination:

-

For example:

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

Language Used: C++

Algorithm used:

We start with initializing a variable with size of array. This integer will hold the final missing number. We start interating over the array using `for` loop. At each step, we add the index of current iterator and substract the number on that index from the variable. This done, to sneak out the missing value by applying the theory of `Expected sum` - `actual sum`. The addition of index represents the Expected sum, and subtraction of number represents the actual sum. This gives out the missing number in the array into the variable.

Code Performance:

Runtime: 11ms
Memory: 20.18MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
