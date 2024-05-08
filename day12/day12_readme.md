Problem Statement: To return the medals according to score in a list.

For example:

```
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
```

Language Used: Python

Algorithm used:

First, a copy of original list was created and then sorted. From the sorted list, we now get the top 3 participants and also other participants positions. A `For` loop is run through the `score` list. There we determine the original position of the participant in list and place it accordingly in the final result list. Then, the final list is returned.

Code Performance:

Runtime: 248ms
Memory: 17.6MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
