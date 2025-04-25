import tkinter as tk  # Import Tkinter library for GUI components
from tkinter import messagebox, filedialog, Scrollbar  # Import specific Tkinter components for message boxes, file dialogs, and scrollbars
from fetch_data import fetch_lastfm_top_albums  # Import the function to fetch albums from Last.fm
from generate_collage import create_collage  # Import the function to generate the collage image
from generate_album_info import generate_album_list  # Import the function to generate album information

from PIL import ImageTk  # Import ImageTk for displaying PIL images in Tkinter

class MusicApp:
    """
    A Tkinter-based application to create and display a collage of top albums from a Last.fm user.
    The app allows users to input their Last.fm username, select a time range, fetch their top albums,
    and generate a collage with corresponding album information.

    Attributes and methods...
    """

    def __init__(self, root):
        """
        Initializes the MusicApp with necessary GUI components and settings.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Music Collage")  # Set the window title

        self.root.state('zoomed')  # Maximizes the window

        self.theme = 'light'  # Default theme is light

        # Create and configure the title label
        self.title_label = tk.Label(root, text="Top Albums Collage", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Create and configure the username entry field
        self.username_label = tk.Label(root, text="Enter your Last.fm username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)  # Entry field for the user to input their username
        self.username_entry.pack(pady=5)

        # Create and configure the time range dropdown
        self.time_range_label = tk.Label(root, text="Select Time Range:")
        self.time_range_label.pack()
        self.time_range = tk.StringVar(value="1month")  # Default value is '1month'
        time_ranges = ['1week', '1month', '3month', '6month', '12month']  # List of time range options
        self.time_range_menu = tk.OptionMenu(root, self.time_range, *time_ranges)  # Dropdown menu for time range selection
        self.time_range_menu.pack(pady=5)

        # Create and configure the grid size dropdown
        self.grid_size_label = tk.Label(root, text="Select Grid Size:")
        self.grid_size_label.pack()
        self.grid_size = tk.StringVar(value="3x3")  # Default value is '3x3'
        grid_sizes = ['3x3', '4x4', '5x5']  # List of grid size options
        self.grid_size_menu = tk.OptionMenu(root, self.grid_size, *grid_sizes)  # Dropdown menu for grid size selection
        self.grid_size_menu.pack(pady=5)

        # Create and configure the fetch button
        self.fetch_button = tk.Button(root, text="Fetch Albums", command=self.fetch_data)
        self.fetch_button.pack(pady=10)

        # Create and configure the collage display label
        self.collage_label = tk.Label(root, text="Your Album Collage will appear here!")
        self.collage_label.pack(pady=20)

        # Create and configure the scrollable frame for album information
        self.album_info_frame = tk.Frame(root)
        self.album_info_frame.pack(pady=10)

        self.scrollbar = Scrollbar(self.album_info_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.album_listbox = tk.Listbox(self.album_info_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)  # Listbox for album details
        self.album_listbox.pack(side=tk.LEFT, fill=tk.Y)

        self.scrollbar.config(command=self.album_listbox.yview)  # Link scrollbar to listbox

        # Create and configure the save button for exporting the collage
        self.save_button = tk.Button(root, text="Save Collage", command=self.save_collage)
        self.save_button.pack(pady=10)

        # Create and configure the theme toggle button
        self.theme_button = tk.Button(root, text="Toggle Light/Dark Mode", command=self.toggle_theme)
        self.theme_button.pack(pady=10)

        self.current_collage = None  # To store the generated collage image
        self.album_data = None  # To store album data for later use

    def fetch_data(self):
        """
        Fetches top albums based on the entered username, selected time range, and grid size.
        """
        username = self.username_entry.get()  # Get the username input from the user
        time_range = self.time_range.get()  # Get the selected time range
        grid_size = self.grid_size.get()  # Get the selected grid size

        if not username:  # Ensure the username is provided
            messagebox.showerror("Error", "Please enter your Last.fm username!")
            return

        # Map grid size to the number of albums to display (9, 16, or 25)
        if grid_size == "3x3":
            album_count = 9
        elif grid_size == "4x4":
            album_count = 16
        elif grid_size == "5x5":
            album_count = 25
        else:
            album_count = 9  # Default to 3x3 if something unexpected happens

        # Fetch album data
        try:
            albums_data = fetch_lastfm_top_albums(username, time_range)  # Pass username and time_range here

            if not albums_data:
                messagebox.showinfo("No Data", f"No albums found for the selected {time_range} period.")
                return

            # Limit to the desired number of albums
            albums = [(album['album_name'], album['image_url']) for album in albums_data[:album_count]]

            # Create the collage
            collage = create_collage(albums, grid_size)
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
        collage_image = collage.convert('RGB')  # Convert the collage image to RGB mode
        collage_image_tk = ImageTk.PhotoImage(collage_image)  # Convert to Tkinter-compatible image
        self.collage_label.config(image=collage_image_tk)  # Update the collage display label with the new image
        self.collage_label.image = collage_image_tk  # Keep a reference to avoid garbage collection

    def display_album_info(self, album_list):
        """
        Displays the album information in the listbox.
        :param album_list: List of dictionaries containing album information (album_name, artist_name, playcount).
        :return: None
        """
        self.album_listbox.delete(0, tk.END)  # Clear the current listbox

        for index, album in enumerate(album_list, start=1):
            album_info = f"{index}. {album['album_name']} - {album['artist_name']} - {album['playcount']} plays"
            self.album_listbox.insert(tk.END, album_info)  # Insert album information into the listbox

    def save_collage(self):
        """
        Saves the generated collage image to the user's file system.
        :return: None
        """
        if self.current_collage:  # Check if the collage has been created
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

            if file_path:
                self.current_collage.save(file_path)  # Save the collage to the file
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
        self.root.config(bg="black")  # Set the background to black
        for widget in self.root.winfo_children():  # Loop through all widgets in the window
            widget.config(bg="black", fg="white")  # Set widget background to black and text to white

    def apply_light_mode(self):
        self.root.config(bg="white")  # Set the background to white
        for widget in self.root.winfo_children():  # Loop through all widgets in the window
            widget.config(bg="white", fg="black")  # Set widget background to white and text to black


# Main program to start the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()  # Create the Tkinter window
    app = MusicApp(root)  # Initialize the MusicApp class
    root.mainloop()  # Start the Tkinter event loop
