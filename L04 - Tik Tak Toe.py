
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
