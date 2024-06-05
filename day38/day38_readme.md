Problem Statement: To find the common characters from a list of words.

For example:

```
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
```

Language Used: Python

Algorithm used:

We start with importing `Counter()` sub-class from `collections` module. Then, we a create an object which counts the number of elements from the first element of list. Then, we start the iteration over the list. At each word, we do an intersection using `&=` operator to ensure minimum number of elements enter the object. The, we return the list of all the elements from the object.

Code Performance:

Runtime: 47ms
Memory: 16.70MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
