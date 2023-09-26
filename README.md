# spotify-playlist-generator
## Overview
This Python script fetches Billboard Hot 100 songs for a chosen date and generates a Spotify playlist with those songs. It's a fun way to relive the music of a particular year or time.
## Code Description
The code is a Python script that performs the following tasks:

1. Web Scraping Billboard Hot 100: It uses the requests library to fetch the Billboard Hot 100 songs for a specified date from the Billboard website. The BeautifulSoup library is then used to extract the song names from the web page.
2. Spotify Integration: The script integrates with the Spotify API using the spotipy library. It uses OAuth 2.0 authentication to access Spotify's features.
3. Playlist Creation: It creates a new Spotify playlist, with the name "Billboard Hot 100" followed by the specified date. This playlist is initially set to private to ensure it's for personal use.
4. Search and Song Addition: For each song retrieved from Billboard Hot 100, the script searches for the song on Spotify, including the year in the search query. If a matching song is found, its Spotify URI is obtained, and the song is added to the newly created playlist.
5. Feedback: If a Billboard Hot 100 song is not found on Spotify, the script provides feedback indicating that the song doesn't exist on Spotify.
6. Confirmation: After processing all the songs, the script confirms the creation of the Spotify playlist and displays the total number of songs added to it.

## What It Does
This code allows users to:

1. Retrieve a historical snapshot of the Billboard Hot 100 chart for a specific date.
2. Create a personalized Spotify playlist containing the Billboard Hot 100 songs for that date.
3. Listen to, enjoy, and share the playlist on Spotify.
4. It's a fun and nostalgic way to relive the music that was trending on a particular day in history, all conveniently organized in a Spotify playlist.
