#Leetcode Solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         mid_ptr = head
#         end_ptr = head

#         while end_ptr is not None and end_ptr.next is not None:
#             mid_ptr = mid_ptr.next
#             end_ptr = end_ptr.next.next

#         return mid_ptr  
