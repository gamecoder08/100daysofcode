#Leetcode Solution

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
        
#         if n < 0:
#             x**=-1
#             n*=-1
        
#         if n % 2 == 1:
#             return x * self.myPow (x,n-1)
#         else:
#             num = self.myPow(x,n//2)
#             return num * num