// Leetcode Solution:

// class Solution {
// public:
//     bool isPalindrome(ListNode* head) {
//         stack <int> s;
//         ListNode* temp = head;
//         while(temp) {
//             s.push(temp->val);
//             temp = temp->next;
//         }

//         temp = head;
//         while(temp)
//         {
//             if(temp->val!=s.top())
//             {
//                 return false;
//             }
//             s.pop();
//             temp = temp->next;
//         }
//         return true;
//     }
// };