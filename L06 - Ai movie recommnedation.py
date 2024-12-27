
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time

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
tfidf_matrix = tfidf.fit_transform(movies_df["combine_feature"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List all unique genres
def listGenres(df):
    return sorted(set(genre.strip() for subList in df["Genre"].dropna().str.split(", ") for genre in subList))

genres = listGenres(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def recommnedMovies(genre=None, mood=None, rating=None, top_number=5):
    filterDf = movies_df
    
    if genre:
        filterDf = filterDf[filterDf["Genre"].str.contains(genres, case=False, na=False)]
    if rating:
        filterDf = filterDf[filterDf["IMDB_Rating"] >= rating] 

    # Randomise the order
    filterDf = filterDf.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for idx, row in filterDf.iterrow:
        overview = row["Overview"] 
        if pd.isna(overview):
            continue 

        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row["Series_Title"], polarity))

        if len(recommendations) == top_number: 
            break
    
    return recommendations if recommendations else "No suitable movie recommendation found."

# Display recommendations🍿 😊  😞  🎥
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

# Handle AI recommendation flow 🔍
def handleAi(name):
    print(f"{Fore.BLUE} Let's find the perfect movie for you! \n")

    # Show genres in a sinle line
    print(f"{Fore.GREEN} Available Genres: ", end="")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN} {idx} {genre}")
    print()

    while True:
        genreInput = input(f"{Fore.YELLOW} Enter a genre number or name: ").strip() 
        if genreInput.isdigit() and 1 <= int(genreInput) <= genres:
            genre = genres[int(genreInput) - 1] 
            break
        elif genreInput.title() in genres:
            genre = genreInput.title()
            break
        
        print(f"{Fore.RED} Invalid input, please try again")

    # Processing animation while analyzing mood 😊  😞  😐
    
    # Processing animation while finding movies
    
      # Small processing animation while finding movies 🎬🍿

   
# Main program 🎥
