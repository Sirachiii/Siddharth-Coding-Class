import re
import random
from colorama import Fore, init
init(autoreset=True) # Initalize Colourama

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    #add cities
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def greetUser():
    print(f"{Fore.CYAN} Hello, I am travel bot, your virtual travel assistant")
    user_name = input(f"{Fore.YELLOW} What is your name? ")
    print(f"{Fore.GREEN} Nice to meet you {user_name}, How can I assist you today?")
    return user_name

# Function to show help options
def showHelp():
    print(f"{Fore.MAGENTA} I can assist you with the following: ") 
    print(f"{Fore.GREEN} - Profile travel reccomendation ")
    print(f"{Fore.GREEN} - Offer packing tips")
    print(f"{Fore.GREEN} - Tell travel jokes")
    print(f"{Fore.CYAN} - Just ask me questions or type 'exit' to leave")

# Function to process user input


# Function to provide travel recommendations

# Function to check flight status (simulated)


# Function to offer packing tips


# Function to tell a joke


# Main chat function


# Start the chatbot

