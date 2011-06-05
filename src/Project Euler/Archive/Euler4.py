#A palindromic number reads the same both ways. The largest palindrome made from the #product of two 2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the product of two 3-digit numbers.

maxz = 0
maxy = 0
gotit = "false"
y = 999
z = 999
u = 0

def palindrome(x):
	if len(x) == 1:
		gotit = "true"
		return gotit
	if len(x) == 2:
		if x[0] == x[1]:
			gotit = "true"
			return gotit
	## test if even
	if len(x) == 3:
		if int(len(x))/2 == float(len(x))/2:
			palindrome(x[1:-1])
			
		else:
			gotit = "false"
	if len(x) > 3:
		if int(len(x))/2 == float(len(x))/2:
			palindrome(x[1:-1])
		else:
			gotit = "false"

			
		
#palindrome("elle")


while palindrome(str(u)) == "true" and len(str(u)) > 1:
	if y > maxy:
		maxy = y
	if z > maxz:
		maxz = z
	print "y is: ", y
	print "z is: ", z	
	
	print "u is: ", u
	print "palindrome sayz", palindrome(str(u))
	
	y = y -1
	u = y * z
	palindrome(str(u))

print maxy
print maxz

#print y
#print z
#print y * z

#x = raw_input("enterstuff: ")
#palindrome(x)

#x, y = 999, 999

#product = x * y



#while y > 0 and maxx == 0 and maxy == 0:
#	u = x * y
#	if palindrome(str(u)) == "true":
#		if x > maxx and y > maxy:
#			maxx = x
#			maxy = y
#	else: y = y -1


#while y > 0 and maxx == 0 and maxy == 0:
	#u = x * y
	#if palindrome(str(u)) == "true":
	#	if x > maxx and y > maxy:
	#		maxx = x
	#		maxy = y
	#else: 
	#	y = y -1
	#	x = x -1

#print x,y
