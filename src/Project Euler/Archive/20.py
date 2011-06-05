import math

num = math.factorial(100)
num = str(num)
numsum = 0

for i in num:
	numsum += int(i)

print numsum
