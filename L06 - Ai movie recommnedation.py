import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import random

# Initialize colorama
init(autoreset=True)

# Load and preprocess the dataset
def load_data():
    try:
        df = pd.read_csv(r"C:\Users\demon\Desktop\Siddharth Coding Class\imdb_top_1000.csv")
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file 'imdb_top_1000.csv' was not found.")
        exit()

movies_df = load_data()

# Vectorize the combined features and compute cosine similarity
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies_df["combined_features"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List all unique genres
def listGenres(df):
    return sorted(set(genre.strip() for subList in df["Genre"].dropna().str.split(", ") for genre in subList))

genres = listGenres(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def recommnedMovies(genre=None, mood=None, rating=None, top_number=5):
    filterDf = movies_df
    
    if genre:
        filterDf = filterDf[filterDf["Genre"].str.contains(genre, case=False, na=False)]
    if rating:
        filterDf = filterDf[filterDf["IMDB_Rating"] >= rating] 

    # Randomise the order
    filterDf = filterDf.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for idx, row in filterDf.iterrows():
        overview = row["Overview"] 
        if pd.isna(overview):
            continue 

        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row["Series_Title"], polarity))

        if len(recommendations) == top_number: 
            break
    
    return recommendations if recommendations else "No suitable movie recommendation found."

# Display recommendations
def displayRecommendation(recs, username):
    print(f"{Fore.YELLOW} Ai analyzed movie recommendation for {username}")
    for idx, (title, Polarity) in enumerate(recs, 1):
        sentiment = "positive" if Polarity > 0 else "negative" if Polarity < 0 else "neutral"
        print(f"{Fore.CYAN} {title} polarity = {Polarity}, {sentiment}")

# Small processing animation
def processingAnimation():
    for _ in range(3): 
        print(f"{Fore.YELLOW} .", end="", flush=True)
        time.sleep(0.5)

# Recommend a random movie
def randomMovie(name):
    random_row = movies_df.sample(1).iloc[0]
    print(f"{Fore.GREEN} Random Movie Recommendation: {random_row['Series_Title']} ({random_row['IMDB_Rating']}/10)")
    print(f"{Fore.CYAN} Genre: {random_row['Genre']}")
    print(f"{Fore.CYAN} Overview: {random_row['Overview']}")

    # Option for more
    while True:
        option = input(f"{Fore.BLUE} Would you like another recommendation? (yes/no): ").strip().lower()
        if option == "yes":
            randomMovie()
        elif option == "no":
            print()
            handleAi(name)
            break

# Handle AI recommendation flow
def handleAi(name):
    print(f"{Fore.BLUE} Let's find the perfect movie for you! \n")

    # Show genres
    print(f"{Fore.GREEN} Available Genres: ", end="")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN} {idx} {genre}")
    print()

    # Option for random movie
    while True:
        choice = input(f"{Fore.YELLOW} Would you like a random movie recommendation? (yes/no): ").strip().lower()
        if choice == 'yes':
            randomMovie(name)
            return
        elif choice == 'no':
            break
        else:
            print(f"{Fore.RED} Invalid input, please try again.")

    while True:
        genreInput = input(f"{Fore.YELLOW} Enter a genre number or name: ").strip() 
        if genreInput.isdigit() and 1 <= int(genreInput) <= len(genres):
            genre = genres[int(genreInput) - 1] 
            break
        elif genreInput.title() in genres: 
            genre = genreInput.title()
            break
        
        print(f"{Fore.RED} Invalid input, please try again")
    
    mood = input(f"{Fore.YELLOW} How do you feel today? (Describe your mood): ").strip()
    
    print(f"{Fore.BLUE} \n Analyzing mood", end="", flush=True)
    processingAnimation()
    polarity = TextBlob(mood).sentiment.polarity
    moodDescription = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    print(f"{Fore.GREEN} Your mood is {moodDescription}, polarity = {round(polarity, 2)}")

    while True:
        ratingInput = input(f"{Fore.YELLOW} Enter minimum imdb rating (7.6 - 9.3) or 'skip': ").strip()
        if ratingInput.lower() == "skip":
            rating = None
            break
        try:
            rating = float(ratingInput)
            if 7.6 <= rating <= 9.3:
                break
            print(f"{Fore.RED} Rating is out of range! Try again.")
        except ValueError:
            print(f"{Fore.RED} Invalid input, please try again.")

    print(f"{Fore.BLUE} Finding movies for {name}", end="", flush=True)
    processingAnimation()

    recs = recommnedMovies(genre=genre, mood=mood, rating=rating, top_number=5)
    if isinstance(recs, str): 
        print(f"{Fore.RED} {recs} \n")
    else:
        displayRecommendation(recs, name)

    while True:
        action = input(f"{Fore.YELLOW} \n Would you like more recommendations (Yes/no): ").strip().lower()
        if action == "no":
            print(f"{Fore.GREEN} Enjoy your movie picks {name}! ")
            break
        elif action == "yes":
            recs = recommnedMovies(genre=genre, mood=mood, rating=rating, top_number=5)
            if isinstance(recs, str):
                print(f"{Fore.RED} {recs} \n")
            else:
                displayRecommendation(recs, name)
        else:
            print(f"{Fore.RED} Invalid choice, you need to try again")

# Main program
def main():
    print(f"{Fore.BLUE} Welcome to your personal movie recommendation assistant!")
    print()
    name = input(f"{Fore.YELLOW} What is your name? ").strip()
    print(f"{Fore.GREEN} \n Nice to meet you {name}")
    print()
    handleAi(name)

if __name__ == "__main__":
    main()
