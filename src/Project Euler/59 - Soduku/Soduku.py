import random
file = open('Soduku.txt', 'r')

NumberOfGames = 50
GamesDatabase = {}
rollBackPoint = {}
choices = {}

for i in range(NumberOfGames): 
    Game = file.readline()
    Game = Game.strip()
    for z in range(9):
        line = file.readline()
        line = line.strip()
        currentLine = list(line)
        if Game in GamesDatabase:
            currentList = GamesDatabase[Game]
        else:
            currentList = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
                currentList[i].append(currentLine[i])
        GamesDatabase[Game] = currentList
        rollBackPoint[Game] = currentList
        
def buildUnknowns(Game):
    tempMap = {}
    currentList = GamesDatabase[Game]
    for x in range(0,9):
        for y in range (0,9):
            if currentList[x][y] == 0:
                tempMap[(x,y)] = 0
    return tempMap

#unKnownMap = buildUnknowns('Grid 15')

                

def getColumn(Game, columnNumber):
    currentColumn = GamesDatabase[Game][columnNumber]
    return currentColumn
 
def getRow(Game, rowNumber):
    currentGame = GamesDatabase[Game]
    currentList = []
    for i in range(9):
        currentList.append(currentGame[i][rowNumber])
    return currentList

def getSquare(Game, squareNumber):
    currentGame = GamesDatabase[Game]
    currentList = []

    if (squareNumber == 1 or squareNumber == 4 or squareNumber == 7):
        columns = [0,1,2]
    if (squareNumber == 2 or squareNumber == 5 or squareNumber == 8):
        columns = [3,4,5]
    if (squareNumber == 3 or squareNumber == 6 or squareNumber == 9):
        columns = [6,7,8]
    if (squareNumber == 1 or squareNumber == 2 or squareNumber == 3):
        rows = [0,1,2]
    if (squareNumber == 4 or squareNumber == 5 or squareNumber == 6):
        rows = [3,4,5]
    if (squareNumber == 7 or squareNumber == 8 or squareNumber == 9):
        rows = [6,7,8]
        
    for row in rows:
        for column in columns:
            currentList.append(currentGame[column][row])
            
    return currentList

def getSquareNumber(Game, columnNumber, rowNumber):
    currentGame = GamesDatabase[Game]
    if columnNumber < 3 and rowNumber < 3: return 1
    if columnNumber > 2 and columnNumber < 6 and rowNumber < 3: return 2
    if columnNumber > 5 and rowNumber < 3: return 3
    if columnNumber < 3 and rowNumber > 2 and rowNumber < 6: return 4
    if columnNumber > 2 and columnNumber < 6 and rowNumber > 2 and rowNumber < 6: return 5
    if columnNumber > 5 and rowNumber > 2 and rowNumber < 6: return 6
    if columnNumber < 3 and rowNumber > 5: return 7
    if columnNumber > 2 and columnNumber < 6 and rowNumber > 5: return 8
    if columnNumber > 5 and rowNumber > 5: return 9 
    

def getPossibilities(Game, columnNumber, rowNumber):
    neededValues = ['1','2','3','4','5','6','7','8','9']
    currentGame = GamesDatabase[Game]
    squareValues = getSquare(Game, getSquareNumber(Game, columnNumber, rowNumber))
    rowValues = getRow(Game, rowNumber)
    columnValues = getColumn(Game, columnNumber)
    possibleValues = list(set(neededValues) - set(squareValues) - set(rowValues) - set(columnValues))    
    return possibleValues

def getIndividualPossibilities(Game, columnNumber, rowNumber):
    neededValues = ['1','2','3','4','5','6','7','8','9']
    currentGame = GamesDatabase[Game]
    #squareValues = getSquare(Game, getSquareNumber(Game, columnNumber, rowNumber))
    rowValues = getRow(Game, rowNumber)
    columnValues = getColumn(Game, columnNumber)
    possibleValues = list(set(neededValues) - set(rowValues) - set(columnValues))    
    return possibleValues

