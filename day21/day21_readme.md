Problem Statement: To check if two strings are isomorphic.

For example:

```
Input: s = "egg", t = "add"
Output: true
```

Language Used: Python

Algorithm used:

Isomorphic strings are two strings in which all occurences of a character can be replaced with preserving their order. In the code, we use `zip()` functions's unique "zipping" property of two characters two characters, so order can be ultimately preserved and cannot be broken. Now, using `*` operator, we return a set of these pairs thus removing any duplicate values. We do the same for each string individually without using `zip()` function. This causes to return a set of unique characters in both the strings. Then, we compare the length of all three lists. The code return `True` if all three are equal, hence confirming same exchange between characters, and `False` otherwise.

Code Performance:

Runtime: 38ms
Memory: 16.73MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
