// Leetcode Solution:

// class Solution {
// public:
//     int maxSubArray(vector<int>& nums) {
//         int res = nums[0];
//         int total = 0;

//         for(int i : nums)
//         {
//             if(total<0)
//             {
//                 total = 0;
//             }

//             total+=i;
//             res = max(res,total);
//         }
//         return res;
//     }
// };