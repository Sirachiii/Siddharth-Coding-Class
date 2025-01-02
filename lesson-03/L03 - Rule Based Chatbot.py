import re
import random
from colorama import Fore, init
init(autoreset=True) # Initalize Colourama

# Data structures for travel recommendations
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities" : ["Tokyo", "Hong Kong", "Melbourne"]
}

weather = {
    "bali" : 25,
    "maldives" : 22,
    "phuket" : 30,
    "swiss Alps" : 6,
    "rocky Mountains" : 12,
    "himalayas" : 9,
    "tokyo" : 22,
    "hong Kong" : 25,
    "melbourne" : 18
}

localTime = {
    "bali": "3:52 PM",
    "maldives": "12:52 PM",
    "phuket": "2:52 PM",
    "swiss Alps": "8:52 AM",
    "rocky Mountains": "12:52 AM",
    "himalayas": "1:37 PM",
    "tokyo": "4:52 PM",
    "hong Kong": "3:52 PM",
    "melbourne": "6:52 PM"
}

news = {
    "bali": "New eco-resort in Bali wins award for sustainable tourism.",
    "maldives": "Maldives launches coral restoration program to combat reef damage.",
    "phuket": "Phuket announces expansion of its international airport to boost tourism.",
    "swiss Alps": "Swiss Alps to introduce new high-speed rail link for easier access.",
    "rocky Mountains": "Rocky Mountains hiking trail reopens after extensive renovations.",
    "himalayas": "Himalayan village installs solar panels to promote green energy.",
    "tokyo": "Tokyo debuts autonomous buses for public transportation system.",
    "hong Kong": "Hong Kong announces plans to redevelop waterfront promenade.",
    "melbourne": "New bakery downtown gains popularity for artisan sourdough bread."
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
    print(f"{Fore.GREEN} - Provide travel reccomendation ")
    print(f"{Fore.GREEN} - Offer packing tips")
    print(f"{Fore.GREEN} - Tell travel jokes")
    print(f"{Fore.GREEN} - Provide the weather forecast")
    print(f"{Fore.GREEN} - Viewing local time in cities")
    print(f"{Fore.GREEN} - View news updates")
    print(f"{Fore.CYAN} - Just ask me questions or type 'exit' to leave")

# Function to process user input
def processInput(user_input):
    user_input = user_input.strip().lower()
    user_input = re.sub(r"\s+", " ", user_input) # Replace multiple spaces with a single space
    return user_input

# Function to provide travel recommendations
def provideRecomendations():
    print(f"{Fore.CYAN} Travel Bot: Sure! Are you interested in beaches, mountains or cities?")
    preference = input(f"{Fore.YELLOW} You: ")
    preference = processInput(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(f"{Fore.GREEN} Travel bot: How about visting {suggestions} ")
        print(f"{Fore.CYAN} Travel bot: Do you like this suggestion? (Yes/no)")
        response = input(f"{Fore.YELLOW} You: ").strip().lower()

        if response == "yes":
            print(f"{Fore.GREEN} Travel Bot: Great! Have an amazing time in {suggestions}")
        elif response == "no":
            print(f"{Fore.RED} Travel Bot: No worries! Lets find another place")
            provideRecomendations()
        else:
            print(f"{Fore.RED} Travel Bot: I didn't catch that, let's start over")
            provideRecomendations()

    else:
        print(f"{Fore.RED} Travel Bot: Sorry, I don't have recomendation for that preference")
    
    showHelp()
    
def viewWeatherForecast():
    print(f"{Fore.CYAN} Travel Bot: Sure! Which city would you like the view the forecast for?")
    cityChosen = input(f"{Fore.YELLOW} You: ").strip().lower()
    print(f"{Fore.CYAN} Travel Bot: The weather in {cityChosen} is currently {weather[cityChosen]} degrees celsius")

def viewLocalTime():
    print(f"{Fore.CYAN} Travel Bot: Sure! Which city would you like the view the local time for?")
    cityChosen = input(f"{Fore.YELLOW} You: ").strip().lower()
    print(f"{Fore.CYAN} Travel Bot: The local time in {cityChosen} is currently {localTime[cityChosen]}")

def viewNewsUpdate():
    print(f"{Fore.CYAN} Travel Bot: Sure! Which city would you like the view the news for?")
    cityChosen = input(f"{Fore.YELLOW} You: ").strip().lower()
    print(f"{Fore.CYAN} Travel Bot: The current news in {cityChosen} is: ")
    print(f"{Fore.GREEN} {news[cityChosen]}")

# Function to offer packing tips
def offerPackingTips():
    print(f"{Fore.CYAN} Travel Bot: where are you travelling to?")
    destination = input(f"{Fore.YELLOW} You: ")
    destination = processInput(destination)
    print(f"{Fore.CYAN} Travel Bot: How many days will you be staying? ")
    days = input(f"{Fore.YELLOW} You: ")
    print(f"{Fore.GREEN} Travel Bot: Packing Tips for {days} days in {destination}")
    print(f"{Fore.GREEN} Travel Bot: - Pack personal clothing items")
    print(f"{Fore.GREEN} Travel Bot: - Don't forget travel adapters and chargers")
    print(f"{Fore.GREEN} Travel Bot: - Check the weather forecast before packing")

# Function to tell a joke
def tellAJoke():
    joke = random.choice(jokes)
    print(f"{Fore.YELLOW} Travel Bot: {joke}")

# Main chat function
def chat():
    name = greetUser()
    showHelp()
    while True:
        user_input = input(f"{Fore.YELLOW} {name}: ")
        processedInput = processInput(user_input) 

        recommendationsKeywords = ["recommendation", "suggest", "recommend", "suggestion", "ideas"]
        packingKeywords = ["pack", "packing", "preparing", "prepare"]

        if processedInput in recommendationsKeywords:
            provideRecomendations()
        elif processedInput in packingKeywords:
            offerPackingTips()
        elif "joke" in processedInput or "funny" in processedInput:
            tellAJoke() 
        elif "weather" in processedInput or "forecast" in processedInput:
            viewWeatherForecast()
        elif "time" in processedInput:
            viewLocalTime()
        elif "news" in processedInput or "update" in processedInput:
            viewNewsUpdate()
        elif "help" in processedInput:
            showHelp()
        elif "exit" in processedInput or "bye" in processedInput:
            print(f"{Fore.CYAN} Travel Bot: Safe Travels! Goodbye")
            break 
        else:
            print(f"{Fore.RED} Travel Bot: I'm sorry, I didn't catch that, could you please repeat?")

# Start the chatbot
if __name__ == "__main__":
    chat()
