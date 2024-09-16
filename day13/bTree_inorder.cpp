// Leetcode Solution:

// class Solution {
//     vector<int> vec;
// public:

//     void inorder(TreeNode* root)
//     {
//         if(root==NULL)
//         {
//             return;
//         }
//         inorder(root->left);
//         vec.push_back(root->val);
//         inorder(root->right);
//     }

//     vector<int> inorderTraversal(TreeNode* root) {
//         inorder(root);
//         return vec;
//     }
// };