def rowColumnSquareNeeded(Game, columnNumber, rowNumber):
    numberCountDictionary = {'1':0, '2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    myPossibilities = getPossibilities(Game, columnNumber, rowNumber)
    print "mypossibilites original",  myPossibilities
    for item in range(0,9):
        if item != columnNumber:
            if GamesDatabase[Game][item][rowNumber] == '0':
                possibility = getIndividualPossibilities(Game, item, rowNumber)
                for p in possibility:
                    numberCountDictionary[p] = numberCountDictionary[p] +1
                print "removing: ", possibility
                myPossibilities = list(set(myPossibilities) - set(possibility))
    for item in range (0,9):
        if item != rowNumber:
            if GamesDatabase[Game][columnNumber][item] == '0':
                possibility = getIndividualPossibilities(Game, columnNumber, item)
                for p in possibility:
                    numberCountDictionary[p] = numberCountDictionary[p] +1
                myPossibilities = list(set(myPossibilities) - set(possibility))
                print "removing: ", possibility
    lowcount = 100
    lowkey = 'haha'
    for key in numberCountDictionary.keys():
        if numberCountDictionary[key] < lowcount and numberCountDictionary[key] != 0:
            lowkey = key
            lowcount = numberCountDictionary[key]
    print 'lowkey is: ', lowkey
    return str(lowkey)

attempt = 1
myMap = {}
def solveGame(Game):
    global attempt
    if attempt == 1:
        for row in range(0,9):
            for column in range (0,9):
                key = (Game, column, row)
                currentGame = GamesDatabase[Game]
                if currentGame[column][row] == '0':
                    myMap[key] = 0
                    #numberOfPossibilities = getPossibilities(Game, column, row)
                    #if len(numberOfPossibilities) == 1:
                    #    updateNumber(Game, column, row, numberOfPossibilities[0])
                    #    solveGame(Game)
                    #    myMap.pop(key,'no')
                    #   break
                    #    break
    else:
        for item in myMap.keys():
            thisGame, column, row = item
            numberOfPossibilities = getPossibilities(thisGame, column, row)
            if len(numberOfPossibilities) == 1:
                updateNumber(Game, column, row, numberOfPossibilities[0])
                solveGame(Game)
                myMap.pop(key,'no')
                break
                       
    if attempt == 2:
        rollBackPoint[Game] = GamesDatabase[Game][:][:]
    if isSolved(Game) == False:
        if isPossible(Game) == False:
            GamesDatabase[Game] = rollBackPoint[Game][:][:]
        guessAndCheckGame(Game, attempt)
        attempt += 1
zeroMap = {}

def solve2(Game):
    #thisMap = buildUnknowns(Game).keys()
    unKnownMap = buildUnknowns('Grid 15')
   # print unKnownMap
    for unKnownValue in unKnownMap.keys():
        column, row = unKnownValue
        numberOfPossibilities = getPossibilities(Game, column, row)
        if len(numberOfPossibilities) == 1:
                updateNumber(Game, column, row, numberOfPossibilities[0])
                unKnownMap.pop((column, row),'no')
                print GamesDatabase[Game]
                solve2(Game)
    if isSolved(Game) == False:
        if isPossible(Game) == False:
            GamesDatabase[Game] = rollBackPoint[Game][:][:]
        guessAndCheckGame2(Game)

def guessAndCheckGame2(Game):
    unKnownMap = buildUnknowns('Grid 15')
    for item in unKnownMap.keys():
        numberOfPossibilities = getPossibilities(Game, GamesDatabase[Game][item[1]],GamesDatabase[Game][item[2]])
        if key in choices.keys():
                numberOfPossibilities = list(set(numberOfPossibilities) - set(choices[key]))
        else:
            choices[key] = ()
        if len(numberOfPossibilities) > 1:
            whichToChoose = random.randint(0,len(numberOfPossibilities)-1)
            t = choices[key]
            t = (t, whichToChoose)
            choices[key] = t
            updateNumber(Game, GamesDatabase[Game][item[1]],GamesDatabase[Game][item[2]], numberOfPossibilities[whichToChoose])
            solve2(Game)
            #break
        if len(numberOfPossibilities) == 0:
            GamesDatabase[Game] = rollBackPoint[Game][:][:]
            solve2(Game)
            #break
        
def guessAndCheckGame(Game, attempt):
    if attempt == 1:
        for row in range(0,9):
            for column in range (0,9):
                key = (Game, column, row)
                currentGame = GamesDatabase[Game]
                if currentGame[column][row] == '0':
                    zeroMap[key] = 0
                    #numberOfPossibilities = getPossibilities(Game, column, row)
                    #if key in choices.keys():
                    #        numberOfPossibilities = list(set(numberOfPossibilities) - set(choices[key]))
#                    else:
#                        choices[key] = ()
#                    if len(numberOfPossibilities) > 1:
#                        whichToChoose = random.randint(0,len(numberOfPossibilities)-1)
#                        t = choices[key]
#                        t = (t, whichToChoose)
#                        choices[key] = t
#                        updateNumber(Game, column, row, numberOfPossibilities[whichToChoose])
#                        solveGame(Game)
#                        break
#                        break
#                    if len(numberOfPossibilities) == 0:
#                        GamesDatabase[Game] = rollBackPoint[Game][:][:]
#                        solveGame(Game)
#                        break
#                        break
    else:
        for item in zeroMap.keys():
            numberOfPossibilities = getPossibilities(Game, GamesDatabase[Game][item[1]],GamesDatabase[Game][item[2]])
            if key in choices.keys():
                    numberOfPossibilities = list(set(numberOfPossibilities) - set(choices[key]))
            else:
                choices[key] = ()
            if len(numberOfPossibilities) > 1:
                whichToChoose = random.randint(0,len(numberOfPossibilities)-1)
                t = choices[key]
                t = (t, whichToChoose)
                choices[key] = t
                updateNumber(Game, GamesDatabase[Game][item[1]],GamesDatabase[Game][item[2]], numberOfPossibilities[whichToChoose])
                solveGame(Game)
                break
            if len(numberOfPossibilities) == 0:
                GamesDatabase[Game] = rollBackPoint[Game][:][:]
                solveGame(Game)
                break
        
                #if attempt == 1:
                #    updateNumber(Game, column, row, numberOfPossibilities[0])
                #else:
                #    updateNumber(Game, column, row, numberOfPossibilities[1])                        
                #solveGame(Game)
                #break
    attempt += 1
                
def Guess(Game, numberOfPossibilities, column, row):
    whichToRemove = random.randint(0,len(numberOfPossibilities)-1)
    updateNumber(Game, column, row, numberOfPossibilities[whichToRemove])
    solveGame(Game)
        
def isPossible(Game):
    currentGame = GamesDatabase[Game]
    for column in range(0,9):
        for row in range(0,9):
            if currentGame[column][row] == '0':
                numberOfPossibilities = getPossibilities(Game, column, row)
                if len(numberOfPossibilities) == 0:
                    return False
                    #break
                    #break
    return True
    
    #print rollBackPoint[Game]
    #print GamesDatabase[Game]
    #if not isSolved(Game) and attempt < 3:
    #    solveGame(Game)
                    
def isSolved(Game):
    currentGame = GamesDatabase[Game][:]
    for column in currentGame:
        for item in column:
            if item == '0':
                print 'says false'
                return False
                #break
                #break
    print 'says true'
    return True
                
def updateNumber(Game, columnNumber, rowNumber, value):
    currentGame = GamesDatabase[Game]
    currentGame[columnNumber][rowNumber] = value
    GamesDatabase[Game] = currentGame
    
def printGame(Game):
    currentGame = GamesDatabase[Game]
    for column in range (0,9):
        for row in range (0,9):
            print str(currentGame[row][column]),
        print ''
print solve2('Grid 15')

#printGame('Grid 15')
#print isSolved('Grid 15')
 
#printGame('Grid 15')
#solve2('Grid 15')
#print '\n\n'
#print "======>"
#printGame('Grid 15')    
#for game in range(11):
#    gamename = 'Grid ' + str(game)
#    solveGame(gamename)
#    print gamename, isSolved(gamename)
    #printGame(gamename)
#    print '\n\n\n'    