a = int(input('请输入成绩：'))

if a >= 90:
	grade = 'A'
elif 60<= a and a<90:
	grade = 'B'
else:
	grade = 'C'
	
print('%d属于%s'%(a,grade))