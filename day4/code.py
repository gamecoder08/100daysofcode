#Leetcode Solution

# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         a=s[:int(len(s)/2)]
#         b=s[int(len(s)/2):]
#         a_vowel=0
#         b_vowel=0
#         for i in a:
#             if i=='a' or i=='A':
#                 a_vowel=a_vowel+1
#             elif i=='e' or i=='E':
#                 a_vowel=a_vowel+1
#             elif i=='i' or i=='I':
#                 a_vowel=a_vowel+1
#             elif i=='o' or i=='O':
#                 a_vowel=a_vowel+1
#             elif i=='u' or i=='U':
#                 a_vowel=a_vowel+1
        
#         for j in b:
#             if j=='a' or j=='A':
#                 b_vowel=b_vowel+1
#             elif j=='e' or j=='E':
#                 b_vowel=b_vowel+1
#             elif j=='i' or j=='I':
#                 b_vowel=b_vowel+1
#             elif j=='o' or j=='O':
#                 b_vowel=b_vowel+1
#             elif j=='u' or j=='U':
#                 b_vowel=b_vowel+1
#         if a_vowel==b_vowel:
#             return True
#         else:
#             return False


#An altered solution for dry run.

def halvesAreAlike(s):
    a=s[:int(len(s)/2)]
    b=s[int(len(s)/2):]
    a_vowel=0
    b_vowel=0
    for i in a:
        if i=='a' or i=='A':
            a_vowel=a_vowel+1
        elif i=='e' or i=='E':
            a_vowel=a_vowel+1
        elif i=='i' or i=='I':
            a_vowel=a_vowel+1
        elif i=='o' or i=='O':
            a_vowel=a_vowel+1
        elif i=='u' or i=='U':
            a_vowel=a_vowel+1
    
    for j in b:
        if j=='a' or j=='A':
            b_vowel=b_vowel+1
        elif j=='e' or j=='E':
            b_vowel=b_vowel+1
        elif j=='i' or j=='I':
            b_vowel=b_vowel+1
        elif j=='o' or j=='O':
            b_vowel=b_vowel+1
        elif j=='u' or j=='U':
            b_vowel=b_vowel+1
    if a_vowel==b_vowel:
        return True
    else:
        return False

s=input('Enter a string with equal length: ')
result=halvesAreAlike(s)
print(result)