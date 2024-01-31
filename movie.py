import requests

def search_movies(movie_query):
    api_key = "d4412c62"  # Got my API key from http://www.omdbapi.com/apikey.aspx, used the FREE! (1,000 daily limit) and recieved the email with my key.
                          # Verified my email address and replaced the api_key value with the key i obtained. 
    base_url = "http://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "s": movie_query,
    }

    response = requests.get(base_url, params = params)
    data = response.json()

    if data["Response"] == "True":
        return data["Search"]
    else:
        print("Error:", data["Error"])
        return []

def get_movie_details(movie_id):
    api_key = "d4412c62"
    base_url = "http://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "i": movie_id,
    }

    response = requests.get(base_url, params = params)
    return response.json()

def display_movie_list(movies):
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['Title']} ({movie['Year']})")

def main():
    print("Welcome to the Movie App!")
    movie_query = input("Enter a movie title: ")

    movies = search_movies(movie_query)

    if movies:
        display_movie_list(movies)

        movie_choice = int(input("Select a movie (enter the number): "))
        selected_movie = movies[movie_choice - 1]

        movie_details = get_movie_details(selected_movie["imdbID"])

        print("\nMovie Details: ")
        for key, value in movie_details.items():
            print(f"{key}: {value}")
    else:
        print("No movies found.")

if __name__ == "__main__":
    main()