Problem Statement: Given a string s.

Task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

```
Example 1:

Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.
```

Technique Used: List; Since Code requires a mixed implementation of Stack and queue.

Approach:

We start by calculating size of the string. Then, we start a loop through the string. We check if the current character is a digit or not using `isdigit()`. If it is, we `pop_back()` from the list and `continue` with loop. Else we add the character to the list. Then, we run a `while()` loop based on if list is `empty()` or not. Then, we concat the first character form the list to an empty string and `pop_front()` it. We repeat this process and return the string.

Performance:

Time Complexity: 0ms
Space Complexity: 8.84MB

Note: These performances are tracked on online compiler and can vary.
