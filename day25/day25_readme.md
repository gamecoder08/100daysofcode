Problem Statement: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

```
Example:

Input: root = [1,2,2,3,4,4,3]
Output: true
```

Technique Used: Binary Tree, DFS, BFS

Approach:

We start by creating a support function `isEqual()`, which checks if both nodes are equal or not. In this function, first is the base condition, if either of node is `NULL`, we return `n1==n2`, n1 and n2 being each nodes. This makes sure the tree is symmetric at that level. Then, we compare the values of each node, if the values as equal, we recursively call the function `isEqual()` and return the value, for left subtree of first node to right subtree of second node `&&` right subtree of first node to left subtree of second node. This compares both the subtrees, making sure they are symmetric. If nothing is returned, we return `false`. In the main function, `isSymmetric()`, we call the helper function for `root->left` and `root->right`, and essentially returning its value.

Performance:

Time Complexity: 3ms
Space Complexity: 17.53MB

Note: These performances are tracked on online compiler and can vary.
