Problem Statement: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
Example:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

Technique Used: Array, Vector, DFS, Matrix

Approach:

We start by taking the size of `grid` matrix which is the input. We create another vector matrix, `vis`, which will track all the visited points in the matrix. Also, a `count` variable is initialized to `0`, which will track no. of islands found. Then, we start traversal through each nodes in the `grid` matrix using nested `for()` loop. Whenever we encounter a cell with value `1` and is not entered in `vis`, we call our helper function `dfs` and increment `count` by 1. In the `dfs()` function, it takes `grid`, `vis`, `i`, `j`, `n` and `m` as input parameters. If the cell entered is out of range, or is already visited, or is equal to `0` in `grid`, we simply return. Else, the cell is marked as `1` in `vis` matrix. We also recusively call the function for each cell above & below and in neighbours to find all the cells with value `1`, thus visiting the complete island. In the main function, when the nested loop exits, we simple return `count`, since it tracks the no. of islands.

Performance:

Time Complexity: 24ms
Space Complexity: 16.94MB

Note: These performances are tracked on online compiler and can vary.
