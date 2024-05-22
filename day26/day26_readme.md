Problem Statement: To reverse a Linked List.

For example:

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Language Used: Python

Algorithm used:

We start with creating two variables, one for tracking new List and one for traversing the list. A `while` loop is run to traverse the list. We then save the next node's data in a variable otherwise we would lose the track of original list. Then, the interchange is done from `.next` to prev node. Then, we move forward a node in original list and then the saved node data is passed on current node to traverse further. After the `while()` loop is run through, we return `prev_node` variable as it serves as a new head for the reversed list.

Code Performance:

Runtime: 36ms
Memory: 17.62MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
