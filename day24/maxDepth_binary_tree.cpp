// Leetcode Solution:

// class Solution {
// public:
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         vector<vector<int>> traversal;
//         if(root==NULL)
//         {
//             return traversal;
//         }

//         queue<TreeNode*> queue;
//         queue.push(root);

//         while(!queue.empty())
//         {
//             vector<int> currLevel;
//             int currSize = queue.size();

//             for(int i = 0; i < currSize; ++i)
//             {
//                 TreeNode* currNode = queue.front();
//                 queue.pop();

//                 currLevel.push_back(currNode->val);

//                 if(currNode->left!=NULL)
//                 {
//                     queue.push(currNode->left);
//                 }
//                 if(currNode->right!=NULL)
//                 {
//                     queue.push(currNode->right);
//                 }
//             }

//             traversal.push_back(currLevel);
//         }
//         return traversal;
//     }
// };