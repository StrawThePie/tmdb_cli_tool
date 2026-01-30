import argparse
from .api import fetch_movies

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument(
        "--type",
        choices=["playing", "popular", "top", "upcoming"],
        required=True,
        help="Type of movies to fetch",
    )
    args = parser.parse_args()

    movies = fetch_movies(args.type)
    for movie in movies:
        print(f"{movie['title']} ({movie['release_date']}) - Rating: {movie['vote_average']}")
