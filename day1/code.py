# Leetcode Solution

# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         string1 = ""
#         string2 = ""
#         for i in word1:
#             string1 = string1 + i
#         for j in word2:
#             string2 = string2 + j
#         if string1 == string2:
#             return True
#         else:
#             return False


#Code adjusted for normal running


def arrayStringsAreEqual(word1, word2):
    string1 = ""
    string2 = ""
    for i in word1:
        string1 = string1 + i
    for j in word2:
        string2 = string2 + j
    if string1 == string2:
        return True
    else:
        return False

word1=[]
word2=[]
n1=int(input("Enter no of elements for first array: "))
n2=int(input("Enter no of elements for first array: "))
for i in range(n1):
    word1.append(i)
for j in range(n2):
    word2.append(j)
     
arrayStringsAreEqual(word1,word2)