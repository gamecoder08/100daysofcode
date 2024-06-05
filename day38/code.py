#Leetcode Solution

# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         min_freq = Counter(words[0])
#         for word in words:
#             min_freq &= Counter(word)
#         return list(min_freq.elements())


#An altered solution for dry run.

from collections import Counter

def commonChars(words):
    min_freq = Counter(words[0])
    for word in words:
        min_freq &= Counter(word)
    return list(min_freq.elements())

n=int(input("Enter length of list: "))
l=[]
for i in range(n):
    l.append(input("Enter word: ")) 
result = commonChars(l)
print(result)