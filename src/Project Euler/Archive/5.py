gotit = False

def divisible(x,y):
	if y == 1:
		return True
	if x % y == 0:
		return divisible(x,y-1)
	else:
		return False
i = 2519

while gotit == False:
	i += 1
	gotit = divisible(i, 20)
	

print i
	


#for i in range (2520, 100000000):
#	while gotit = false:
#		for z in range(1,21):
#			gotit = divisible(i,z) 

