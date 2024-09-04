// Leetcode Solution

// class Solution {
// public:
//     bool backspaceCompare(string s, string t) {
//         stack<char> s1;
//         stack<char> t1;
//         for(char i : s)
//         {
//             if(i=='#')
//             {
//                 if(s1.empty())
//                 {
//                     continue;
//                 }
//                 else{
//                     s1.pop();
//                 }
//             }
//             else
//             {
//                 s1.push(i);
//             }
//         }
//         for(char j : t)
//         {
//             if(j=='#')
//             {
//                 if(t1.empty())
//                 {
//                     continue;
//                 }
//                 else{
//                     t1.pop();
//                 }
//             }
//             else
//             {
//                 t1.push(j);
//             }
//         }
//         return s1==t1;
//     }
// };