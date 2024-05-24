Problem Statement: To find if a Linked list is Palindrome or not.

For example:

```
Input: head = [1,2,2,1]
Output: true
```

Language Used: Python

Algorithm used:

So, approach her would be copying the data from the Linked List to a normal list, and then simply use two pointer approach to find if list is palindrome or not. So, using `while` loop to traverse through Linked list and we append the data into an empty list. We then declare two pointer with indices of the start and end of list respectively. Then, we simultaneously traverse through the list finding till when the list has same values. If the value of `left` is greater than `right` indicating successfull completion of loop, it will return `True` meaning the list is palindrome, else it will return `False`.

Code Performance:

Runtime: 266ms
Memory: 36.88MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
