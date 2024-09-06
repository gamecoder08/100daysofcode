Problem Statement: Given the head of a linked list, rotate the list to the right by k places.

```
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

Technique Used: Linked List, Circular Linked List

Approach:

We start by removing the base cases of linked list having no elements or single element or no rotation needed, since the list will remain same. Then, we start traversing the linked list to find the size of the list. Since, question can ask for rotations larger than size of list, we go for `k % n` approach, where `k` is no of rotations and `n` is size of list. This will bring down no. of rotations to managable size since larger than list means a full rotation is certainly completed and will be a waste of space and time doing it. Then, we find a new `k` by doing `k % n` and if `k` is equal to `0`, we again return `head` since, this means a full rotation was needed and there will be no changes in the linked list. Now, we do another traversal to find new tail and head of list using `while()` loop till `k - len`. There, we connect the `tail` from the `head` of linked list making it a circular linked list. Then, we assign `head` to `curr->next`, making the next node as required `head` and assigning `curr->next=nullptr` breaking the linked list again back to singly linked list. We then, return the new `head`.

Performance:

Time Complexity: 3ms
Space Complexity: 16.60MB

Note: These performances are tracked on online compiler and can vary.
