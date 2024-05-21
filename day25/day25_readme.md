Problem Statement: To delete the nodes from a linked list if a matching value is found.

For example:

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

Language Used: Python

Algorithm used:

We start with checking if the head node is empty or not. If it is, the code returns `head` back. Then, we check if the head node contains the value itself or not. Then, we start the traversal of linked list using `while` loop with condition if `temp.next` exists and if value matches. If it does, the `temp.next` jumps the node from `next` to `next.next`, thus deleting the node. After the whole traversal, the code returns `head`.

Code Performance:

Runtime: 39ms
Memory: 19.42MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
