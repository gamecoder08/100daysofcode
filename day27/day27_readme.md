Problem Statement: Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

```
Example:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

```

Technique Used: Binary Tree, Postorder, Inorder

Approach:

We start by creating the main function `buildTree()` which initializes the construction process by calling the helper function `buildtree()`. First, it checks if inorder and postorder vectors are empty or if they have different sizes. If any of these conditions are true, the code returns `nullptr`, indicating that the tree cannot be built. In the helper function `buildtree()`, we begin by checking if the `start` index is greater than `end` or if idx has become less than 0, indicating that we have processed all elements or reached the end of a subtree. In such cases, we return `NULL`, representing an empty node. Next, we fetch the current root value from the postorder vector using the `idx` index, which is initialized to the last element of postorder. We then decrement `idx`, so that the next recursive call processes the next node in reverse order. We create a new `TreeNode` using the current value from postorder and check if it’s a leaf node by verifying if `start == end`. If it’s a leaf node, we return the newly created `node`. If it’s not a leaf node, we search for the position of the current root value in the inorder vector using the helper function `searchPos()`. This function iterates over the inorder vector between start and end to find the index of the current root. Once we find the position, we recursively build the right subtree first by calling buildtree with the range `pos + 1` to `end` (to cover elements on the right of the root). Then, we recursively build the left subtree by calling buildtree with the range `start` to `pos - 1`. Finally, after constructing the left and right subtrees, the current node is returned as the root of the subtree.

Performance:

Time Complexity: 7ms
Space Complexity: 26.76MB

Note: These performances are tracked on online compiler and can vary.
