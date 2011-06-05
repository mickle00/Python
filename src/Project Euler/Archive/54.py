import re

f = open('poker.txt', 'r')
a = []
p1 = []
p2 = []
p1count = 0
p2count = 0
update = [0,0]


highcardvalue = {'1':10,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '11':11, '12': 12, '13':13, '14':14, '10':10}
lowcardvalue = {'1':10,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':1, '11':11, '12': 12, '13':13, '14':14, '10':10}

for line in f.readlines():
	line = line.strip()
	a.append(line)

for i in a:
	p1temp = []
	p2temp = []
	p1temp.append(i[0:2])
	p1temp.append(i[3:5])
	p1temp.append(i[6:8])
	p1temp.append(i[9:11])
	p1temp.append(i[12:14])
	p2temp.append(i[15:17])
	p2temp.append(i[18:20])
	p2temp.append(i[21:23])
	p2temp.append(i[24:26])
	p2temp.append(i[27:29])
	#print "p1temp ", p1temp
	#print "p2temp ", p2temp
	p1.append(p1temp)
	p2.append(p2temp)

#for i in len(p1):

def royal(list):
	if straightflush(list) != None and highcard(list) == 14:
		return True
	else:
		return None

def betterroyal(list1, list2):
	if royal(list1) != None:
		return list1
	elif royal(list2) != None:
		return list2
	else:
		return None

def straightflush(list):
	if straight(list) != None and flush(list) != None:
		return straight(list)
	else:
		return None

def betterstraightflush(list1, list2):
	if straightflush(list1) == None and straightflush(list2) != None:
		return list2
	if straightflush(list1) != None and straightflush(list2) == None:
		return list1
	if straightflush(list1) != None and straightflush(list2) != None:
		if straightflush(list1) > straightflush(list2):
			return list1
		elif straightflush(list2) > straightflush(list1):
			return list2
	else:
		return None

def fourofakind(list):
	fourofakindlist = []
	highcardlist =[]
	for i in range(0, 5):
		highcardlist.append(list[i][0])

	for i in highcardlist:
		if highcardlist.count(i) > 3:
			fourofakindlist.append(highcardvalue[i])
	fourofakindlist.sort(reverse=True)
	if len(fourofakindlist) > 0:
		return fourofakindlist[0]
	else:
		return None

def betterfourofakind(list1, list2):
	if fourofakind(list1) == None and fourofakind(list2) != None:
		return list2
	if fourofakind(list1) != None and fourofakind(list2) == None:
		return list1
	if fourofakind(list1) != None and fourofakind(list2) != None:
		if fourofakind(list1) > fourofakind(list2):
			return list1
		else:
			return list2
	else:
		return None
def fullhouse(list):
	cardslist = []
	threeofakindlist = []
	pairlist = []
	highcardpairlist =[]
	highcardthreeofakindlist =[]
	fullhouselist = []
	for i in range(0, 5):
		cardslist.append(list[i][0])

	for i in cardslist:
		if cardslist.count(i) == 3 and highcardvalue[i] not in threeofakindlist:
			threeofakindlist.append(highcardvalue[i])

	threeofakindlist.sort(reverse=True)

	for i in cardslist:
		if cardslist.count(i) == 2 and highcardvalue[i] not in pairlist: # and i not in threeofakindlist:
			pairlist.append(highcardvalue[i])

	if len(threeofakindlist) == 1: fullhouselist.append(threeofakindlist[0])
	if len(pairlist) == 1: fullhouselist.append(pairlist[0])

	fullhouselist.sort(reverse=True)
	
	if len(fullhouselist) == 2:
		return fullhouselist
		#return list
	else:
		return None

def betterfullhouse(list1, list2):

	if fullhouse(list1) !=None and fullhouse(list2) == None:
		return list1
	elif fullhouse(list1) == None and fullhouse(list2) != None:
		return list2
	elif fullhouse(list1) != None and fullhouse(list2) != None:
		if fullhouse(list1)[0] > fullhouse(list2)[0]:
			return list1
		elif fullhouse(list1)[0] == fullhouse(list2)[0]:
			if fullhouse(list1)[1] > fullhouse(list2)[1]:
				return list1
			else:
				return list2
		#elif fullhouse(list1) == None and fullhouse(list2) == None:
			#return None
		else:
			return list2

	else:
		return None

def flush(list):
	newlist = []
	if list[0][1] == list[1][1] == list[2][1] == list[3][1] == list[4][1]:
		for i in range(0,5):
			newlist.append(highcardvalue[list[i][0]])
		newlist.sort(reverse=True)
		return newlist[0]
	else:
		return None

def betterflush(list1, list2):
	if flush(list1) != None and flush(list2) == None:
		return list1
	if flush(list1) == None and flush(list2) != None:
		return list2
	if flush(list1) != None and flush(list2) != None:
		if flush(list1) > flush(list2):
			return list1
		elif flush(list2) > flush(list1):
			return list2
	else:
		return None

def straight(list):
	orderlist = []
	highordervaluelist = []
	lowordervaluelist = []	
	for i in range(0, 5):
		orderlist.append(list[i][0])

	for i in orderlist:
		highordervaluelist.append(highcardvalue[i])

	highordervaluelist.sort(reverse=True)

	for i in orderlist:
		lowordervaluelist.append(lowcardvalue[i])

	lowordervaluelist.sort(reverse=True)

	if highordervaluelist[-1] == highordervaluelist[-2]-1 == highordervaluelist[-3]-2 == highordervaluelist[-4]-3 == highordervaluelist[-5]-4:
		if highcardvalue[str(highordervaluelist[0])] == 14:
			return highordervaluelist[0]
		else:
			return highordervaluelist[0]

	elif lowordervaluelist[-1] == lowordervaluelist[-2]-1 == lowordervaluelist[-3]-2 == lowordervaluelist[-4]-3 == lowordervaluelist[-5]-4 :
		if lowcardvalue[str(lowordervaluelist[0])] == 14:
			return lowordervaluelist[1]
		else:
			return lowordervaluelist[0]
	else:
		return None

def betterstraight(list1, list2):
	if straight(list1) != None and straight(list2) == None:
		return list1
	if straight(list1) == None and straight(list2) != None:
		return list2
	if straight(list1) != None and straight(list2) != None:
		if straight(list1) > straight(list2):
			return list1
		elif straight(list2) > straight(list1):
			return list2
	else:
		return None

def threeofakind(list):
	threeofakindlist = []
	highcardlist =[]
	for i in range(0, 5):
		highcardlist.append(list[i][0])

	for i in highcardlist:
		if highcardlist.count(i) > 2:
			threeofakindlist.append(highcardvalue[i])
	threeofakindlist.sort(reverse=True)
	if len(threeofakindlist) > 0:
		return threeofakindlist[0]
	else:
		return None

def betterthreeofakind(list1, list2):
	if threeofakind(list1) != None and threeofakind(list2) == None:
		return list1
	elif threeofakind(list1) == None and threeofakind(list2) != None:
		return list2
	elif threeofakind(list1) != None and threeofakind(list2) != None:
		if threeofakind(list1) > threeofakind(list2):
			return list1
		elif threeofakind(list1) < threeofakind(list2):
			return list2
		elif threeofakind(list1) == threeofkind(list2):
			print "THREEOFADEBUG"
			return None
	else:
		return None

def twopair(list):
	pairs = []
	highcardlist =[]
	for i in range(0, 5):
		highcardlist.append(list[i][0])

	for i in highcardlist:
		if highcardlist.count(i) > 1 and highcardvalue[i] not in pairs:
			pairs.append(highcardvalue[i])

	pairs.sort(reverse=True)
	if len(pairs) > 1:
		return pairs[0:2]
	else:
		return None

def bettertwopair(list1, list2):
	if twopair(list1) != None and twopair(list2) == None:
		return list1
	if twopair(list1) == None and twopair(list2) != None:
		return list2
	if twopair(list1) == None and twopair(list2) == None:
		return None
	if twopair(list1)[0] > twopair(list2)[0]:
		return list1
	elif twopair(list1)[0] == twopair(list2)[0]:
		if twopair(list1)[1] > twopair(list2)[1]:
			return list1
		else:
			return list2
	elif twopair(list2)[0] > twopair(list1)[0]:
		return list2
	else:
		return None

def pair(list):
	highestpair = []
	highcardlist =[]
	for i in range(0, 5):
		highcardlist.append(list[i][0])

	for i in highcardlist:
		if highcardlist.count(i) > 1:
			highestpair.append(highcardvalue[i])
	highestpair.sort(reverse=True)
	if len(highestpair) > 0:
		return highestpair[0]
	else:
		return None

def betterpair(list1, list2):
	if pair(list1) != None and pair(list2) == None:
		return list1
	if pair(list1) == None and pair(list2) != None:
		return list2
	if pair(list1) != None and pair(list2) != None:
		if pair(list1) > pair(list2):
			return list1
		elif pair(list2) > pair(list1):
			return list2
		elif pair(list1) == pair(list2):
			print "######### DEBUG ME #########"
			## FIX THIS LATER
			##betterhighcard(list1, list2)
	else:
		return None

def highcard(list):
	highcard = 0
	highcardlist =[]
	for i in range(0, 5):
		highcardlist.append(list[i][0])

	for i in highcardlist:
		temphigh = highcardvalue[i]
		if temphigh > highcard:
			highcard = temphigh

	return highcard


def betterhighcard(list1, list2):
	if highcard(list1) > highcard(list2):
		return list1
	else:
		return list2


def winner(hand, value):
	print "Hand", hand, "won with ", value, "\n"
	#print "\n"

HighCardCount = 0
PairCount = 0
TwoPairCount = 0
ThreeofaKindCount = 0
StraightCount = 0
FlushCount = 0
FullHouseCount = 0
FourofaKindCount = 0
StraightFlushCount = 0
RoyalFlushCount = 0


def winnertype(type):
	global HighCardCount
	global PairCount
	global TwoPairCount
	global ThreeofaKindCount
	global StraightCount
	global FlushCount
	global FullHouseCount
	global FourofaKindCount
	global StraightFlushCount
	global RoyalFlushCount
	if type == "highcard": HighCardCount = HighCardCount + 1
	if type == "pair": PairCount += 1
	if type == "twopair": TwoPairCount += 1
	if type == "threeofakind": ThreeofaKindCount += 1
	if type == "straight": StraightCount += 1
	if type == "flush": FlushCount += 1
	if type == "fullhouse": FullHouseCount += 1
	if type == "fourofakind": FourofaKindCount += 1
	if type == "straightflush": StraightFlushCount +=1
	if type == "royalflush": RoyalFlushCount += 1

def breakdown():
	print "\n#### BREAKDOWN ####"
	global HighCardCount
	global PairCount
	global TwoPairCount
	global ThreeofaKindCount
	global StraightCount
	global FlushCount
	global FullHouseCount
	global FourofaKindCount
	global StraightFlushCount
	global RoyalFlushCount

	print "High Cards:", HighCardCount
	print "Pairs:", PairCount
	print "Two Pair:", TwoPairCount
	print "Three of a Kind:", ThreeofaKindCount
	print "Straights:", StraightCount
	print "Flush:", FlushCount
	print "Full Houses:", FullHouseCount
	print "Four of a Kind:", FourofaKindCount
	print "Straight Flush:", StraightFlushCount
	print "Royal Flush:", RoyalFlushCount

	totalcount = HighCardCount + PairCount + TwoPairCount + ThreeofaKindCount + StraightCount + FlushCount + FullHouseCount + FourofaKindCount + StraightFlushCount + RoyalFlushCount
	print "\nTotal Count:", totalcount

def betterhand(listone, listtwo):

	p1add = 0
	p2add = 0

	for i in range(len(listone)):
		list1 = listone[i]
		list2 = listtwo[i]
		print "Hand 1: ", list1
		print "Hand 2: ", list2

		if betterroyal(list1, list2) != None:
			winnertype("royalflush")
			if betterroyal(list1, list2) == list1:
				p1add = p1add + 1
				winner(1, "Royal Flush")
			else:
				p2add = p2add +1
				winner(2, "Royal Flush")

		elif betterstraightflush(list1, list2) != None:
			winnertype("straightflush")
			if betterstraightflush(list1, list2) == list1:
				p1add = p1add + 1
				winner(1, "Straight Flush")
			else: 
				p2add = p2add + 1
				winner(2, "Straight Flush")
		elif betterfourofakind(list1, list2) != None:
			winnertype("fourofakind")
			if betterfourofakind(list1, list2) == list1:
				p1add = p1add +1
				winner(1, "Four of a kind")
			else:
				p2add = p2add +1
				winner(2, "Four of a kind")

		elif betterfullhouse(list1, list2) != None:
			winnertype("fullhouse")
			if betterfullhouse(list1, list2) == list1:
				p1add = p1add+1
				winnner(1, "Full House")
			else:
				p2add = p2add +1
				winner(2, "Full House")

		elif betterflush(list1, list2) != None:
			winnertype("flush")
			if betterflush(list1, list2) == list1:
				p1add = p1add + 1
				winner(1, "Flush")
			elif betterflush(list1, list2) == list2: 
				p2add = p2add + 1
				winner(2, "Flush")

		elif betterstraight(list1, list2) != None:
			winnertype("straight")
			if betterstraight(list1, list2) == list1:
				p1add = p1add + 1
				winner(1, "Flush")
			elif betterstraight(list1, list2) == list2: 
				p2add = p2add + 1
				winner(2, "Flush")


		elif betterthreeofakind(list1, list2) != None:
			winnertype("threeofakind")
			if betterthreeofakind(list1, list2) == list1:
				p1add = p1add +1
				winner(1, "Three of a kind")
			else:
				p2add = p2add +1
				winner(2, "Three of a Kind")

		elif bettertwopair(list1, list2) != None:
			winnertype("twopair")
			if bettertwopair(list1, list2) == list1:
				p1add = p1add +1
				winner(1, "Two Pair")
			else:
				p2add = p2add +1
				winner(2, "Two Pair")


		elif betterpair(list1, list2) !=None:
			winnertype("pair")
			if betterpair(list1, list2) == list1:
				p1add = p1add +1
				winner(1, "pair")
			elif betterpair(list1, list2) == list2:
				p2add = p2add +1
				winner(2, "pair")

		else:
			winnertype("highcard")
			if betterhighcard(list1, list2) == list1:
				winner(1, "highcard")
				p1add = p1add + 1
			elif betterhighcard(list1, list2) == list2:
				winner(2, "highcard")
				p2add = p2add + 1

	tempupdate = [p1add, p2add]
	
	return tempupdate

results = betterhand(p1, p2)
print "Hand 1 had", results[0], "winners."
print "Hand 2 had", results[1], "winners."

breakdown()

t1 = [['3S', '4S', '5S', '6S', '7D']]
t2 = [['8S', '4S', '5S', '6S', '7D']]


def test(listone, listtwo):

	p1add = 0
	p2add = 0

	for i in range(1):
		list1 = listone[i]
		list2 = listtwo[i]

		if betterhighcard(list1, list2) == list1:
			p1add = p1add + 1
		elif betterhighcard(list1, list2) == list2:
			p2add = p2add + 1

	tempupdate = [p1add, p2add]
	return tempupdate

#print betterhand(t1, t2)
#print straight(t1[0])
#print straight(t2[0])
#print betterstraight(t1[0], t2[0])
	

#p1count = update[0]
#p2count = update[1]

##def betterhandtest(list1, list2):
##	tempupdate = [0,0]
##	one = 0
##	two = 0
##	for i in range(-1, len(list1)):
##		one =  one + int(betterhand(list1[i], list2[i])
##		two = two + int(betterhand(list1[i], list2[i])
		#tempupdate = tempupdate + betterhand(list1[i], list2[i], list3)
##	tempupdate[0] = one
##	tempupdate [1] = two
##	return tempupdate

#betterhandtest(p1[0], p2[0], update)
#print len(p1)
#print len(p2)

##print(p1)

#print betterfullhouse(['3S', '3S', '3S', '7S', '7D'], ['3S', '3S', 'KS', 'KS', 'KD'])

#print betterhandtest([['3S', '4S', '5S', '6S', '7D'],['3S', '4S', '5S', 'TS', '7S'],['3S', '4S', '5S', '6S', '7S'],['3S', '4S', '5S', 'TS', '7S']], p2, [0,0])

#print betterhandtest([['3S', '4S', '5S', '6S', '7D'],['3S', '4S', '5S', 'TS', '7S'],['3S', '4S', '5S', '6S', '7S'],['3S', '4S', '5S', 'TS', '7S']], [['3S', '4S', '5S', '6S', 'AS'],['3S', '4S', '5S', '6S', '2D'],['3S', '4S', '5S', '6S', '2D'],['3S', '4S', '5S', 'TS', '2D']], [0,0])

#print betterhandtest(p1, p2, [0,0])

'''
print "\n#### UNIT TESTS #####"

print "\n#### HIGH CARD TESTS ####"
highcardtest = ['3S', '4S', '5S', '6S', '7S']
highcardtest2 = ['JS', '4S', 'AS', '6S', 'KS']
print "Highcard test should return 7: ", highcard(highcardtest)
print "Highcard2 test should return 14: ", highcard(highcardtest2)

print "\n#### BETTER HIGH CARD TEST ####"
highcardtest = ['3S', '4S', '5S', '6S', '7S']
highcardtest2 = ['JS', '4S', 'AS', '6S', 'KS']
print "Better Highcard test should return", highcardtest2, ": ", betterhighcard(highcardtest,highcardtest2)

print"\n#### PAIR TESTS ####"
pairtest = ['QS', 'QS', '5S', '5S', '7S']
pairtest2 = ['3S', '4S', '5S', 'QS', '7S']
print "Pair should return 12:", pair(pairtest)
print "Pair should return None:", pair(pairtest2)

print"\n#### BETTER PAIR TESTS ####"
pairtest = ['QS', 'QS', '5S', '5S', '7S']
pairtest2 = ['3S', '4S', '5S', 'QS', '7S']
print "Better should return", pairtest, ": ", betterpair(pairtest, pairtest2)

print"\n#### TWO PAIR TESTS ####"
twopairtest = ['QS', 'QS', '5S', '5S', '7S']
twopairtest2 = ['3S', '7S', '5S', 'QS', '7S']
print "Two Pair should return [12, 5]:", twopair(twopairtest)
print "Two Pair should return None:", twopair(twopairtest2)

print "\n#### BETTER TWO PAIR TEST ####"
twopairtest = ['4S', '4S', '7S', '6S', '7S']
twopairtest2 = ['4S', '4S', '6S', '6S', 'KS']
print "Better two pair test should return", twopairtest, ": ", bettertwopair(twopairtest,twopairtest2)

print"\n#### THREE OF A KIND TESTS ####"
threeofakindtest = ['QS', 'QS', 'QS', '5S', '7S']
threeofakindtest2 = ['3S', '4S', '5S', 'QS', '7S']
print "Three of a kind should return 12:", threeofakind(threeofakindtest)
print "Three of a kind should return None:", threeofakind(threeofakindtest2)

print"\n#### BETTER THREE OF A KIND TESTS ####"
threeofakindtest = ['QS', 'QS', 'QS', '5S', '7S']
threeofakindtest2 = ['5S', '5S', '5S', 'QS', '7S']
print "Better three of a kind should return:", threeofakindtest, ": ",  betterthreeofakind(threeofakindtest, threeofakindtest2)


print"\n#### STRAIGHT TESTS ####"
print "Nope, Alex Hortin is still gay IMO"
straighttest = ['AS', '2S', '3S', '5S', '4S']
straighttest2 = ['3S', '4S', '5S', '6S', '7S']
straighttest3 = ['8S', 'JS', 'QS', 'KS', 'AS']
straighttest4 = ['6S', '7S', '8S', '9S', 'TS']
straighttest5 = ['8S', '9S', '6S', 'JS', 'QS']
straighttest6 = ['TS', 'AS', 'KS', 'JS', 'QS']
print "Straight should return 5:", straight(straighttest)
print "Straight should return 7:", straight(straighttest2)
print "Straight should return None:", straight(straighttest3)
print "Straight should return 10:", straight(straighttest4)
print "Straight should return None:", straight(straighttest5)
print "Straight should return 14:", straight(straighttest6)


print"\n#### BETTERSTRAIGHT TESTS ####"
print "Better straight should return:", straighttest6, ": ", betterstraight(straighttest6, straighttest)

print "\n#### FLUSH TESTS ####"
flushtest = ['3S', '4S', '5S', '6S', '7S']
flushtest2 = ['3S', '4S', '5S', '6S', '7D']
flushtest3 = ['3S', '4S', '5S', '6S', 'TS']
flushtest4 = ['3D', '4S', '5S', '6S', 'TS']
print "Flushtest should return 7:", flush(flushtest)
print "Flushtest2 should return None:", flush(flushtest2)
print "Flushtest3 should return 10:", flush(flushtest3)

print "\n#### BETTER FLUSH TEST ####"
print "Best flush is", flushtest3, ": ", betterflush(flushtest, flushtest3)
print "Best flush is", "None", ": ", betterflush(flushtest4, flushtest2)

print "\n#### FULL HOUSE TESTS ####"
fullhousetest = ['3S', '3S', '3S', '6S', '6S']
fullhousetest2 = ['3S', '3S', '5S', '7S', '7D']
fullhousetest3 = ['3S', '3S', '3S', '6S', 'TS']
print "fullhousetest should return [6, 3]:", fullhouse(fullhousetest)
print "fullhousetest2 should return None:", fullhouse(fullhousetest2)
print "fullhousetest3 should return None:", fullhouse(fullhousetest3)


print "\n#### BETTER FULL HOUSE TEST ####"
print "Better fullhouse is", fullhousetest, ": ", betterfullhouse(fullhousetest, fullhousetest3)


print"\n#### FOUR OF A KIND TESTS ####"
fourofakindtest = ['QS', 'QS', 'QS', 'QS', '7S']
fourofakindtest2 = ['3S', '4S', '5S', 'QS', '7S']
print "Three of a kind should return 12:", fourofakind(fourofakindtest)
print "Three of a kind should return None:", fourofakind(fourofakindtest2)

print"\n#### BETTER FOUR OF A KIND TEST ####"
print "Four of a kind should return", fourofakindtest, ": ", betterfourofakind(fourofakindtest, fourofakindtest2)
print "Four of a kind should return", fourofakindtest, ": ", betterfourofakind(fourofakindtest2, fourofakindtest)

print "\n#### STRAIGHT FLUSH TESTS ####"
straightflushtest = ['8S', '4S', '5S', '6S', '7S']
straightflushtest2 = ['3S', '4S', '5S', '6S', '7D']
straightflushtest3 = ['3D', '4S', '5S', '6S', '7D']
print "Flushtest should return 8:", straightflush(straightflushtest)
print "Flushtest2 should return None:", straightflush(straightflushtest2)

print "\n#### BETTER STRAIGHT FLUSH TESTS #####"
print "Straight Flush Test should return", straightflushtest, ": ", betterstraightflush(straightflushtest, straightflushtest2)
print "Straight Flush Test should return", "None", ": ", betterstraightflush(straightflushtest3, straightflushtest2)

print "\n#### ROYAL FLUSH TESTS ####"
royaltest = ['TS', 'JS', 'QS', 'KS', 'AS']
royaltest2 = ['TS', 'JS', 'QS', 'KS', 'AD']
print "Royal should return True:", royal(royaltest)
print "Royal should return None:", royal(royaltest2)

print "\n"
'''

