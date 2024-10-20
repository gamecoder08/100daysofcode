// Leetcode Solution:

// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         unordered_set<int> hashset;
//         for(int i : nums)
//         {
//             if(hashset.count(i)>0)
//                 return true;
//             hashset.insert(i);
//         }
//         return false;
//     }
// };