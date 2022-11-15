from random import randint

tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]

def showTable(tableGame):
    for row in tableGame:
        for item in row:
            print (item, end="  ")
        print()
    
def caseFilled(board, x, y):
    if board[x][y] == '-':
        return False
    else:
        return True

def is_player_win(board, player):
    win = None

    n = len(board)

    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def is_board_filled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

def Morpion():
    playerOne = input("Joueur 1, entrez votre pseudo : ")
    playerTwo = input("Joueur 2, entrez votre pseudo : ")
    playerOneShoot = "X"
    playerTwoShoot = "O"
    playerStart = randint(1, 2)
    if playerStart == 1:
        print(playerOne + ", commence")
        playerTurn = playerOne
        playerShoot = playerOneShoot
    else:
        print(playerTwo + ", commence")
        playerTurn = playerTwo
        playerShoot = playerTwoShoot
    correctShoot = False
    playerWin = False
    showTable(tableGame)
    while playerWin == False:
        while correctShoot == False:
            print("Tour de " + playerTurn)
            choiceX = int(input("Ligne: "))
            choiceY = int(input("Colonne: "))
            if caseFilled(tableGame, choiceX, choiceY) != True:
                tableGame[choiceX][choiceY] = playerShoot
                correctShoot = True
        showTable(tableGame)

        if is_player_win(tableGame, playerShoot):
            print("Le joueur " + playerTurn + " à gagné la partie ! :)")
            break

        if is_board_filled(tableGame):
            print("Egalité ! :/")
            break

        if playerShoot == playerOneShoot:
            playerShoot = playerTwoShoot
            playerTurn = playerTwo
        else:
            playerShoot = playerOneShoot
            playerTurn = playerOne

        correctShoot = False
    
    otherGame = input("Voulez-vous rejouer ? oui ou non: ")
    if otherGame == "oui":
        print("C'est reparti !")
        Morpion()
    elif otherGame == "no":
        print("A bientôt !")

Morpion()