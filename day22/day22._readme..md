Problem Statement: To check if a list contains duplicate values. Returns `True` if all the nums are unique, else `False`.

For example:

```
Input: nums = [1,2,3,1]
Output: true
```

Language Used: Python

Algorithm used:

We create an empty set at start. Then, we traverse through the list using `i` variable as iterator. We check if the `i` is present in the set or not. If it is, code return `True`. Then, the code proceeds to add that number in the set. Since, a `set()` cannot have duplicate values, it is not stored, if the number is already in set( either way the code will return `True` before hand.). After the whole list is traversed through, if the code did not return `True` anywhere, it auto returns `False`.

Code Performance:

Runtime: 403ms
Memory: 32.02MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
