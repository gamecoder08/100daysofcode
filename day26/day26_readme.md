Problem Statement: Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

```
Example:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

```

Technique Used: Binary Tree, DFS, BFS

Approach:

We start by creating a base function, to check if `root` is `NULL`, if it is, the code returns `false`, indicating there can be no path there. Then, we check if the `left` and `right` subtrees of `root` are `NULL`, indicating the node is leaf node. We also check in same conditon with `&&`, if `targetSum` subtract `val` of current node, will result in `0`, if yes, we return `true`, indicating a path has been found. If none of these conditions are fulfilled, we recursively call the function on each of subtrees, `left` and `right`using `||`, with new targetSum as `targetSum` - `val` of current node. The logic is to recusively run same function for each tree, with the subtracted target value, so that if a path is found, the value will eventually become `zero`. So, in whichever subtree returns `true`, using `||`, we will return `true` eventually.

Performance:

Time Complexity: 4ms
Space Complexity: 20.00MB

Note: These performances are tracked on online compiler and can vary.
