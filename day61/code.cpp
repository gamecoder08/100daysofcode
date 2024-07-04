// Leetcode Solution

// class Solution {
// public:
//     bool isPowerOfFour(int n) {
//         if (n==1){
//             return true;
//         }
//         if (n%4!=0){
//             return false;
//         }
//         if (n<8){
//             if (n==4){
//                 return true;
//             }
//             else{
//                 return false;
//             }
//         }
//         int m = n/4;
//         return isPowerOfFour(m);
//     }
// };