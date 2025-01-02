
import random
from colorama import init, Fore
init(autoreset=True)

def displayBoard(board):
    print()
    print(" " + formatSymbol(board[0]) + " | " + formatSymbol(board[1]) + " | " + formatSymbol(board[2]))
    print(f"{Fore.CYAN}-----------")
    print(" " + formatSymbol(board[3]) + " | " + formatSymbol(board[4]) + " | " + formatSymbol(board[5]))
    print(f"{Fore.CYAN}-----------")
    print(" " + formatSymbol(board[6]) + " | " + formatSymbol(board[7]) + " | " + formatSymbol(board[8]))
    print()

def formatSymbol(symbol):
    if symbol == "X":
        return Fore.RED + symbol + Fore.RESET
    elif symbol == "O":
        return Fore.BLUE + symbol + Fore.RESET
    else:
        return Fore.YELLOW + symbol + Fore.RESET

def playerChoice():
    symbol = ""

    while symbol not in ["X", "O"]:
        symbol = input(f"{Fore.GREEN} Do you want to be X or O? ").upper()

    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def playerMove(board, symbol, playerName):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input(f"{Fore.GREEN} {playerName}, enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print(f"{Fore.RED} Invalid Move, please try again")
        except ValueError:
            print(f"{Fore.RED} Please enter a number between 1 until 9")

    board[move - 1] = symbol

def aiMove(board, aiSymbol, playerSymbol):
    # Check if ai can win in the next move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = aiSymbol
            if checkWin(board_copy, playerSymbol):
                board[i] = aiSymbol
                return 
            
    # Choose a random move
    possibleMove = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possibleMove)
    board[move] = aiSymbol

def checkWin(board, symbol):
    winCondition = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal Win
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical Win
        (0, 4, 8), (2, 4, 6) # Diagonal win
    ]

    for condition in winCondition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
        
    return False

def checkFull(board):
    return all(not spot.isdigit() for spot in board)

def tiktactoe():
    print(f"{Fore.YELLOW} Welcome to tik tac toe game!")
    playerName = input(f"{Fore.GREEN} Please enter your name: ")

    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        playerSymbol, aiSymbol = playerChoice()
        turn = "player"
        gameOn = True

        while gameOn:
            displayBoard(board)
        
            if turn == "player":
                playerMove(board, playerSymbol, playerName)
                if checkWin(board, playerSymbol):
                    displayBoard(board)
                    print(f"{Fore.GREEN} Congratulations {playerName}, you have won the game!")
                    gameOn = False
                else:
                    if checkFull(board):
                        displayBoard(board)
                        print(f"{Fore.YELLOW} It is a tie!")
                    else:
                        turn = "AI"

            else:
                print(f"{Fore.BLUE} Ai is making its move")
                aiMove(board, aiSymbol, playerSymbol)
                if checkWin(board, aiSymbol):
                    displayBoard(board)
                    print(f"{Fore.RED} Ai has won the game!")
                    gameOn = False
                else:
                    if checkFull(board):
                        displayBoard(board)
                        print(f"{Fore.YELLOW} It is a tie!")
                        break 
                    else:
                        turn = "player"
        
        playAgain = input(f"{Fore.GREEN} {playerName}, Do you want to play again? (yes/no): ").lower()
        if playAgain == "no":
            print(f"{Fore.CYAN} Thank you for playing")
            break

if __name__ == "__main__":
    tiktactoe()
