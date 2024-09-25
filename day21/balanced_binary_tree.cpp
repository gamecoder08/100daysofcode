// Leetcode Solution:

// class Solution {
//     int checkHeight(TreeNode* node)
//     {
//         if(node==NULL)
//         {
//             return 0;
//         }
//         int leftHeight = checkHeight(node->left);
//         if(leftHeight == -1)
//         {
//             return -1;
//         }
//         int rightHeight = checkHeight(node->right);
//         if(rightHeight == -1)
//         {
//             return -1;
//         }
//         if(abs(leftHeight-rightHeight) > 1)
//         {
//             return -1;
//         }
//         return 1 + max(leftHeight,rightHeight);
//     }
// public:
//     bool isBalanced(TreeNode* root) {
//         if(checkHeight(root) != -1)
//         {
//             return true;
//         }
//         else
//         {
//             return false;
//         }
//     }
// };