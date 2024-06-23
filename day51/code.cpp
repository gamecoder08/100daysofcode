// Leetcode Solution

// class Solution {
// public:
//     int scoreOfString(string s) {
//         int score = 0;
//         int n = size(s);
//         for (int i=1; i<n;i++){
//             int diff = int(s[i-1]) - int(s[i]);
//             if (diff<0){
//                 score += (diff*(-1));
//             }
//             else{
//                 score += diff;
//             }
//         }
//         return score;
//     }
// };