// Leetcode Solution:

// class Solution {
// public:
//     Node* flatten(Node* head) {
//         if(head == NULL)
//         {
//             return NULL;
//         }
//         Node *ptr = head;
//         stack<Node*> st;
//         while(ptr)
//         {
//             if(ptr->child)
//             {
//                 if(ptr->next){
//                     st.push(ptr->next);
//                 }

//                 ptr->child->prev = ptr;
//                 ptr->next = ptr->child;
//                 ptr->child = NULL;
//             }

//             if(!ptr->next && !st.empty())
//             {
//                 ptr->next = st.top();
//                 st.pop();
//                 ptr->next->prev = ptr;
//             }
//             ptr = ptr->next;
//         }
//         return head;
//     }
// };