#Leetcode Solution

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word:
#             return word
#         firstocc_index=0
#         for i in range(len(word)):
#             if word[i]==ch:
#                 firstocc_index=i
#                 break
#         a_string=word[:firstocc_index+1]
#         rest_string=word[firstocc_index+1:]
#         return a_string[::-1]+rest_string


#An altered solution for dry run.

def reversePrefix(word, ch):
    if ch not in word:
        return word
    firstocc_index=0
    for i in range(len(word)):
        if word[i]==ch:
            firstocc_index=i
            break
    a_string=word[:firstocc_index+1]
    rest_string=word[firstocc_index+1:]
    return a_string[::-1]+rest_string

word=input("Enter the word: ")
ch=input("Enter the string: ")
result=reversePrefix(word,ch)
print(result)