// Leetcode Solution

// class Solution {
// public:
//     bool isPowerOfTwo(int n) {
//         if (n==1){
//             return true;
//         }
//         else if(n%2!=0){
//             return false;
//         }
//         if (n<4){
//             if (n==2){
//                 return true;
//             }
//             else{
//                 return false;
//             }
//         }
//         int m = n/2;
//         return isPowerOfTwo(m);
//     }
// };