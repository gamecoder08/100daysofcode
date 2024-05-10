#Leetcode Solution

# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         nums.sort()
#         return (nums[-1]*nums[-2])-(nums[0]*nums[1])


def maxProductDifference(nums):
    nums.sort()
    return (nums[-1]*nums[-2])-(nums[0]*nums[1])
    
n=int(input("Enter length of list: "))
nums=[]
for i in range(n):
    nums.append(int(input("Enter score: ")))    
result=maxProductDifference(nums)
print(result)