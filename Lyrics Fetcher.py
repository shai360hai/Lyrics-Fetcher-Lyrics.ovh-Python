import requests

def get_lyrics_from_lyricsovh(artist, song_name):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song_name}"
    try:
        response = requests.get(url, timeout=15) 
        if response.status_code == 200:
            return response.json().get("lyrics", "Lyrics not found.")
        else:
            return "Lyrics not found or an error occurred."
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

print("Hello, welcome to 'Lyrics Fetcher'.")
artist = input("Enter the name of the artist: ")
song_name = input("Enter the song name: ")

lyrics = get_lyrics_from_lyricsovh(artist, song_name)

if "Lyrics not found" in lyrics:
    print("\nSorry, we couldn't find the lyrics. Please check the artist and song name.")
elif "Request timed out" in lyrics or "An error occurred" in lyrics:
    print(f"\n{lyrics}")
else:
    print("\nLyrics:\n")
    print(lyrics)
