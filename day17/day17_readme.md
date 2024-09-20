Problem Statement: Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

```
Example:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

```

Technique Used: Linked List, Math

Approach:

We start by creating a dummy node to mark the start of list and another `temp` node initialised through `dummy` node to mark the start of new list. We then initialise a `carry` integer which tracks the carry in summations. Then, we start a `while()` until the `head` of each list or `carry` is valid. Then, we check if each list has a valid node or not. If it has, it's `val` is added to an initialised `sum` integer. Then, we move that head forward. After checking both lists, we calculate carry. We then, calculate final sum needed to be added in a node. We then create a new node and attach it to `temp` node, to create a new list. We then interchange dummy and temp. And delete old dummy node (now as temp) to avoid memory leak. Then, we simply return the new `dummy` node since it's the new `head` of list.

Performance:

Time Complexity: 16ms
Space Complexity: 77.59MB

Note: These performances are tracked on online compiler and can vary.
