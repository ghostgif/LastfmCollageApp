def generate_album_list(album_data):
    """
    Generates a list of album information based on the provided album data.
    The information includes the album's name, artist, and play count.

    :param album_data: List of dictionaries containing album information.
                        Each dictionary should have the keys 'album_name', 'artist_name', and 'playcount'.
    :return: List of dictionaries where each dictionary contains album info (album_name, artist_name, playcount).
    """
    album_list = []  # Initialize an empty list to store the formatted album data.

    # Iterate over each album in the album_data list
    for album in album_data:
        # Check that the album has the required keys
        if 'album_name' in album and 'artist_name' in album and 'playcount' in album:
            album_info = {
                "album_name": album['album_name'],
                "artist_name": album['artist_name'],
                "playcount": album['playcount']
            }
            album_list.append(album_info)  # Append the album info to the album list
        else:
            print(f"Invalid album data: {album}")  # Print an error message if the album data is incomplete

    return album_list  # Return the list of formatted album information
