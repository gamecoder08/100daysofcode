Problem Statement: To sort a sentence of using the number given in the last index of string.

For example:

```
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
```

Language Used: Python

Algorithm used:

At first, we use `split()` function to convert the string into a list. Then, the list is sorted by comparing the last index of string using `[][-1]` method. I have used bubble sort here since the constraint is small and is also easy to implement. Then, another loop runs over the list in order to remove the digit using an inline loop. Then the return value is the list passed through the `' '.join()` function.

Code Performance:

Runtime: 26ms
Memory: 16.71MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
