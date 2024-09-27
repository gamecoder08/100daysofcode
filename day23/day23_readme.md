Problem Statement: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

```
Example:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

```

Technique Used: Binary Tree, DFS

Approach:

We start by creating an empty `vector`, `traversal` which will store more vectors with values of each level. Then, we return a base case, if `root` is `NULL`, then we return the empty vector. Also, we create a `queue` which will keep track of nodes in bfs order. We push the `root` into the `queue`. Then, we start a `while()` loop, while the queue is not empty. Then, we create a secondary `vector`, `currLevel` to store values of current level. We, get the queue size, and run a `for()` loop, until the size, thus until the size of current level. We get the top node of queue using `front()` and `pop()` it out. We push the value of current node to `currLevel`. Then, we check if the `left` and `right` nodes of current nodes are not empty. If they aren not, then they are pushed into queue. After the `for()` loop, we push the `currLevel` vector to the empty vector,`traversal`. Then, the whole cycle continues, traversing each level and storing the values of each node. When all the loop exists, we return `traversal`.

Performance:

Time Complexity: 3ms
Space Complexity: 15.19MB

Note: These performances are tracked on online compiler and can vary.
