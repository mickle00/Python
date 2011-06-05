answer = False
whatitis = 0

for i in range (1,333):
	while answer == False:
		for z in range(i,333):
			while answer == False:
				for y in range(z,333):
					while answer == False:
						if i + z + y == 1000:
							if i**2 + z**2 == y**2:
								print i,z,y
								answer = True

	
