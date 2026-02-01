import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

TYPE_TO_ENDPOINT = {
    "playing": "movie/now_playing",
    "popular": "movie/popular",
    "top": "movie/top_rated",
    "upcoming": "movie/upcoming",
}

def fetch_movies(movie_type: str):
    if not API_KEY:
        raise RuntimeError("TMDB_API_KEY is missing. Set it in your .env file.")

    endpoint = TYPE_TO_ENDPOINT[movie_type]
    url = f"{BASE_URL}/{endpoint}"
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])
