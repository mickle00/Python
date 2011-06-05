file = open('Soduku.txt', 'r')

NumberOfGames = 50
GamesDatabase = {}
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
        
#print GamesDatabase['Grid 50'] 

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
    possibleValues = list(set(neededValues) - set(squareValues))
    possibleValues = list(set(possibleValues) - set(rowValues))
    possibleValues = list(set(possibleValues) - set(columnValues))
    
    return possibleValues

def solveGame(Game):
    for row in range(0,9):
        for column in range (0,9):
            currentGame = GamesDatabase[Game]
            if currentGame[column][row] == '0':
                numberOfPossibilities = getPossibilities(Game, column, row)
                if len(numberOfPossibilities) == 1:
                    updateNumber(Game, column, row, numberOfPossibilities[0])
                    solveGame(Game)
                
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
        
for game in GamesDatabase.keys():
    print game
    solveGame(game)
    printGame(game)
    print '\n\n\n'    