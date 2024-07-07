Problem Statement: To move all the zeroes in the array to the end of array.

Explaination:

-

For example:

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Language Used: C++

Algorithm used:

We use two pointer approach for this question. We create a `left` pointer and a `right` pointer to traverse through the array. The `right` pointer traverses through the array as an interator, while `left` pointer is declared as at index `0`. Once the loop starts, at each every element `right` approaches, we check if the number is non-zero. If it's not, we `swap` the element to the postion of `left` pointer and increment `left` pointer. If the element is zero, the condition is ignored. Using this approach, we send all the non-zero elements to the `start` of the unsorted list. This way, all the zeroes come at the end of array.

Code Performance:

Runtime: 15ms
Memory: 21.58MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
