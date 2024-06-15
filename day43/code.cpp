// Leetcode Solution

// class Solution {
// public:
//     int searchInsert(vector<int>& nums, int target) {
//         int n = size(nums);
//         if (target>nums[n-1]){
//             return n;
//         }
//         for (int i=0;i<n;i++){
//             if (nums[i]==target){
//                 return i;
//             }
//             else if (nums[i]>target){
//                 return i;
//             }
//         }
//         return 0;
//     }
// };