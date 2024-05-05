#Leetcode Solution

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         arr_dict={}
#         values=[]
#         for i in arr:
#             appearance=arr.count(i)
#             arr_dict.update({i:appearance})
#         values = list(arr_dict.values())
#         return len(values) == len(set(values))


#An altered solution for dry run.

def uniqueOccurrences(arr):
    arr_dict={}
    values=[]
    for i in arr:
        appearance=arr.count(i)
        arr_dict.update({i:appearance})
    values = list(arr_dict.values())
    return len(values) == len(set(values))


arr=[]
n=int(input("Enter length of list: "))
for i in range(n):
    arr.append(int(input(f"The element for list in position {i}")))

result=uniqueOccurrences(arr)
print(result)