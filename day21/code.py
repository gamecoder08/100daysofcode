#Leetcode Solution

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         set_zip = set(zip(s, t))
#         set_s = set(s)
#         set_t = set(t)
#         result = len(set_zip) == len(set_s) == len(set_t)
#         return result

#An altered solution for dry run.

def isIsomorphic(s,t):
    set_zip = set(zip(s, t))
    set_s = set(s)
    set_t = set(t)
    result = len(set_zip) == len(set_s) == len(set_t)
    return result
    
s=input("Enter string 1: ")
t=input("Enter string 2: ")
result=isIsomorphic(s,t)
print(result)