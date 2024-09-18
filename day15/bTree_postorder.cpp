// Leetcode Solution:

// class Solution {
//     vector<int> vec;
// public:

//     void postorder(TreeNode* root)
//     {
//         if(root==NULL)
//         {
//             return;
//         }
//         postorder(root->left);
//         postorder(root->right);
//         vec.push_back(root->val);
//     }

//     vector<int> postorderTraversal(TreeNode* root) {
//         postorder(root);
//         return vec;
//     }
// };