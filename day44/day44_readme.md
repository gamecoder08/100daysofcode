Problem Statement: To find if a string has paranthesis in a proper closing and opening order or not.

For example:

```
Input: s = "()[]{}"
Output: true
```

Language Used: C++

Algorithm used:

We start with initialising an empty stack. We then start a `for` loop operation through each and every string. We check if the terative character is any of the opening brackets. If it is, then it is pushed into stack. Else, we check if stack is empty `or` has any of the closing brackets in it with it's opening counterpart `not` on top. If either condition is true, it returns `False`. After these, we pop the stack, and carry on with loop. If any of the return cases are not achieved, we return the empty stack.

Code Performance:

Runtime: 0ms
Memory: 7.65MB

NOTE: These performance results are for one time run and may give different stats for different inputs and runs.
