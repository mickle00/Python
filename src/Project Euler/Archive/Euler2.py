start1 = 1
start2 = 2

fibnum = [1,2]

sum = 0

while sum < 4000001:
	if start1 + start2 < 4000001:
		sum = start1 + start2
		start1 = start2
		start2 = sum
		fibnum.append(sum)
	else:
		break

total=0
for i in fibnum:
	if float(i)/2 == int(i)/2:
		total = total + i	

print fibnum

print "total = ", total
