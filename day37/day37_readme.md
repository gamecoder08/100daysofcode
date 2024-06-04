Problem Statement: To find the length of highest possible palindrome in a string.

For example:

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

Language Used: Python

Algorithm used:

We create an empty set using `set()` function to track the elements in the string. We then start string traversal. On each char of string, we check if that char exists in set or not. If it does, it means it contributes to the length of palindrome and length is increased by 2. If it doesn't, it gets added to the set. Upon whole traversal of string, if any element remains in the set, it means it must have been a middle element since all others could have been encountered twice. Thus, we add 1 to the length. Then, we return the string length as result.

Code Performance:

Runtime: 32ms
Memory: 16.48MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
