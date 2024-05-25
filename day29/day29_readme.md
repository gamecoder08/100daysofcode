Problem Statement: To find if a Linked list is Looping or not.

For example:

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

Language Used: Python

Algorithm used:

We use double pointer approach here, the same approach I used a few ques back. One pointer moves faster than another. If both pointer eventually meet at a node, this means the Linked List is a loop. Else, the code returns False when list is finished.

Code Performance:

Runtime: 39ms
Memory: 18.86MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
