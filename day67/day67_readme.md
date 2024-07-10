Problem Statement: To lower case characters of a string without using built - in functions.

Explaination:

-

For example:

```
Input: s = "Hello"
Output: "hello"
```

Language Used: C++

Algorithm used:

Since, built-in functions are not allowed, we can use `ASCII` values here. The difference between the upper case character and it's lower counterpart is constant which is `32`. So, we run a loop through the word. We check if the `ASCII` value of each character lies in the range of Upper cased characters, which is `65 - 90`. So, if falls under this category, the ASCII value if added with `32`, hence converting the character.

Code Performance:

Runtime: 0ms
Memory: 7.31MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
