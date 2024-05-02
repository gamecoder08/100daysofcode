Problem Statement: To find string halves have equal number of vowels. It is case sensitive.

For example:

```
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
```

Language Used: Python

Algorithm used:

First the string is split into two words using string slicing. The, two loops are run through each slice and it counts the number of vowels in both of them and store them in two variables. It then compares both variables and returns `True` if they are equal else `False`.

Update: Code optimised a bit. Upon learning about `zip()` function in python. The new code zips the two words together since multiple iterations can be done in a single loop. This can increase perform and will make code a bit more efficient.

Code Performance:

Runtime: 41ms -> 39ms
Memory: 16.66MB -> 16.64MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
