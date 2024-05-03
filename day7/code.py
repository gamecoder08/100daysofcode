#Leetcode Solution

# class Solution:
#     def sortSentence(self, s: str) -> str:
#         str_list=s.split()
#         swapped=0
#         while swapped==0:
#             num_swaps=0
#             for i in range(1,len(str_list)):
#                 if int(str_list[i-1][-1])>int(str_list[i][-1]):
#                     temp=str_list[i-1]
#                     str_list[i-1]=str_list[i]
#                     str_list[i]=temp
#                     num_swaps=num_swaps+1
#             if num_swaps==0:
#                 swapped=1
#         for i in range(len(str_list)):
#             str_list[i]= ''.join((x for x in str_list[i] if not x.isdigit()))
#         return ' '.join(str_list)


#An altered solution for dry run.

def sortSentence(s):
    str_list=s.split()
    swapped=0
    while swapped==0:
        num_swaps=0
        for i in range(1,len(str_list)):
            if int(str_list[i-1][-1])>int(str_list[i][-1]):
                temp=str_list[i-1]
                str_list[i-1]=str_list[i]
                str_list[i]=temp
                num_swaps=num_swaps+1
        if num_swaps==0:
            swapped=1
    for i in range(len(str_list)):
        str_list[i]= ''.join((x for x in str_list[i] if not x.isdigit()))
    return ' '.join(str_list)

s=input("Enter a sentence with desired position at the end of each word: ")
result=sortSentence(s)
print(result)