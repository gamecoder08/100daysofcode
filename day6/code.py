#Leetcode Solution

# class Solution:
#     def findMaxK(self, nums: List[int]) -> int:
#         largest=-1
#         nums_set=set(nums)
#         for i in nums_set:
#             if i>0:
#                 if -i in nums and i>largest:
#                     largest=i
#         return largest


#An altered solution for dry run.

def findMaxK(nums):
    largest=-1
    nums_set=set(nums)
    for i in nums_set:
        if i>0:
            if -i in nums and i>largest:
                largest=i
    return largest

nums=[]
n=int(input("Enter list size: "))
for i in range(n):
    nums.append(input(f"Enter value {i}: "))
result=findMaxK(nums)
print(result)