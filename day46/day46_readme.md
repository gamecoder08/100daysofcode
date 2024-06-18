Problem Statement: To find the Largest number formed by concating a string of numbers from an array.

For example:

```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

Language Used: C++

Algorithm used:

At start, we create a custom function `compare_nums` which will compare two separate strings ints and will return the largest among the two strings formed by concating them side-by-side. Then, in main, we take the length of `nums` array and use `sort()` function to sort the array using the custom `compare_nums` function. We then, create an empty string and concate all the strings from the sorted array. For the end-line case, we consider if the first index is `0` in the sorted array, it will mean the whole array is full of zeroes, thus return `0`. Else, the final concated string will be returned.

Code Performance:

Runtime: 5ms
Memory: 15.24MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
