Problem Statement: To find if a list of numbers can be divided into a series of lists of given length.

For example:

```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
```

Language Used: Python

Algorithm used:

We start with importing `Counter()` sub-class from `collections` module. At first, we check if the lists are possible to form or not. Then, we a create an object which counts the number of occurrences of each element from the list. Then, we sort the list keys using `sorted()` function. We start iteration over the sorted list. We compare if the card is available in card list from the occurences counting object. If it is not available, we proceed the loop, else we store the key. We then iterate over to see if each element next to it till the length of `groupSize` is consecutive or not. If it's not the code directly return `False` else, it stores it as a list. And a count is decremented from the object for the each item in the formed list. After all the iterations, we return `True` if the loop is not broken.

Code Performance:

Runtime: 47ms
Memory: 16.70MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
