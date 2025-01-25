
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
        option = sorted(option) # Shuffle the answer options
    
        for j, answer in enumerate(option): 
            print(f"{j + 1}. {answer}") 

        # Collect the user's answer
        userAnswer = input("Your Answer (1/2/3/4): ")

        # Check if the answer is correct
        if option[int(userAnswer) - 1] == questionData["correct_answer"]:
            print("Correct Answer") 
            score += 1 

        else:
            print(f"Wrong Answer, the correct answer was: {questionData['correct_answer']}")  
        
        print()

    print(f"Your final score is: {score} / {len(triviaData['results'])}")

else:
    print("Failed to retrieve trivia questions")

