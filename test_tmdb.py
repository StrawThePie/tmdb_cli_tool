import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    raise SystemExit("TMDB_API_KEY is missing from .env")

url = "https://api.themoviedb.org/3/movie/popular"
params = {"api_key": api_key, "language": "en-US", "page": 1}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()

for movie in data.get("results", [])[:5]:
    print(movie["title"])
