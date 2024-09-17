Problem Statement: Given the root of a binary tree, return the preorder traversal of its nodes' values.

```
Example:

Input: root = [1,null,2,3]

Output: [1,2,3]

```

Technique Used: Binary Tree, Stack

Approach:

We start by initialising an `<int>` vector in the `private` space of class. Then, we create an `preorder()` void function which will be the main traversal function. We add the base case which is if the `root` is `NULL`, then we simply `return`. Then, we push the data of the current node into the vector we created earlier. Then, we recursively call the function for `root->left` branch of tree. Then, we again recursively call the function,this time for `root->right`. Then, in the main function `preorderTraversal()`, we simply call the `inorder()` function. Then, we return `vec` as the resultant answer.

Performance:

Time Complexity: 0ms
Space Complexity: 10.14MB

Note: These performances are tracked on online compiler and can vary.
