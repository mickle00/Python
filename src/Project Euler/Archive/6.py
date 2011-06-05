firstsum = 0
add = 0

for i in range (1,101):
	firstsum += i**2
	add += i

print firstsum

print add

print add**2


print 'answer is: ',  (add**2 - firstsum)

