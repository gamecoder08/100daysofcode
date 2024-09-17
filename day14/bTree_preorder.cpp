// Leetcode Solution:

// class Solution {
//     vector<int> vec;
// public:

//     void preorder(TreeNode* root)
//     {
//         if(root==NULL)
//         {
//             return;
//         }
//         vec.push_back(root->val);
//         preorder(root->left);
//         preorder(root->right);
//     }

//     vector<int> preorderTraversal(TreeNode* root) {
//         preorder(root);
//         return vec;
//     }
// };