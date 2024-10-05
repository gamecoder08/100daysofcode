Problem Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

```
Example:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

Technique Used: Linked List, Slow - fast pointer

Approach:

We start by adding base case if `head` or `head->next` are `NULL`, we directly return `false`. Then, we create two node pointers, `slow` initialised at `head` and `fast` initialised at `head->next`. Then, we enter a `while()` loop, until `slow!=fast`. In loop, we check if `fast->next` or `fast->next->next` are `NULL`, if they are we return `false`. Then, we move `slow` one step ahead, while we move `fast` twice the step ahead. If loop, exits with base condition getting true, this means a loop exists, and we return `true`, after the loop.

Performance:

Time Complexity: 6ms
Space Complexity: 10.80MB

Note: These performances are tracked on online compiler and can vary.
