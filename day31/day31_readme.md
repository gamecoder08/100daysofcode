Problem Statement: Given the head of a singly linked list, reverse the list, and return the reversed list.

```
Example:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```

Technique Used: Linked List, Three pointer

Approach:

We start by creating three temp nodes, `curr`, `nextt` and `prev`, to track current node, prev node and next node respectively. We then start a `while()` loop until,`curr` node is not equal to `NULL`. We start by reassigning `nextt` to `curr->next`. Retrack `curr` node's `next` to `prev`. Then, we shift `prev` to `curr` node. And lastly we assign `curr` node to `nextt` node, indicating moving forward in original list, while also reversing nodes previous to `curr` node.

Performance:

Time Complexity: 2ms
Space Complexity: 13.00MB

Note: These performances are tracked on online compiler and can vary.
