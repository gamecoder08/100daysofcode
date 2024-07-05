Problem Statement: To check if a number is a bad version or not.

For example:

Each number represent a version number till `n`. Around somewhere in between a version turned out bad, resulting in all consequent versions to turn out bad. To find out the first bad version among the versions using a given pre declared function `isBadVersion()`.

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

Language Used: C++

Algorithm used:

We use two pointer approach for this question. We start with a pointer at the bottom of versions and one at a top. We start a `while` loop until the lower pointer `low` is lesser than higher one `high`. We find the middle of the list, we check if the middle version and the version just below return `true` and `false` respectively, meaning the middle version is first bad one. If it does return true for the `and` if, then `mid` is returned. Else if, checking middle version returns `true`, we lower upper pointer `high` value to `mid - 1` reducing the range since all the upper ones are bad, else we increase the value of lower pointer `low` to `mid + 1`, meaning all lower ones are good. When the loop ends, and nothing is returned, we return the lower pointer `low`, meaning there was a single version, which bad itself.

Code Performance:

Runtime: 0ms
Memory: 7.19MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
