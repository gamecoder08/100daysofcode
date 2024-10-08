// Leetcode Solution:

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         ListNode* prev = NULL;
//         ListNode* curr = head;
//         ListNode* nextt;
//         while(curr)
//         {
//             nextt=curr->next;
//             curr->next=prev;
//             prev=curr;
//             curr=nextt;
//         }
//         head = prev;
//         delete curr, prev, nextt;
//         return head;
//     }
// };