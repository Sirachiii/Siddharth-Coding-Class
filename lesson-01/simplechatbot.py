
print("Hello, I am chatbot")
name = input("What is your name? ")
print("Nice to meet you", name)
userFeeling = input("How are you feeling today? ")
userFeeling = userFeeling.lower()

if "good" in userFeeling or "great" in userFeeling or "better" in userFeeling:
    print("I'm glad to hear that")
else:
    print("I hope your day gets better")
