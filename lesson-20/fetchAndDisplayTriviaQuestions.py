
import requests

# Trivia API endpoint
url = "https://opentdb.com/api.php?amount=5&type=multiple" # Fetch 5 questions with multiple choice

# Send Get Request to fetch trivia questions
response = requests.get(url) 

# Check if the request was successful
if response.status_code == 200:
    triviaData = response.json()

    score = 0
    for i, questionData in enumerate(triviaData["results"]):
        print(f"Question {i + 1}: {questionData['question']}")
        option = questionData["incorrect_answers"] + [questionData["correct_answer"]]  
