
# Name
print("Hello, I am chatbot")
name = input("What is your name? ")
print("Nice to meet you", name)
print("")

# Feelings
feeling = input("How are you feeling today? ")
feeling = feeling.lower()

if "good" in feeling or "great" in feeling or "better" in feeling:
    print("I'm glad to hear that")
else:
    print("I hope your day gets better")
print("")

# Age
age = int(input("How old are you? "))
if age > 20:
    print("So you are an adult.")
elif age <= 20:  
    print("Wow, you are very young.")
print("")

# Height 
height = int(input("How tall are you? "))
if height >= 175:
    print("Wow, you're quite tall")
elif height > 160 and height < 175:
    print("You are average height")
else:
    print("Oh, you are short")
print("")

# Hobbies 
hobby = input("What do you like to do in your free time? ")
print("Nice,", hobby, "sounds like alot of fun")
print("")

# Favourite Food
food = input("What is your favourite food? ")
food = food.lower()

hotFoods = ['pizza', 'noodles', 'burgers']
coldFoods = ['ice-cream', 'yogurt', 'milkshakes'] 

if food in hotFoods:
    print("Oh wow, I love some hot", food, "on a cold day")
elif food in coldFoods:
    print("Oh wow, I love some cold", food, "on a hot day")
print("")

# Favourite Season
season = input("What is your favourite season? ")
season = season.lower()

if season == "summer":
    print("I love summer! Nothing beats having fun in the warm sun")

elif season == "winter":
    print("Winter is great, I just love staying inside with my blankets")

elif season == "autumn":
    print("Autumn is so beautiful with all the colorful leaves falling from the trees.")

elif season == "spring":
    print("Spring is amazing! The flowers bloom, and everything feels fresh and new.") 

