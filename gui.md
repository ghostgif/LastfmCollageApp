Description:
The gui.py file is responsible for creating the graphical user interface (GUI) for the Album Collage Generator. Using Tkinter, it allows users to input their Last.fm username, select a time range, and view their generated album collage. The GUI also provides the option to download the collage and toggle between light and dark modes.
Key Features:
-	User Input: Users enter their Last.fm username and select a time range (e.g., "1week", "1month", "3month").
-	Album Information: Displays a list of the top albums fetched from Last.fm with album name, artist, and play count.
-	Collage Display: Displays the album collage with album artwork in a grid format (3x3, 4x4, or 5x5).
-	Save Collage: Users can save the generated collage as an image file.
-	Theme Toggle: A button to switch between light and dark modes for the interface.
Key Functions:
fetch_data(self)
This function fetches the user's top albums based on the Last.fm username and time range, generates a collage, and displays both the collage and album information.
display_collage(self, collage)
This function is used to display the generated collage in the GUI.
display_album_info(self, album_list)
This function displays the formatted album information in a scrollable list box within the GUI.
save_collage(self)
This function allows the user to save the generated collage as an image.
toggle_theme(self)
This function toggles between light and dark themes in the GUI.
Technologies Used:
-	Tkinter: For creating the GUI, including buttons, labels, list boxes, and scrollbars.
-	Pillow (PIL): For displaying and resizing images in the GUI.
-	Requests: To fetch data and images from Last.fm.
