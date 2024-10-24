Problem Statement: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```
Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

Technique Used: hashMap

Approach:

We start by declaring a `hashMap` for storing each element and its index. We start a `for()` loop through the vector array. We calculate the `complement` by subtracting number on each the current index from the `target` number, each iteration. We find if the `complement` exists in the current hashMap. If it does, it returns the `index` of the current complement and the index of other number from the nums, thus the iterator. Outside, `if()`, we add the current element and the index to the hasMap if nothing returns. After the loop completes, we return an empty vector, `{}`, since no two desired numbers were found.

Performance:

Time Complexity: 3ms
Space Complexity: 14.46MB

Note: These performances are tracked on online compiler and can vary.
