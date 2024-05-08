#Leetcode Solution

# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         sorted_list=score.copy()
#         sorted_list.sort(reverse=True)
#         result=['0'] * len(score)
#         for i in range(len(score)):
#             if score[i]==sorted_list[0]:
#                 result[i]="Gold Medal"
#             elif score[i]==sorted_list[1]:
#                 result[i]="Silver Medal"
#             elif score[i]==sorted_list[2]:
#                 result[i]="Bronze Medal"
#             else:
#                 result[i]=str(1+sorted_list.index(score[i]))
#         return result


#An altered solution for dry run.

def findRelativeRanks(score):
    sorted_list=score.copy()
    sorted_list.sort(reverse=True)
    result=['0'] * len(score)
    for i in range(len(score)):
        if score[i]==sorted_list[0]:
            result[i]="Gold Medal"
        elif score[i]==sorted_list[1]:
            result[i]="Silver Medal"
        elif score[i]==sorted_list[2]:
            result[i]="Bronze Medal"
        else:
            result[i]=str(1+sorted_list.index(score[i]))
    return result
    
n=int(input("Enter length of list: "))
score=[]
for i in range(n):
    score.append(int(input("Enter score: ")))    
result=findRelativeRanks(score)
print(result)