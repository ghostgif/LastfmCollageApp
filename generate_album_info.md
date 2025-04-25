Description:
The `generate_album_info.py` file processes album data fetched from Last.fm to create a formatted list of albums for display. It is designed to handle the album information in a simple format, ready for the GUI to display to the user.

Key Functions:

`generate_album_list(album_data)`
This function processes the raw album data and prepares it in a formatted list, making it ready for display.

Parameters:
- album_data: A list of dictionaries containing album details fetched from Last.fm.

Returns:
A list of dictionaries with `album_name`, `artist_name`, and `playcount` for each album.

Usage:
This file is used to format the album data in the appropriate structure for the GUI to display.

Technologies Used:
- Python Lists and Dictionaries: For organizing and formatting album data.
- Error Handling: To ensure data integrity (only albums with the required fields are included).
