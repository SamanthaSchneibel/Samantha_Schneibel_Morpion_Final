#on admet une fonction random
from random import randint

#créer un tableau vierge
tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]

#définir une fonction showtable
def showTable(tableGame):
    print("---------------")
    for row in tableGame:
        for item in row:
            print (item, end="  ")
        print()
    print("---------------\n")
    
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

def morpion():
    global tableGame
    playerOne = input("Joueur X, entrez votre pseudo : \n")
    playerTwo = input("Joueur O, entrez votre pseudo : \n")
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
            print("Tour de " + playerTurn + "\n")
            choiceX = int(input("Ligne: (ligne 1 = 0, ligne 2 = 1 et ligne 3 = 2 \n)"))
            choiceY = int(input("Colonne: (colonne 1 = 0, colonne 2 = 1 et colonne 3 = 2 \n)"))
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
    
    otherGame = input("Voulez-vous rejouer ? oui ou non : ")
    if otherGame == "oui":
        tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
        print("C'est reparti !")
        morpion()
    elif otherGame == "no":
        print("A bientôt !")

morpion()