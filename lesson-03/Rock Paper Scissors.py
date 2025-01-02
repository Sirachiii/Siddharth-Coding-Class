import random
from colorama import init, Fore
init(autoreset=True)

choices = {1: "Scissors", 2: "Rock", 3: "Paper"}

winConditions = [
    [1, 2], 
    [3, 1], 
    [2, 3]   
]

playerScore = 0
aiScore = 0

def getUserOption():
    while True:  
        print(f"{Fore.CYAN}Pick your item:")
        print(f"{Fore.GREEN}1 = Scissors")
        print(f"{Fore.GREEN}2 = Rock")
        print(f"{Fore.GREEN}3 = Paper")
        userChoice = input(f"{Fore.YELLOW}Option Chosen: ") 
        
        if userChoice.isdigit() and int(userChoice) in choices:
            return int(userChoice)  
        print(f"{Fore.RED}Invalid choice, try again!")

def checkWin(player, ai):
    if [player, ai] in winConditions:
        return "player"
    elif [ai, player] in winConditions:
        return "ai"
    else:
        return "tie"

def game():
    global playerScore, aiScore
    print(f"{Fore.MAGENTA}Welcome to Rock Paper Scissors!")

    while True: 
        userChoice = getUserOption()
        aiChoice = random.randint(1, 3)

        winner = checkWin(userChoice, aiChoice) 

        print(f"{Fore.CYAN}You chose {choices[userChoice]}.")
        print(f"{Fore.CYAN}AI chose {choices[aiChoice]}.")

        if winner == "player":
            playerScore += 1
            print(f"{Fore.GREEN}You won!", end="")
        elif winner == "ai":
            aiScore += 1
            print(f"{Fore.RED}You lost!", end="")
        elif winner == "tie":
            print(f"{Fore.YELLOW}It's a tie!", end="")
        print(f"{Fore.YELLOW} Score: {playerScore}-{aiScore}")

        repeatOption = input(f"{Fore.CYAN}Play again? (yes/no): ").lower() 
        if repeatOption != "yes":
            print(f"{Fore.BLUE}Final Score: {Fore.YELLOW}{playerScore}-{aiScore}")
            print(f"{Fore.BLUE}Bye, thanks for playing!")
            break

if __name__ == "__main__":
    game()
