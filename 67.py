a = [123,999,568,987,1024,35,742,841,888]
p = 0




max = 0
for i in range(1,9):
	p = i
	if a[p]>a[max]:
		max = p
k = max
a[0],a[k] = a[k],a[0]

print(a)