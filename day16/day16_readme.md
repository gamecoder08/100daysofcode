Problem Statement: Given the root of a complete binary tree, return the number of the nodes in the tree.

```
Example:

Input: root = [1,2,3,4,5,6]
Output: 6

```

Technique Used: Binary Tree, Recursion

Approach:

We are using direct recursion to solve this problem. We start by setting up the base case, which returns `0` if `root` is `NULL`. Then, we call the function recursively for `root->left` subtree and `root->right` subtree and add 1 for the root node in each cycle. Then, we return this summation.

Performance:

Time Complexity: 12ms
Space Complexity: 29.42MB

Note: These performances are tracked on online compiler and can vary.
