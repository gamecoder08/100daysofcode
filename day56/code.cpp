// Leetcode Solution

// class Solution {
// public:
//     int sum(int n)
//     {
//         int summ=0, ans;
//         while(n)
//         {
//             summ+=n%10;
//             n/=10;
//         }
//         if(summ>9)
//             ans=sum(summ);
        
//         else
//             ans=summ;
        
//         return ans;
//     }
//     int addDigits(int num) {
//         return sum(num);
//     }
// };