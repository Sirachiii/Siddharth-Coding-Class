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
        conversation_history.append(text) 

        if sentiment > 0.75:
            positive_count += 1
            return "\n {Fore.GREEN} Very Positive sentiment detected, agent {user_name} score = {sentiment}"
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1
            return "\n {Fore.GREEN} Positive sentiment detected, agent {user_name} score = {sentiment}"
        elif -0.25 < sentiment <= 0.25:
            neutral_count += 1
            return "\n {Fore.YELLOW} Neutral sentiment detected, agent {user_name} score = {sentiment}"
        elif -0.75 < sentiment <= -0.25:
            return "\n {Fore.RED} Negative sentiment detected, agent {user_name} score = {sentiment}"
    except:
        return "\n {Fore.RED} Error occured during sentiment analyzation, agent {user_name}"

# - Append the user input to `conversation_history`
# - Update the sentiment counters based on the category
# - Handle exceptions to avoid crashes

# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command

# Define a function to validate the user's name
# - Continuously prompt the user for a name until they enter a valid alphabetic string
# - Strip any extra spaces and ensure the input is not empty or invalid

# Define the main function to start the chatbot
# - Display a welcome message and introduce the Sentiment Spy activity
# - Ask the user for their name and store it in the `user_name` variable
# - Enter an infinite loop to interact with the user:
#   - Prompt the user to enter a sentence or command
#   - Check for empty input and prompt the user to enter a valid sentence
#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
