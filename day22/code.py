#Leetcode Solution

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         numbers=set()
#         for i in nums:
#             if i in numbers:
#                 return True
#             numbers.add(i)
#         return False

#An altered solution for dry run.

def containsDuplicate(nums):
    numbers=set()
    for i in nums:
        if i in numbers:
            return True
        numbers.add(i)
    return False
    
n=input("Enter length of list: ")
nums=[]
for i in range(n):
    nums.append(int(input(f"Enter element {i}: ")))
result=containsDuplicate(nums)
print(result)