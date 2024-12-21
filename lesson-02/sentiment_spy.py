# Import necessary libraries
from textblob import TextBlob # - TextBlob for natural language processing tasks like sentiment analysis
import colorama # - Colorama for colored terminal output
from colorama import Fore, Style
import sys # - sys and time for animations and delays
import time # time module to create delays for animation

# Initialize Colorama to reset terminal colors automatically after each output
colorama.init(autoreset=True)

# Define global variables
user_name = "" # - `user_name`: To store the name of the user (Agent)
conversation_history = [] # - `conversation_history`: A list to store all user inputs

# - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends
positive_count = 0
negative_count = 0
neutral_count = 0

# Define a function to simulate a processing animation
def showProcessingAnimation():
    print(f"{Fore.CYAN} Detecting Sentiment Clues", end="")
    for _ in range(3): # - Prints "loading dots" to make the chatbot feel interactive
        time.sleep(0.5)
        print(".", end="") # - Use a loop to display three dots with a slight delay
        sys.stdout.flush() # Force terminal to display output immediately

# Define a function to analyze sentiment of the text
def analyzeSentiment(text):
    # Global variable 
    global positive_count, negative_count, neutral_count

    # - Use TextBlob to calculate the polarity of the input text
    # - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        conversation_history.append(text) # - Append the user input to `conversation_history`

        # - Update the sentiment counters based on the category
        if sentiment > 0.75:
            positive_count += 1
            return f"\n {Fore.GREEN} Very Positive sentiment detected, agent {user_name} score = {sentiment}"
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1
            return f"\n {Fore.GREEN} Positive sentiment detected, agent {user_name} score = {sentiment}"
        elif -0.25 < sentiment <= 0.25:
            neutral_count += 1
            return f"\n {Fore.YELLOW} Neutral sentiment detected, agent {user_name} score = {sentiment}"
        elif -0.75 < sentiment <= -0.25:
            return f"\n {Fore.RED} Negative sentiment detected, agent {user_name} score = {sentiment}"
        elif sentiment < -0.75: 
            return f"\n {Fore.RED} Very Negative sentiment detected, agent {user_name} score = {sentiment}" 

    except Exception as e: # - Handle exceptions to avoid crashes
        return f"\n {Fore.RED} Error occured during sentiment analyzation, agent {user_name}. {str(e)}"




# Define a function to handle commands
def executeCommand(command):
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command
    global conversation_history, positive_count, negative_count, neutral_count
    if command == "summary":
        return (f"{Fore.CYAN} Mission Report \n"
                f"{Fore.GREEN} Positive Messages detected = {positive_count}\n"
                f"{Fore.YELLOW} Neutral Messages detected = {neutral_count}\n"
                f"{Fore.RED} Negative Messages detected = {negative_count}\n"
                )
    
    elif command == "reset":
        # Clear all Data
        conversation_history.clear()
        positive_count = neutral_count = negative_count = 0 # Reset Counter
        return (f"{Fore.CYAN} Mission Reset all previous data all been cleared")
    
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN} Message {i + 1} = {msg}" for i ,msg in enumerate(conversation_history)]) \
                if conversation_history else f"{Fore.YELLOW} No Conversation history available" 
    
    elif command == "help":
        # Display list of available commands
        return (f"{Fore.CYAN} Available Commands \n"
                f"Type any sentence to analyze its sentiment \n"
                f"Type 'summary' to get a mission report on analyze sentiment \n"
                f"Type 'reset' to clear all of data and start fresh \n"
                f"Type 'history' to view all previous messages \n"
                f"Type 'exit' to conclude your mission and exit the chat \n")

    else:
        # Handle unknown commands
        return f"{Fore.RED} Unknown command, type 'help' for a list of commands" 


# Define a function to validate the user's name
def getValidName():

    # - Continuously prompt the user for a name until they enter a valid alphabetic string
    while True:
        name = input("What is your name? ").strip() # - Strip any extra spaces and ensure the input is not empty or invalid
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED} Please enter a valid name, with only alphabetic letters")

# Define the main function to start the chatbot
def startSentimentChat():

    print(f"{Fore.CYAN} {Style.BRIGHT} Welcome to sentiments spy, we will detect your personal emotion")# - Display a welcome message and introduce the Sentiment Spy activity
    
    # - Ask the user for their name and store it in the `user_name` variable
    global user_name
    user_name = getValidName()
    print(f"{Fore.CYAN} Nice to meet you agent {user_name} Type your sentence to analyze your emotion. Type 'help' for options")

    # - Enter an infinite loop to interact with the user:
    while True:

        userinput = input(f"{Fore.MAGENTA} {Style.BRIGHT} Agent {user_name} : {Style.RESET_ALL} ").strip() #   - Prompt the user to enter a sentence or command
        
        #   - Check for empty input and prompt the user to enter a valid sentence
        if not userinput:
            print(f"{Fore.RED} Please enter non empty message or type 'help'")
            continue

#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`
        if userinput.lower() == "exit":
            print(f"{Fore.BLUE} Mission complete, exiting sentiments spy. Farewell agent {user_name}")
            print(executeCommand('summary'))
            break

        elif userinput.lower() in ["summary", "reset", "history", "help"]:
            print(executeCommand(userinput.lower()))
        
        else:
            # Simulating process animation and analyze sentiment
            showProcessingAnimation()
            result = analyzeSentiment(userinput)
            print(result)

# Define the entry point for the script
if __name__ == "__main__":
    startSentimentChat()
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
