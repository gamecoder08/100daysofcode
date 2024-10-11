// Leetcode Solution:

// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//         if(list1 == NULL)
//         {
//             return list2;
//         }
//         if(list2 == NULL)
//         {
//             return list1;
//         }

//         ListNode* dummy = new ListNode();
//         ListNode* head = dummy;

//         ListNode* temp1 = list1;
//         ListNode* temp2 = list2;

//         while(temp1 && temp2)
//         {
//             if(temp1->val <= temp2->val)
//             {
//                 head->next = temp1;
//                 temp1 = temp1->next;
//             }
//             else if(temp1->val > temp2->val)
//             {
//                 head->next = temp2;
//                 temp2 = temp2->next;
//             }
//             head = head->next;
//         }

//         if(temp1)
//         {
//             head->next = temp1;
//         }

//         if(temp2)
//         {
//             head->next = temp2;
//         }

//         head = dummy->next;
//         delete dummy;
//         return head;
//     }
// };