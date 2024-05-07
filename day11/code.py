#Leetcode Solution

# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         new_matrix=[]
#         for i in range(len(matrix[0])):
#             temp=[]

#             for j in range(len(matrix)):
#                 temp.append(matrix[j][i])
            
#             new_matrix.append(temp)
#         return new_matrix


#An altered solution for dry run.

def transpose(matrix):
    new_matrix=[]
    for i in range(len(matrix[0])):
        temp=[]

        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        
        new_matrix.append(temp)
    return new_matrix
    
m=int(input("Enter no of rows: "))
n=int(input("Enter no of columns: "))
matrix=[]
for i in range(m):
    a=[]
    for j in range(n):
        a.append(int(input("Enter value: ")))
    matrix.append(a)
    
result=transpose(matrix)
print(result)