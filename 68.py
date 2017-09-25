list1 = [123,999,568,987,1024,35,742,841,888]
list2 = []

m = int(input('please input your number:'))

for i in range(len(list1)-m,len(list1)):
	list2.append(list1[i])
	
for i in range(len(list1)-m+1,0,-1):
	list1[i]=list1[i-m]
	
for i in range(m):
	list1[i]=list2[i]
	
print(list1)