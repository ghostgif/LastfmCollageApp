Description:
The `gui.py` file is responsible for creating the graphical user interface (GUI) for the Album Collage Generator. Using Tkinter, it allows users to input their Last.fm username, select a time range, and view their generated album collage. The GUI also provides the option to download the collage and toggle between light and dark modes.

Key Features:
- User Input: Users enter their Last.fm username and select a time range (e.g., "1week", "1month", "3month").
- Album Information: Displays a list of the top albums fetched from Last.fm with album name, artist, and play count.
- Collage Display: Displays the album collage with album artwork in a grid format (3x3, 4x4, or 5x5).
- Save Collage: Users can save the generated collage as an image file.
- Theme Toggle: A button to switch between light and dark modes for the interface.

Key Functions:

`fetch_data(self)`
This function fetches the user's top albums based on the Last.fm username and time range, generates a collage, and displays both the collage and album information.

Parameters:
- `self`: The Tkinter window instance.

Responsibilities:
- Collects the user's Last.fm username and the selected time range.
- Maps the grid size selection to determine the number of albums to display (9, 16, or 25).
- Calls `fetch_lastfm_top_albums` to get the top albums from Last.fm.
- Creates a collage of album artwork using `create_collage`.
- Filters the album data used in the collage and passes it to `generate_album_list`.
- Displays the collage and album information in the GUI.

---

`display_collage(self, collage)`
This function is used to display the generated collage in the GUI.

Parameters:
- `collage`: The collage image object that will be displayed in the GUI.

Responsibilities:
- Converts the collage image to a Tkinter-compatible format using `ImageTk.PhotoImage`.
- Updates the `collage_label` widget to display the generated collage.

---

`display_album_info(self, album_list)`
This function displays the formatted album information in a scrollable list box within the GUI.

Parameters:
- `album_list`: A list of dictionaries containing album details (album_name, artist_name, playcount).

Responsibilities:
- Clears any existing album information in the list box.
- Loops through the `album_list` and inserts each album's details into the list box.
- Each entry displays the album's name, artist, and play count.

---

`save_collage(self)`
This function allows the user to save the generated collage as an image.

Responsibilities:
- Prompts the user with a file dialog to select where to save the collage.
- Saves the collage to the selected location in `.png` format using `filedialog.asksaveasfilename`.

---

`toggle_theme(self)`
This function toggles between light and dark themes in the GUI.

Responsibilities:
- Switches the theme from light to dark or vice versa by updating the background and foreground colors of the root window and all widgets.

---

Technologies Used:
- Tkinter: For creating the GUI, including buttons, labels, list boxes, and scrollbars.
- Pillow (PIL): For displaying and resizing images in the GUI.
- Requests: To fetch data and images from Last.fm.
