a = [(1,2,3)]
w=()
print a
b = (4,5,6)

a.append(b)

print a

for i in a:
	for z in i:
		print z

for x in range(1,1001):
	for y in range(x, 1001):
		for z in range (y, 1001):
			if x+y+z == 1000:
				w = (x,y,z)
				a.append(w)

for i in a:
	if i[0]**2 + i[1]**2 == i[2]**2:
		print i[0]*i[1]*i[2]
