Problem Statement: To implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

```
Example:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)

```

Technique Used: String, ASCII notation

Approach:

We start by traversing over whitespaces as they are not needed in the number. Then, we check for `-` or `+` to determine if the number will be postive and negative, and thus intialize a `sign` variable as `1` or `-1`. The, we loop over numbers. We determine the number in the string using `s[i]-'0'` technique, which effectively returns the integer version of that number. Then, we check for overflow using `INT_MAX`. If the number is overflowed with postive sign, `INT_MAX` is returned, else if the number is overflowed with negative sign, `INT_MIN` is returned. If nothing is returned, then `ans` with mutiplication of `sign` is returned. This returns the accurate required integer number.

Performance:

Time Complexity: 0ms
Space Complexity: 9.02MB

Note: These performances are tracked on online compiler and can vary.
