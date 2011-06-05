import re
import string

f = open('names.txt', 'r')
listofnames = []
a = f.read()
a = re.sub('"','', a)
b = re.split(',', a)

b.sort()

namedict = {}
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphdict = {}

count = 1
for i in b:
	namedict[i] = count
	#print i
	count += 1

#print namedict['QUINCY']
count = 1
for i in alph:
	s = string.upper(i)
	alphdict[s] = count
	count += 1

total = 0
namevalue = 0
lettervalue = 0

for i in b:
	namevalue = namedict[i]
	#print "i is: ", i
	for y in range(len(i)):
		#print "y is: ", i[y]
		lettervalue += alphdict[i[y]]

	total += namevalue * lettervalue
	lettervalue = 0


print "total value is: ", total	

