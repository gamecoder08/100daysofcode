Problem Statement: To return `True` or `False` depending upon the no of occurance of element in the list.

For example:

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

Language Used: Python

Algorithm used:

An empty dictionary is created. The `count()` function in python returns the no of times an element is appeared in the list with `for` loop. This info is then stored in the dictionary. Later, a list is created from the values of dictionary. It is then compared using `len()` function to the `len()` of `set()` function. The code returns `True` if the values are unique and it returns `False` if the values are not unique.

Code Performance:

Runtime: 65ms
Memory: 16.77MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
