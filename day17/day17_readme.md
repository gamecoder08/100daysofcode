Problem Statement: To assign cookies to a child if the craving is lesser than size of cookie. More clear in example.

For example:

```
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

Language Used: Python

Algorithm used:

First we sort both the listss using `sort()` function. After that two variables `result` and `j` are created in order to track fulfilled children and to track children array respectively. A loop is run through s list for cookies and a size comparison is done between craving of chill in `g` list and size of cookie in `s` list. Once condistion is satisfied, both the created variables are incremented by 1. Once, `j` reaches size of `g` array. The loop breakes and `result` is returned.

Code Performance:

Runtime: 138ms
Memory: 18.38MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
