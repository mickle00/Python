from math import sqrt

pf = []
pf2 = []

num = 600851475143.0
snum = int(sqrt(num))

for i in range(1, snum):
	if (int(num)/i == float(num)/i) : pf.append(i)

def prime(x):
	num = x
	snum = sqrt(float(x))
	snum = int(snum)
	for i in range (1, snum):
		if int(num)/i != float(num)/i:
			if i in pf: pf.remove(i)
	for i in pf:
		if i not in pf2:
			pf2.append(i)
			print i
			

	#prime(len(pf2)-1)
		
	##prime(i)

	##print pf2

l = len(pf)
#print pf[l-1]
prime(pf[l-1])				
print pf2


