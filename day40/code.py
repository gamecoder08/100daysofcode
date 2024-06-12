#Leetcode Solution

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         nums.sort()


#An altered solution for dry run.

def sortColors(nums):
    nums.sort()
    
n=int(input("Enter length of list: "))
nums=[]
for i in range(0,n):
    nums.append(int(input("Enter value: ")))

result=sortColors(nums)
print(result)