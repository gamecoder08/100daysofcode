// Leetcode Solution:

// class Solution {
// public:

//      int searchPos(vector<int>& inorder, int start, int end, int curr) {
//         for (int i = start; i <= end; i++) {
//             if (inorder[i] == curr) {
//                 return i;
//             }
//         }
//         return -1;
//     }

//     TreeNode* buildtree(vector<int>& inorder, vector<int>& preorder, int start, int end, int& idx) {
//         if (start > end || idx < 0) {
//             return NULL;
//         }

//         int curr = preorder[idx];
//         idx++;

//         TreeNode* node = new TreeNode(curr);

//         if (start == end) {
//             return node;
//         }

//         int pos = searchPos(inorder, start, end, curr);

//         node->left = buildtree(inorder, preorder, start, pos - 1, idx);
//         node->right = buildtree(inorder, preorder, pos + 1, end, idx);

//         return node;
//     }

//     TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
//         if (preorder.empty() || inorder.empty() || inorder.size() != preorder.size()) {
//             return nullptr;
//         }

//         int idx = 0;
//         return buildtree(inorder, preorder, 0, inorder.size() - 1, idx);
//     }
// };