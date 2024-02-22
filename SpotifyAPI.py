import os
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Make sure to install the packages


def process_audio_files(directory_path):
    """
    Process audio files in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing audio files.
    """
    processed_songs = []

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            if file_name.endswith(".mp3"):
                process_mp3(file_path, processed_songs)
            elif file_name.endswith(".flac"):
                process_flac(file_path, processed_songs)
            elif file_name.endswith(".m4a"):
                process_m4a(file_path, processed_songs)


def process_mp3(file_path, processed_songs):
    """
    Extract details from MP3 files.

    Parameters:
    - file_path (str): The path to the MP3 file.
    - processed_songs (list): A list to store processed song names.
    """
    try:
        audio = MP3(file_path)
        artist = audio.get("TPE1")
        title = audio.get("TIT2")

        if artist is not None and title is not None:
            print("File: {}".format(file_path))
            print("Artist: {}".format(artist))
            print("Title: {}".format(title))

            formatted_song_name = format_song_name(artist, title)
            processed_songs.append(formatted_song_name)

            delete_file(file_path)
            print("-------------------")

    except Exception as e:
        print("Error processing {}: {}".format(file_path, str(e)))

def process_flac(file_path, processed_songs):
    """
    Extract details from FLAC files.

    Parameters:
    - file_path (str): The path to the FLAC file.
    - processed_songs (list): A list to store processed song names.
    """
    try:
        audio = FLAC(file_path)
        artist = audio.get("artist")
        title = audio.get("title")

        if artist is not None and title is not None:
            print("File: {}".format(file_path))
            print("Artist: {}".format(artist))
            print("Title: {}".format(title))

            formatted_song_name = format_song_name(artist, title)
            processed_songs.append(formatted_song_name)

            delete_file(file_path)
            print("-------------------")

    except Exception as e:
        print("Error processing {}: {}".format(file_path, str(e)))


def process_m4a(file_path, processed_songs):
    """
    Extract details from M4A files.

    Parameters:
    - file_path (str): The path to the M4A file.
    - processed_songs (list): A list to store processed song names.
    """
    try:
        audio = MP4(file_path)
        artist = audio.get("\xa9ART")
        title = audio.get("\xa9nam")

        if artist is not None and title is not None:
            print("File: {}".format(file_path))
            print("Artist: {}".format(artist))
            print("Title: {}".format(title))

            formatted_song_name = format_song_name(artist, title)
            processed_songs.append(formatted_song_name)

            delete_file(file_path)
            print("-------------------")

    except Exception as e:
        print("Error processing {}: {}".format(file_path, str(e)))


def format_song_name(artist, title):
    """
    Format the song name.

    Parameters:
    - artist (str): The artist name.
    - title (str): The song title.

    Returns:
    - formatted_song_name (str): The formatted song name.
    """
    artist_name = " ".join(artist) if artist else ""
    title_name = " ".join(title) if title else ""
    formatted_song_name = f"{title_name} {artist_name}"
    return formatted_song_name


def delete_file(file_path):
    """
    Delete a file.

    Parameters:
    - file_path (str): The path to the file to be deleted.
    """
    try:
        os.remove(file_path)
        print("Deleted file: {}".format(file_path))
    except Exception as e:
        print("Error deleting {}: {}".format(file_path, str(e)))


def search_and_add_to_playlist(sp, playlist_id, processed_songs, not_found_songs):
    """
    Search for songs on Spotify and add them to a playlist.

    Parameters:
    - sp (Spotipy): The Spotipy Spotify API object.
    - playlist_id (str): The ID of the playlist to add songs to.
    - processed_songs (list): A list of processed song names.
    - not_found_songs (list): A list to store songs not found on Spotify.
    """
    for song in processed_songs:
        results = sp.search(q=song, type='track')

        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            sp.playlist_add_items(playlist_id=playlist_id, items=[track_id])
            print(f'Track added to your playlist successfully. {song}')
        else:
            print(f'No search results found. {song}')
            not_found_songs.append(song)


def main():
    directory_path = "your directory"  # For example: "D:\\FileName"
    processed_songs = []
    not_found_songs = []

    process_audio_files(directory_path)

    print()
    print(processed_songs)

    with open("all-processed_songs.txt", "w", encoding="utf-8") as all_processed_songs_file:
        for song in processed_songs:
            all_processed_songs_file.write(song + "\n")

    print()

    client_id = 'your client_id'  # For example: 'c27187h982937ha346wdi35h'
    client_secret = 'your client_secret'  # For example: '24527187h982937ha346di35'
    redirect_uri = 'your redirect_uri'  # For example: 'http://localhost:8000/callback'
    scope = 'playlist-modify-public'  # Could be different for each purposes

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                   redirect_uri=redirect_uri, scope=scope))

    playlist_id = 'your playlist_id'  # For example: '2V187F982G937HA346K35'

    search_and_add_to_playlist(sp, playlist_id, processed_songs, not_found_songs)

    print(not_found_songs)

    with open("notfound.txt", "w", encoding="utf-8") as notfound_file:
        for song in not_found_songs:
            notfound_file.write(song + "\n")


if __name__ == "__main__":
    main()
