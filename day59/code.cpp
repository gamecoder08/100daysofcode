// Leetcode Solution

// class Solution {
// public:
//     bool isPowerOfThree(int n) {
//         if (n==1){
//             return true;
//         }
//         else if(n%3!=0){
//             return false;
//         }
//         if (n<4){
//             if (n==3){
//                 return true;
//             }
//             else{
//                 return false;
//             }
//         }
//         int m = n/3;
//         return isPowerOfThree(m);
//     }
// };