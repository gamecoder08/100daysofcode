#Leetcode Solution

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1=nums1+nums2
#         nums1.sort()
#         n=len(nums1)
#         if n%2==0:
#             return (nums1[int((n-1)/2)]+nums1[int(n/2)])/2
#         else:
#             return float(nums1[int(n/2)])  

#An altered solution for dry run.

def findMedianSortedArrays(nums1,nums2):
    nums1=nums1+nums2
    nums1.sort()
    n=len(nums1)
    if n%2==0:
        return (nums1[int((n-1)/2)]+nums1[int(n/2)])/2
    else:
        return float(nums1[int(n/2)])  
    
n1=input("Enter length of list 1: ")
nums1=[]
for i in range(n1):
    nums1.append(int(input(f"Enter element {i}: ")))

n2=input("Enter length of list 2: ")
nums2=[]
for j in range(n2):
    nums2.append(int(input(f"Enter element {j}: ")))
    
result=findMedianSortedArrays(nums1,nums2)
print(result)