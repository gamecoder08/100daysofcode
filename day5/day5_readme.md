Problem Statement: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

```
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

Technique Used: Linked List, Slow & Fast Pointer (Floyd's Cycle Detection Algorithm)

Approach:

We start by declaring a `slow` and `fast` pointer. We create a `while()` loop to check if a loop exists or not in the linked list. The traversal speed for `fast` is `fast->next->next`, while for `slow` it is `slow->next`. The loop runs as long as `fast` and `fast->next` are not `NULL`. Or `slow` and `fast` meet at a node. Either way the loop will break. Then, we check if `fast` and `fast->next` are `NULL` or not. If they are, this means the loop broke because of reaching the end of tail and there is no loop. Else, it means their is a loop and `while()` loop broke because `slow` and `fast` meet at a point. Then, we run another `while()` loop until `slow` and `head` meet. We traverse both the head one step at a time until they meet. When they meet, the loop breaks and `head` is returned. Both pointer `head` and `slow` will meet at the start of loop since the distance needed to complete the loop and from start of list to start of loop is same.

Performance:

Time Complexity: 3ms
Space Complexity: 10.38MB

Note: These performances are tracked on online compiler and can vary.
