// Leetcode Solution

// class Solution {
// public:
//     string clearDigits(string s) {
//         int n = size(s);
//         list<char> li;
//         string ans="";
//         for(int i=0;i<n;i++)
//         {
//             if(isdigit(s[i]))
//             {
//                 li.pop_back();
//                 continue;
//             }
//             else
//             {
//                 li.push_back(s[i]);
//             }
//         }
//         while(!li.empty())
//         {
//             ans=ans+(li.front());
//             li.pop_front();
//         }
//         return ans;
//     }
// };