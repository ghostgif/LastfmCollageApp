import requests

API_KEY = 'e164ca84eeab9a157b0e95cf30c29408'  # Replace with your actual API key


def fetch_lastfm_top_albums(username, time_range):
    """
    Fetches the top albums from Last.fm for a specific username and time range.

    This function makes a request to the Last.fm API to fetch the user's top albums for a given time range.
    It returns the list of albums containing album name, artist name, playcount, and the album artwork URL.

    :param username: The Last.fm username to fetch the top albums for.
    :param time_range: The time range for the top albums (e.g., '1week', '1month', '3month', '6month', '12month').
    :return: A list of dictionaries containing album information or an empty list if no albums are found or if an error occurs.

    Example:
        fetch_lastfm_top_albums('ghostgif', '1month')

    Returns:
        [
            {
                "album_name": "Stop Making Sense (Deluxe Edition) [Live]",
                "artist_name": "Talking Heads",
                "playcount": "236",
                "image_url": "https://lastfm.freetls.fastly.net/i/u/174s/585d09deb82a5547a1bfebf5ab86e4fb.jpg"
            },
            ...
        ]
    """
    # Map '1week' to '7day' for the API request
    if time_range == '1week':
        time_range = '7day'

    # API URL for fetching the top albums based on the time range
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user={username}&api_key={API_KEY}&period={time_range}&format=json'

    response = requests.get(url)
    data = response.json()

    # Check if there's an error in the API response
    if 'error' in data:
        print(f"Error: {data['message']}")
        return []

    # If no albums data is returned
    if not data['topalbums']['album']:
        print(f"No albums found for {time_range} period. Please check your listening history.")
        return []

    albums = data['topalbums']['album']
    album_list = []  # Create a list to store the fetched albums
    for album in albums:
        album_name = album['name']
        artist_name = album['artist']['name']
        playcount = album['playcount']
        image_url = album['image'][2]['#text']  # Get the medium-sized album artwork

        album_info = {
            "album_name": album_name,
            "artist_name": artist_name,
            "playcount": playcount,
            "image_url": image_url
        }
        album_list.append(album_info)

    return album_list  # Return the list of albums
