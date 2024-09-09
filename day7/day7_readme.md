Problem Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.

```
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

Technique Used: Linked List, Two Pointers, Dummy head Pointer

Approach:

We start by declaring a dummy head pointer with `0` as a value at start of head to handle edge cases. Then, we create a secondary `dummy` pointer to traverse through list. We then move `head` pointer by `n` spaces using a `for()` loop. The, we move both the pointer `head` and `dummy` to the end of list until `head->next` is `NULL`. This makes that `dummy` pointer is behind `n` spaces at the list. Then, we bypass the deletion node and return `res->next`. `res->next` because original list didn't had that extra `0` value, so we need to remove that.

Performance:

Time Complexity: 4ms
Space Complexity: 14.66MB

Note: These performances are tracked on online compiler and can vary.
