#Leetcode Solution

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         str_set=set()
#         length=0
#         for i in s:
#             if i in str_set:
#                 str_set.remove(i)
#                 length +=2
#             else:
#                 str_set.add(i)

#         if str_set:
#             length+=1

#         return length


#An altered solution for dry run.


def longestPalindrome(s):
    str_set=set()
    length=0
    for i in s:
        if i in str_set:
            str_set.remove(i)
            length +=2
        else:
            str_set.add(i)

    if str_set:
        length+=1

    return length


n=input("Enter string: ")
result = longestPalindrome(n)
print(result)