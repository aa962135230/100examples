n = int(input('please input your number:'))
list=[]
for i in range(1,n+1):
	list.append(i)
	
sum=0
while(1):
	t = 0
	for i in range(1,len(list)+1):
		sum =sum+1
		if (sum)%3==0:
			list.pop(i-1-t)
			t = t + 1
			
	if len(list) == 1:
		print('the last num is %d'%list[0])
		break