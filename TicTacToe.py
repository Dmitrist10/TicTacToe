import random

field = []
fieldSize = 3
isPlaying = True
currentPlayer = "x"
winState = "" 


# custom Clamp function
def Clamp(value, min, max) -> int:
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value
    



def DisplayGameField(size: int):

    # Iterate in reverse
    for i in range(size - 1, -1, -1):
        # Y axis
        print(i+1, end=" ")

        # Main game field
        for j in range(size):
            print(field[i][j], end=" ")
        print()

    # X axis numbers 
    for i in range(size + 1):
        print(i, end=" ")
    print()



# check if bot/player has won
def CheckHasWin(player : str):
    global fieldSize
    global field

    for row in field:
        if all(cell == player for cell in row):
            return True
    for col in range(fieldSize):
        if all(field[row][col] == player for row in range(fieldSize)):
            return True

    #Diagonal check
    if all(field[i][i] == player for i in range(fieldSize)):
        return True
    if all(field[i][fieldSize - 1 - i] == player for i in range(fieldSize)):
        return True

    return False

def CheckDraw():
    global fieldSize
    global field

    for i in range(fieldSize):
        for j in range(fieldSize):
            if field[i][j] == "-":
                return False

    return True



def GetUserMove():

    while True:
        userInput = input(f"X Y: ")
        if HandleUserInput(userInput):
            break

    ChangeCurrentPlayer()

def GetBotMove():

    while True:
        userInput = " ".join(
            [str(random.randint(1, fieldSize + 1)), str(random.randint(1, fieldSize + 1))])
        if HandleUserInput(userInput):
            break

    ChangeCurrentPlayer()

def HandleUserInput(userInput):
    global fieldSize
    global currentPlayer

    parts = list(userInput.split())

    # check if it has more than 2 parts
    # check if it is numeric for both parts
    # check if the value is in the field size
    if len(parts) != 2 or str(parts[0]).isnumeric() == False or str(parts[1]).isnumeric() == False or int(parts[0]) > fieldSize or int(parts[1]) > fieldSize:
        print("Invalid input!")
        return False

    x = int(parts[0]) - 1
    y = int(parts[1]) - 1

    if field[y][x] == "-":
        field[y][x] = currentPlayer
        return True
    else:
        return False



def ChangeCurrentPlayer():
    global currentPlayer

    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

def Restart():
    global fieldSize
    global field
    global currentPlayer

    fieldSize = Clamp(int(input("field Size (2-5): ")), 2, 5)
    field = [["-" for _ in range(fieldSize)] for _ in range(fieldSize)]
    currentPlayer = "x"

def RestartGame():
    global isPlaying
    print("========================")
    DisplayGameField(fieldSize)
    print("========================")
    print(f"Round: {winState}")

    restartInput = input("Would you like to restart? (yes/no): ")

    if restartInput.lower() == "yes":
        Restart()
        return True
    elif restartInput.lower() == "no":
        global isPlaying
        isPlaying = False
        return False
    else:
        print("Invalid input!")
        RestartGame()



# Gameloop

# DisplayGameField()
# Check for game ended
# Player turn
# Check for game ended
# Bot turn
def GamePlayLoop():
    global winState
    Restart()

    while isPlaying:
        print("========================")
        DisplayGameField(fieldSize)
        print("========================")

        if CheckDraw():
            winState = "draw"
            if RestartGame():
                continue
        elif CheckHasWin("o"):
            winState = "lost"
            if RestartGame():
                continue
        elif CheckHasWin("x"):
            winState = "win"
            if RestartGame():
                continue

        GetUserMove()

        if CheckDraw():
            winState = "draw"
            if RestartGame():
                continue
        elif CheckHasWin("o"):
            winState = "lost"
            if RestartGame():
                continue
        elif CheckHasWin("x"):
            winState = "win"
            if RestartGame():
                continue

        GetBotMove()

GamePlayLoop()