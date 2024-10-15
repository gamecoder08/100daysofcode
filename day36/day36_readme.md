Problem Statement: A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

To construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

```
Example:

head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

```

Technique Used: Modified Doubly Linked List.

Approach:

We start by adding the base case, if `head` is `NULL`, we simply return `NULL`. Now, we create a `temp`, temporary node to traverse the list. We start by traversing the list using `while()` loop and `temp = ptr->next` technique. We create a `newNode()` inside every iteration and initialize it with `temp->val` and insert it at `temp->next`. This modifies the whole new list and creates a copy of each node with exact same node values. We then move `temp` back to `head`. And create another `while()` loop for traversal, since this time we need to assign the `random` pointer to each copied nodes. We go through each node in original list and assign `random` node using `temp->next->random = temp->random->next` to each of copied nodes. This makes the `random` pointer of each node to point towards the copy version of the orignal node. Now, we create a `newHead` node pointer and assign it as the head of new list using `head->next`. We then, do a traversal through the list, disconnecting the nodes and joining the copied nodes together using a temporary `copyNode` variable. At last, we return `newHead`.

Performance:

Time Complexity: 3ms
Space Complexity: 14.60MB

Note: These performances are tracked on online compiler and can vary.
