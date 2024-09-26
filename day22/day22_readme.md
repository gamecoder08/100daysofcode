Problem Statement: Given the root of a binary tree, invert the tree, and return its root.

```
Example:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

Technique Used: Binary Tree, DFS

Approach:

We start by adding the base condition, if `root` is `NULL`, we return `NULL`. Then, we create a `temp` node, and assign the value of `root->left` node to it. Then, we assign `root->right` node to `root->left`. Then, we assign `temp` node to `root->right`, thus interchanging them. Then, we recursively call the function for `root->left` and `root->right` branch of tree. Then, at last, we return `root`.

Performance:

Time Complexity: 0ms
Space Complexity: 11.90MB

Note: These performances are tracked on online compiler and can vary.
