#Leetcode Solution

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         largest_str="000"
#         for i in num:
#             test_str=''
#             test_str=i+i+i
#             if test_str in num:
#                 if int(test_str)>int(largest_str):
#                     largest_str=test_str
#         if largest_str not in num:
#             largest_str=''
#         return largest_str


#Improvised code for normal run


def largestGoodInteger(num):
    largest_str="000"
    for i in num:
        test_str=''
        test_str=i+i+i
        if test_str in num:
            if int(test_str)>int(largest_str):
                largest_str=test_str
    if largest_str not in num:
        largest_str=''
    return largest_str

num=input("Enter a number: ")
result=largestGoodInteger(num)
print(result)