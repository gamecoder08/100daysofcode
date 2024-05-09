#Leetcode Solution

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         return (nums[-1]-1) * (nums[-2]-1)

def maxProduct(nums):
    nums.sort()
    return (nums[-1]-1) * (nums[-2]-1)
    
n=int(input("Enter length of list: "))
nums=[]
for i in range(n):
    nums.append(int(input("Enter score: ")))    
result=maxProduct(nums)
print(result)