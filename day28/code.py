#Leetcode Solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         values=[]
#         while head:
#             values.append(head.val)
#             head = head.next
        
#         left, right = 0, len(values) - 1
#         while left < right and values[left]==values[right]:
#             left+=1
#             right-=1
#         return left>=right
