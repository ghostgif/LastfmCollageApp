Description:
The `fetch_data.py` file is responsible for interfacing with the Last.fm API to fetch the user's top albums based on their listening habits. It retrieves album details, including album names, artist names, play counts, and album artwork URLs, for a specified time period (week, month, 3 months, etc.).

Key Functions:

`fetch_lastfm_top_albums(username, time_range)`
This function fetches the top albums from Last.fm for the given username and time range.

Parameters:
- username: A string representing the Last.fm username.
- time_range: A string representing the time range to filter albums (options: '1week', '1month', '3month', '6month', '12month').

Returns:
A list of dictionaries where each dictionary contains:
- `album_name`: Name of the album.
- `artist_name`: Name of the artist.
- `playcount`: Play count of the album.
- `image_url`: URL of the album cover image.

Usage:
This file is imported by other parts of the project that require album data from Last.fm.

Technologies Used:
- Requests: To make HTTP requests to the Last.fm API.
- JSON: To parse the response data from the API.
