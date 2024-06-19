Problem Statement: To find the index of first occurence of a string (`needle`) in another string (`haystack`).
For example:

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

Language Used: C++

Algorithm used:

We use `find()` function to directly find the occurence of the string, since it returns the index of first occurence or `-1` if none.

Code Performance:

Runtime: 0ms
Memory: 7.69MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
