# SpotifyAPI
# Audio Metadata Processor and Spotify Playlist Updater

This Python script processes audio files, extracts metadata, and updates a Spotify playlist based on the extracted information.

## Features

- **Audio File Processing:**
  - Supports MP3, FLAC, and M4A file formats.
  - Extracts artist and title information from audio files.

- **Spotify Integration:**
  - Searches for songs on Spotify using extracted metadata.
  - Adds found tracks to a specified Spotify playlist.

## Requirements

- Python 3.x
- Install required Python packages by running: `pip install -r requirements.txt`

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/erfanshafagh/SpotifyAPI.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain your Spotify API credentials:
   - Visit the Spotify Developer Dashboard website.
   - Create a new application to get your `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.
   - You should set other variables such as `DIRECTORY_PATH` and `PLAYLIST_ID`.

4. Run the script:

    ```bash
    python SpotifyAPI.py
    ```

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an [issue](https://github.com/erfanshafagh/SpotifyAPI/issues) or create a [pull request](https://github.com/erfanshafagh/SpotifyAPI/pulls).


