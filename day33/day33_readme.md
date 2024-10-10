Problem Statement: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

```
Example:

Input: head = [1,2,2,1]
Output: true
```

Technique Used: Linked List, Stack

Approach:

We start by creating a stack to store values of Linked list in it. We traverse the list once and `push()` all the values inside the stack using a `temp` node to traverse the list. Then, we move `temp` back to `head`. We again start a traversal using `while()` loop but this time we also compare each values with `top()` of stack. If any values mismatches, the code returns `false`. But, if value is same. That value if `pop()` from the stack. After exiting the loop, if loop exists due to condition, thus traversing the list as a whole, we return `true`.

Performance:

Time Complexity: 166ms
Space Complexity: 126.04MB

Note: These performances are tracked on online compiler and can vary.
