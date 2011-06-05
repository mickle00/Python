from math import sqrt

big = 0
i = 2
pf = []


num = 600851475143/71/839/1471/6857


while big == 0 and i < 1000000:
	if int(num)/i == float(num)/i:
		big = i
	else:
		i += 1


print big

