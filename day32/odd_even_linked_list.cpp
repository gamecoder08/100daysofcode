// Leetcode Solution:

// class Solution {
// public:
//     ListNode* oddEvenList(ListNode* head) {
//         if(head == NULL)
//             return NULL;
//         ListNode* odd  = head;
//         ListNode* even = head -> next;
//         ListNode* evenhead = head -> next;

//         while(even != NULL and even -> next != NULL)
//         {
//             odd ->next = odd -> next -> next;
//             odd = odd -> next;

//             even -> next = even -> next -> next;
//             even = even -> next;
//         }

//         odd -> next = evenhead;
//         return head;
//     }
// };