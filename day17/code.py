#Leetcode Solution

# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()
#         result=0
#         j=0
#         for i in range(len(s)):
#             if s[i]>=g[j]:
#                 result+=1
#                 j+=1

#             if j==len(g):
#                 break
#         return result

#An altered solution for dry run.

def findContentChildren(g, s):
    g.sort()
    s.sort()
    result=0
    j=0
    for i in range(len(s)):
        if s[i]>=g[j]:
            result+=1
            j+=1

        if j==len(g):
            break
    return result
    
n1=int(input("Enter no. of children: "))
g=[]
for i in range(n1):
    g.append(int(input("Enter craving: ")))   
     
n2=int(input("Enter no. of cookies: "))
s=[]
for i in range(n2):
    s.append(int(input("Enter cookie size: ")))    

result=findContentChildren(g,s)
print(result)