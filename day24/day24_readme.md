Problem Statement: Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```
Example:

Input: root = [3,9,20,null,null,15,7]
Output: 3

```

Technique Used: Binary Tree, Bottom - Up

Approach:

We start by creating the base case of if `root` is `Null`, we return `0` as height. Then, we create two depth variables, `leftDepth` and `rightDepth`, for left and right subtrees and recusrively calling the main function for each of the subtrees, respectively. Then, we return the `max()` of the both depths with a summation of `1` as the height of root, of the particular tree/subtree as the result of function.

Performance:

Time Complexity: 2ms
Space Complexity: 17.70MB

Note: These performances are tracked on online compiler and can vary.
