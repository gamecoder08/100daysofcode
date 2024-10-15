// Leetcode Solution:

// class Solution {
// public:
//     Node* copyRandomList(Node* head) {
//         if(!head)
//         {
//             return NULL;
//         }

//         Node *temp = head;

//         while(temp)
//         {
//             Node *newNode = new Node(temp->val);
//             newNode->next = temp->next;
//             temp->next = newNode;
//             temp = newNode->next;
//         }

//         temp = head;
//         while (temp) {
//             if (temp->random) {
//                 temp->next->random = temp->random->next;
//             }
//             temp = temp->next->next;
//         }

//         Node *newHead = head->next;
//         temp = head;
//         Node* copyTemp = newHead;

//         while (temp) {
//             temp->next = temp->next->next;
//             if (copyTemp->next) {
//                 copyTemp->next = copyTemp->next->next;
//             }
//             temp = temp->next;
//             copyTemp = copyTemp->next;
//         }
//         return newHead;
//     }
// };