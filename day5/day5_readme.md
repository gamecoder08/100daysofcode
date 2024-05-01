Problem Statement: To reverse a prefix in a word and then return the word.

For example:

```
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
```

Language Used: Python

Algorithm used:

First, an if condition checks if `ch` exists in `word` or not. If not, it returns the `word`. Then, a loop is run throughout the whole string. When the ith variable is equal to `ch`, then the loop breaks and `i` is stored as first occurence of ch. Then, the algorithm breaks the string and returns the string using string slicing after concatation.

Code Performance:

Runtime: 36ms
Memory: 16.56MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
