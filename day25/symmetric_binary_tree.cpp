// Leetcode Solution:

// class Solution {
// public:
//     bool isEqual(TreeNode* n1, TreeNode* n2)
//     {
//         if(!n1 || !n2)
//         {
//             return n1==n2;
//         }
//         if(n1->val == n2 ->val)
//         {
//             return isEqual(n1->left,n2->right) && isEqual(n1->right,n2->left);
//         }
//         return false;
//     }

//     bool isSymmetric(TreeNode* root) {
//         return isEqual(root->left,root->right);
//     }
// };