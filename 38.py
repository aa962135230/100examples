

list = []
sum = 0
for i in range(3):
	list.append([])
	for j in range(3):
		list[i].append(int(input('请输入你的数字：')))
for i in range(3):
	sum += list[i][i]
print(sum)