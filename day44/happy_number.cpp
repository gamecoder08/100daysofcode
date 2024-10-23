// Leetcode Solution:

// class Solution {
// public:
//     int sqdigitsum(int num)
//     {
//         int sum = 0, temp;
//         while(num)
//         {
//             temp = num % 10;
//             sum = sum + temp * temp;
//             num = num / 10;
//         }
//         return sum;
//     }
//     bool isHappy(int n) {
//         int slow, fast;
//         slow = fast = n;
//         do
//         {
//             slow = sqdigitsum(slow);
//             fast = sqdigitsum(fast);
//             fast = sqdigitsum(fast);
//             if(fast==1)
//             {
//                 return 1;
//             }
//         }while(slow != fast);
//         return 0;
//     }
// };