# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (dotenv)
load_dotenv()

# Retrieve Spotify API credentials from environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
client_uri = os.getenv("client_uri")

# URL for the Billboard Hot 100 chart
link = "https://www.billboard.com/charts/hot-100"

# Prompt the user for the date they want to fetch
date = input("What year you would like to travel to (in YYYY-MM-DD format)?: ")

# Send an HTTP GET request to fetch the Billboard Hot 100 page and parse it with BeautifulSoup
response = requests.get(f"{link}/{date}").text
soup = BeautifulSoup(response, "html.parser")

# Extract song names from the page using CSS selectors
songs = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in songs]

# Initialize the Spotify API client with OAuth authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=client_uri,
    scope="playlist-modify-private"  # Set the desired scope for playlist modification
))

# Create a new Spotify playlist with the Billboard Hot 100 songs for the specified date
playlist_name = f"Billboard Hot 100 {date}"
user_id = sp.me()['id']  # Get the user's Spotify ID
playlist = sp.user_playlist_create(user_id, playlist_name, public=False)  # Adjust public/private as needed

# Extract the year from the input date
year = date.split("-")[0]

# Search for each Billboard Hot 100 song on Spotify and add it to the playlist
for song_name in song_names:
    # Search for the song on Spotify, including the year to narrow down results
    result = sp.search(q=f"track:{song_name} year:{year}", type="track")
    try:
        track_uri = result['tracks']['items'][0]['uri']  # Get the URI of the first search result
        sp.playlist_add_items(playlist['id'], [track_uri])  # Add the track to the playlist
    except IndexError:
        print(f"Track '{song_name}' for the year {year} doesn't exist on Spotify. Skipped")

# Print a confirmation message with the number of songs added to the playlist
print(f"Playlist '{playlist_name}' created with {len(song_names)} songs.")