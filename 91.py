import time

print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))

start = time.time()
print(start)
for i in range(3000):
	print(i)
end = time.time()
print(end-start)



