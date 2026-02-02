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

    try:
        movies = fetch_movies(args.type)
    except Exception as e:
        print(f"Error: {e}")
        return

    for movie in movies[:10]:
        title = movie.get("title", "Unknown title")
        release_date = movie.get("release_date", "Unknown date")
        rating = movie.get("vote_average", "N/A")
        print(f"{title} ({release_date}) - Rating: {rating}")

def print_movies(movies):
    if not movies:
        print("No movies found.")
        return

    print("-" * 80)
    for i, movie in enumerate(movies[:10], start=1):
        title = movie.get("title", "Unknown title")
        release_date = movie.get("release_date", "Unknown date")
        rating = movie.get("vote_average", "N/A")
        overview = movie.get("overview", "").strip()

        print(f"{i}. {title} ({release_date}) - Rating: {rating}")
        if overview:
            print(f"   {overview[:120]}{'...' if len(overview) > 120 else ''}")
        print("-" * 80)
