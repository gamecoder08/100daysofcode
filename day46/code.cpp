// Leetcode Solution

// class Solution {
// public:
//     bool static compare_nums(int a, int b){
//         string ptr=to_string(a), qtr = to_string(b);
//         return ptr+qtr>qtr+ptr;
//     }
//     string largestNumber(vector<int>& nums) {
//         int n = size(nums);
//         sort(nums.begin(), nums.end(), compare_nums);

//         string ans;
//         for (int i=0;i<n;i++){
//             ans+=to_string(nums[i]);
//         }
//         if(ans[0]=='0'){
//             return "0";
//         }
//         return ans;
//     }
// };