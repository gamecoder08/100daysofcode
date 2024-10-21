Problem Statement: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

```
Example:

Input: nums = [4,1,2,1,2]
Output: 4

```

Technique Used: XOR

Approach:

We start by initialising a variable `0`. Using a `for()` we traverse through each element of the given list, and `XOR` to each and every value of array. If the value is repeated, it will eventually cross itself and cancel it out as `0`, thus leaving the `result` containing the single number.

Performance:

Time Complexity: 0ms
Space Complexity: 19.58MB

Note: These performances are tracked on online compiler and can vary.
