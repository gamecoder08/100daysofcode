Problem Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Return true if there is a cycle in the linked list. Otherwise, return false.

```
Example:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

```

Technique Used: Linked List, Two pointer

Approach:

We start by adding base case if either of `head`s are `NULL`, we return `NULL` directly without doing anything. Then, we create two nodes, `nodeA` and `nodeB` for traversal in each list. We start a `while()` loop until `nodeA!=nodeB`. Then, we create a conditon, we any of the node reaches the end point i.e. becomes `NULL`, it gets switched to the other list in order to make sure no. of nodes of traversal are same for both the nodes. With this logic, even if the lists are uneven, the nodes can cycle through and find the common node eventually if it exists. The loop will terminate in amy case, since if we find common node, both `nodeA` and `nodeB` will contain and return it, and if there is no common node, both `nodeA` and `nodeB` will be `NULL` and it will be returned.

Performance:

Time Complexity: 32ms
Space Complexity: 17.37MB

Note: These performances are tracked on online compiler and can vary.
