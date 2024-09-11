Problem Statement: To delete a given node from a singly linked list without having access to head node.

```
Example:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

```

Technique Used: Linked List

Approach:

We actually need to remove the current value from the linked list. So, without having access to data we directly cannot remove current node. So, we copy the `next` node's value in the current node. And then, we bypass the next node using `node->next = node->next->next`.

Performance:

Time Complexity: 5ms
Space Complexity: 12.79MB

Note: These performances are tracked on online compiler and can vary.
