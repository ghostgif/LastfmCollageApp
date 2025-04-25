import requests  # Import the requests library to make HTTP requests

API_KEY = 'e164ca84eeab9a157b0e95cf30c29408'


def fetch_lastfm_top_albums(username, time_range):
    """
    Fetches the top albums from Last.fm for a specific username and time range.
    :param username: The Last.fm username to fetch the top albums for.
    :param time_range: The time range for the top albums (e.g., '1week', '1month', '3month', '6month', '12month').
    :return: A list of dictionaries containing album information or an empty list if no albums are found or if an error occurs.
    """
    if time_range == '1week':  # If the selected time range is '1week', convert it to '7day' for Last.fm's API
        time_range = '7day'

    # Construct the API URL to fetch the top albums for the user and the specified time range
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user={username}&api_key={API_KEY}&period={time_range}&format=json'

    response = requests.get(url)  # Send the GET request to the Last.fm API
    data = response.json()  # Parse the JSON response from the API

    if 'error' in data:  # If there is an error in the response, print the error message and return an empty list
        print(f"Error: {data['message']}")
        return []

    if not data['topalbums'][
        'album']:  # If no albums are returned for the specified time range, print a message and return an empty list
        print(f"No albums found for {time_range} period.")
        return []

    albums = data['topalbums']['album']  # Extract the album data from the API response
    album_list = []  # Initialize an empty list to store album information

    # Iterate through each album in the fetched album data
    for album in albums:
        album_name = album['name']  # Get the album name
        artist_name = album['artist']['name']  # Get the artist name
        playcount = album['playcount']  # Get the play count for the album
        image_url = album['image'][2]['#text']  # Get the medium-sized album artwork image URL

        # Store the album information in a dictionary
        album_info = {
            "album_name": album_name,
            "artist_name": artist_name,
            "playcount": playcount,
            "image_url": image_url
        }
        album_list.append(album_info)  # Add the album information to the list

    return album_list  # Return the list of album information
