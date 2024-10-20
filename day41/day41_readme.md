Problem Statement: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```
Example:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

```

Technique Used: HashMap, Array/Vector

Approach:

We start by creating an empty hashset object. Using a `for()` we traverse through each element of the given list, and insert it in hashSet. Before inserting, we check if the element is already in hashSet or not, if it is, we return `true`, meaning there are duplicates in list. After the loop, if loop runs succesfully, we return `false`, meaning there were no duplicates in the list.

Performance:

Time Complexity: 34ms
Space Complexity: 73.22MB

Note: These performances are tracked on online compiler and can vary.
