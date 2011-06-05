all = []

xx = "stupid"
maxi = 0

for i in range(1,1000):
	for z in range (1,1000):
		all.append(i*z)
all.sort()

#print all

l = len(all)

max = ''
max2 = []


for i in all:
	while max == '':
		test = str(all[l-1])
		l = l-1
		if len(test) == 6:
			if test[0] == test[5]:
				if test[1] == test[4]:
					if test[2] == test[3]:
						max=test
						max2.append(test)
						max2.sort()

print max
print max2

for i in range(1,1000):
	for z in range (1,1000):
		if (i*z) == int(max2[len(max2)-1]):
			print "I is: ", i
			print "Z is: ", z



