Problem Statement: To add two numbers from a Linked list stored in a reversed order.

For example:

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

Language Used: Python

Algorithm used:

We start with assigning a dummy head. Then, the approach is to traverse both Linked list at same time and add the values of the node and store it next to the dummy node and move dummy node forward. We also take in mind about carry using `//` operator. After the calculation, we return the `result` pointer which would also be the head of Linked list storing the sum.

Code Performance:

Runtime: 50ms
Memory: 16.62MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
