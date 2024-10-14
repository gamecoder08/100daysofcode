Problem Statement: Given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

```
Example:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

```

Technique Used: Doubly Linked List, DFS

Approach:

We start by adding the base case, if `head` is `NULL`, we simply return `NULL`. Now, we create a `ptr`, temporary node to traverse the list and a `stack`, to store the values of `next` pointers of any node whenever a `child` pointer appears. We start by traversing the list using `while()` loop and ptr = `ptr->next` technique, if there is a `child` pointer set to `NOT NULL`, meaning there is a child list there, we `push()` that node's `next` in the stack, if it exists. Then, we switch the node pointers and merge the child list into the main list. We create another `if` condition, whenever there is `ptr->next` being `NULL` and `stack` being not empty, means we are at the end of a list in the child linked list. Then, we take the `top()`, node from stack and merge it into the list and then `pop()` it out of stack. The traversal continues. This will merge all the remaining lists after their respective child lists get merged and exit the loop. At last, we return `head` of the new list.

Performance:

Time Complexity: 0ms
Space Complexity: 10.52MB

Note: These performances are tracked on online compiler and can vary.
