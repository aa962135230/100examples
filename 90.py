list = [10086,'zhuhua',[1,2,3,4]]


print(len(list))
print(list[1:])
list.append('i.m new here')
print(len(list))
print(list[-1])
print(list.pop(1))
print(len(list))
print(list)
matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1])
a= [row[1]for row in matrix]
print(a)
b = [row[1] for row in matrix if row[1]%2 ==0]
print(b)