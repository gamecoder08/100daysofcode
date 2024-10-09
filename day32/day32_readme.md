Problem Statement: Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

```
Example:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

Technique Used: Linked List, Three pointer

Approach:

We start by creating a edge case of if `head` is `NULL`, then we return `NULL`. Then, we create three `temp` nodes, `odd` at `head`, `even` at `head->next` and `evenHead` at `head->next`, to track odd nodes, even nodes and head of list even nodes respectively. We start a `while()` loop until `odd` and `odd->next` are not `NULL`. This allows to traverse through all nodes. We start by jumping nodes in `odd` list by using `odd->next = odd->next->next`. This jumps the adjascent even nodes, eseentially creating a list of only odd nodes. Then we do, `odd = odd->next` to go for next odd node. Similarly, we do same for even nodes, which will in turn create a list of even nodes being tracked by `evenHead` node. At last, when the loop exists, we join both the lists using `odd->next = evenHead`. Then, we return `head`.

Performance:

Time Complexity: 7ms
Space Complexity: 15.27MB

Note: These performances are tracked on online compiler and can vary.
