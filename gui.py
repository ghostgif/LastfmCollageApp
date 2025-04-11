import tkinter as tk
from tkinter import messagebox, filedialog, Scrollbar
from fetch_data import fetch_lastfm_top_albums  # Import the function from fetch_data.py
from generate_collage import create_collage  # Import the updated create_collage function
from generate_album_info import generate_album_list  # Import the new function to generate album list

from PIL import ImageTk  # Import ImageTk for displaying the PIL image in Tkinter


class MusicApp:
    """
    A Tkinter-based application to create and display a collage of top albums from a Last.fm user.
    The app allows users to input their Last.fm username, select a time range, fetch their top albums,
    and generate a collage with corresponding album information.

    Attributes:
        root: The root Tkinter window.
        theme: The current theme of the application ('light' or 'dark').
        title_label: The label for the title of the app.
        username_label: The label for the username input field.
        username_entry: The entry field for the username.
        time_range_label: The label for the time range dropdown menu.
        time_range: The time range selected by the user.
        time_range_menu: The dropdown menu for selecting the time range.
        fetch_button: The button to trigger the data fetching process.
        collage_label: The label where the collage image will be displayed.
        album_info_frame: The frame that contains the album information.
        album_listbox: The listbox widget displaying album details.
        scrollbar: The scrollbar for the album information listbox.
        save_button: The button to save the generated collage image.
        theme_button: The button to toggle between light and dark mode.
        current_collage: The generated collage image.
        album_data: The data of the fetched albums.

    Methods:
        __init__: Initializes the MusicApp with necessary GUI components and settings.
        fetch_data: Fetches top albums based on the entered username and selected time range.
        display_collage: Displays the generated collage image in the app.
        display_album_info: Displays the album information in the listbox.
        save_collage: Saves the generated collage image to the user's file system.
        toggle_theme: Toggles between light and dark mode.
        apply_dark_mode: Applies dark mode to the app.
        apply_light_mode: Applies light mode to the app.
    """

    def __init__(self, root):
        """
        Initializes the MusicApp with necessary GUI components and settings.

        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Music Collage")

        # Set the window to windowed fullscreen (maximize the window)
        self.root.state('zoomed')  # This maximizes the window but still keeps it windowed.

        self.theme = 'light'  # Default theme

        # Title
        self.title_label = tk.Label(root, text="Top Albums Collage", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Username entry
        self.username_label = tk.Label(root, text="Enter your Last.fm username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Time range dropdown
        self.time_range_label = tk.Label(root, text="Select Time Range:")
        self.time_range_label.pack()
        self.time_range = tk.StringVar(value="1month")
        time_ranges = ['1week', '1month', '3month', '6month', '12month']
        self.time_range_menu = tk.OptionMenu(root, self.time_range, *time_ranges)
        self.time_range_menu.pack(pady=5)

        # Fetch button
        self.fetch_button = tk.Button(root, text="Fetch Albums", command=self.fetch_data)
        self.fetch_button.pack(pady=10)

        # Collage display
        self.collage_label = tk.Label(root, text="Your Album Collage will appear here!")
        self.collage_label.pack(pady=20)

        # Scrollable frame for album information
        self.album_info_frame = tk.Frame(root)
        self.album_info_frame.pack(pady=10)

        self.scrollbar = Scrollbar(self.album_info_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.album_listbox = tk.Listbox(self.album_info_frame, height=15, width=80,
                                        yscrollcommand=self.scrollbar.set)  # Increased width to fit full info
        self.album_listbox.pack(side=tk.LEFT, fill=tk.Y)

        self.scrollbar.config(command=self.album_listbox.yview)

        # Save button for exporting the collage
        self.save_button = tk.Button(root, text="Save Collage", command=self.save_collage)
        self.save_button.pack(pady=10)

        # Light/Dark mode toggle button
        self.theme_button = tk.Button(root, text="Toggle Light/Dark Mode", command=self.toggle_theme)
        self.theme_button.pack(pady=10)

        self.current_collage = None  # To store the generated collage image
        self.album_data = None  # To store album data for later use

    def fetch_data(self):
        """
        Fetches top albums based on the entered username and selected time range.

        This function is called when the 'Fetch Albums' button is clicked. It requests the top albums from
        Last.fm using the user's username and the selected time range. If successful, it generates and displays
        a collage of the albums and their corresponding information.

        :return: None
        """
        username = self.username_entry.get()
        time_range = self.time_range.get()

        if not username:
            messagebox.showerror("Error", "Please enter your Last.fm username!")
            return

        # Pass the entered username and selected time range to fetch the top albums
        try:
            albums_data = fetch_lastfm_top_albums(username, time_range)  # Pass username and time_range here

            if not albums_data:
                messagebox.showinfo("No Data", f"No albums found for the selected {time_range} period.")
                return

            # Convert the data into a list of tuples (album_name, image_url)
            albums = [(album['album_name'], album['image_url']) for album in albums_data[:9]]  # Only take top 9 albums

            # Create the collage
            collage = create_collage(albums)
            self.current_collage = collage  # Store the collage to be saved later
            self.display_collage(collage)

            # Filter the albums that were used in the collage
            collage_album_data = [album for album in albums_data if
                                  album['album_name'] in [album[0] for album in albums]]

            # Generate and display album info
            album_list = generate_album_list(collage_album_data)
            self.display_album_info(album_list)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")

    def display_collage(self, collage):
        """
        Displays the generated collage image in the GUI.

        :param collage: The generated collage image.
        :return: None
        """
        # Convert the PIL image to a Tkinter-compatible image
        collage_image = collage.convert('RGB')
        collage_image_tk = ImageTk.PhotoImage(collage_image)

        # Display the collage in the GUI
        self.collage_label.config(image=collage_image_tk)
        self.collage_label.image = collage_image_tk  # Keep a reference to avoid garbage collection

    def display_album_info(self, album_list):
        """
        Displays the album information in the listbox.

        :param album_list: List of dictionaries containing album information (album_name, artist_name, playcount).
        :return: None
        """
        self.album_listbox.delete(0, tk.END)  # Clear the current listbox

        for index, album in enumerate(album_list, start=1):
            # Format album information as: Album Title - Artist - Plays plays
            album_info = f"{index}. {album['album_name']} - {album['artist_name']} - {album['playcount']} plays"
            self.album_listbox.insert(tk.END, album_info)

    def save_collage(self):
        """
        Saves the generated collage image to the user's file system.

        :return: None
        """
        if self.current_collage:
            # Prompt the user for a file destination to save the image
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

            if file_path:
                # Save the collage to the specified path
                self.current_collage.save(file_path)
                messagebox.showinfo("Success", f"Collage saved successfully to {file_path}")
        else:
            messagebox.showerror("Error", "No collage to save. Please fetch albums first.")

    def toggle_theme(self):
        """
        Toggles between light and dark mode.

        :return: None
        """
        if self.theme == 'dark':
            self.theme = 'light'
            self.apply_light_mode()
        else:
            self.theme = 'dark'
            self.apply_dark_mode()

    def apply_dark_mode(self):
        """
        Applies the dark theme to the app.

        :return: None
        """
        self.root.config(bg="black")
        for widget in self.root.winfo_children():
            widget.config(bg="black", fg="white")

    def apply_light_mode(self):
        """
        Applies the light theme to the app.

        :return: None
        """
        self.root.config(bg="white")
        for widget in self.root.winfo_children():
            widget.config(bg="white", fg="black")


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()
