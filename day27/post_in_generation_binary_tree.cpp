// Leetcode Solution:

// class Solution {
// public:

//     int searchPos(vector<int>& inorder, int start, int end, int curr) {
//         for (int i = start; i <= end; i++) {
//             if (inorder[i] == curr) {
//                 return i;
//             }
//         }
//         return -1;
//     }

//     TreeNode* buildtree(vector<int>& inorder, vector<int>& postorder, int start, int end, int& idx) {
//         if (start > end || idx < 0) {
//             return NULL;
//         }

//         int curr = postorder[idx];
//         idx--;

//         TreeNode* node = new TreeNode(curr);

//         if (start == end) {
//             return node;
//         }

//         int pos = searchPos(inorder, start, end, curr);

//         node->right = buildtree(inorder, postorder, pos + 1, end, idx);
//         node->left = buildtree(inorder, postorder, start, pos - 1, idx);

//         return node;
//     }

//     TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
//         if (postorder.empty() || inorder.empty() || inorder.size() != postorder.size()) {
//             return nullptr;
//         }

//         int idx = postorder.size() - 1;
//         return buildtree(inorder, postorder, 0, inorder.size() - 1, idx);
//     }
// };