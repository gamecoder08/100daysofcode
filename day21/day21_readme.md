Problem Statement: Given a binary tree, determine if it is height-balanced.

```
Example:

Input: root = [3,9,20,null,null,15,7]
Output: true

```

Technique Used: Binary Tree, Post - Order Traversal

Approach:

We start by creating an independent function `checkHeight()` which takes root nodes as a parameter. The base case is if `node` is `NULL`, then we return `0`, since height of that particular node tree is zero. Then, we call this function recursively for each of the nodes, `left` and `right`, separately and return `-1`, if any height is found to be `-1`, meaning tree is unbalanced. We also check if the `abs()` difference of `leftHeight` and `rightHeight` is lesser than 1. If it is, this means tree is unbalanced, and thus we return -1. Now, if any of the return cases has not been followed. The function returns summation of `1` & `max()` of both the heights essentially returning the height of the node. Now, in the main `isBalanced()` function, we check if the above function returns true, if it does not, we return `true` meaning, tree is balanced, else we return `false`, meaning tree is unbalanced.

Performance:

Time Complexity: 7ms
Space Complexity: 21.84MB

Note: These performances are tracked on online compiler and can vary.
