Problem Statement: Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.

```
Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

Technique Used: Stack

Approach:

We start by declaring two `character` stacks for each string. We then iterate through the strings and `push()` each element into the stack. If the element is `#`, an element is `pop()` from the stack, if the stack is not empty. If it is empty, then we just `continue` forward. At the end, both stacks are compared and result is returned.

Performance:

Time Complexity: 0ms
Space Complexity: 8.23MB

Note: These performances are tracked on online compiler and can vary.
