Problem Statement: To find middle of a linked list.

For example:

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

Language Used: Python

Algorithm used:

We declare two variables, one to track end of list and one to track middle of list. So, the approach is the end list var will move twice as fast as mid var. This will cause the end var to reach end of list while the mid var will be in the middle of list hence finding the middle of list. Then, we will just return the middle variable.

Code Performance:

Runtime: 31ms
Memory: 16.49MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
