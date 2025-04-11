Description:
The generate_collage.py file handles the creation of album collages. Using Pillow (PIL), it generates a 3x3 collage by default (though it supports different grid sizes like 4x4 and 5x5) using the album artwork URLs fetched from Last.fm.
Key Functions:
create_collage(albums)
This function generates a collage from the album artwork URLs by resizing and arranging the images in a grid format.
Parameters:
-	albums: A list of tuples, where each tuple contains:
  -	album_name: The name of the album.
  -	image_url: The URL of the album artwork.
Returns:
-	A PIL.Image object representing the generated collage.
Usage:
This file is used to create a visual representation of the user's most played albums and displays them as a collage.
Technologies Used:
-	Pillow (PIL): For handling image processing (resizing and arranging images).
-	Requests: To download the album artwork images.
-	BytesIO: For reading image data directly from HTTP responses.
Collage Grid Options:
-	The collage can be customized to display different grid sizes, such as 3x3, 4x4, or 5x5, based on the user's preference.
