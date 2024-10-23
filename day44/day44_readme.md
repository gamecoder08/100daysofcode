Problem Statement: To write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

```
Example:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

```

Technique Used: Fast and slow pointer

Approach:

We start by creating a helper function which will calculate the sum of digits of the input number and return the sum. Essentially, it just uses `%` operator and `/` operator to fetch the unit's place number and remove it respectively, and also using it to calculate sum. In the main function here, we initialise two pointers `slow` and `fast` both equal to number `n`. We call the helper function once for `slow`, and twice for `fast`, thus speeding up the `fast` pointer, inside a `do() - while()` loop. Logic is, if the number is a happy number, both fast or slow pointer will reach `1` eventually. And if it's not, they will meet each other inside the cyclic loop after some time. So, we check if `fast` equals `1` anytime, considering it will reach `1` first. If it does, we immediately return `1`, thus `true`. If it does not, we wait for the loop to exit. And then we return `0`, hence `false`.

Performance:

Time Complexity: 0ms
Space Complexity: 7.37MB

Note: These performances are tracked on online compiler and can vary.
