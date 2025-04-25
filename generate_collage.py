import os  # Import os for file system operations
from PIL import Image, ImageDraw, ImageFont  # Import PIL for image manipulation
import requests  # Import requests for fetching album images
from io import BytesIO  # For working with byte data for images

def create_collage(albums, grid_size):
    """
    Generates a collage based on grid size: 3x3, 4x4, or 5x5.
    :param albums: List of tuples (album_name, album_image_url) for albums to be used in the collage.
    :param grid_size: The grid size, either '3x3', '4x4', or '5x5'.
    :return: The collage image object
    """
    # Determine grid size based on user selection
    if grid_size == "3x3":
        grid_width, grid_height = 3, 3  # 3x3 grid (3 columns, 3 rows)
    elif grid_size == "4x4":
        grid_width, grid_height = 4, 4  # 4x4 grid (4 columns, 4 rows)
    elif grid_size == "5x5":
        grid_width, grid_height = 5, 5  # 5x5 grid (5 columns, 5 rows)
    else:
        grid_width, grid_height = 3, 3  # Default to 3x3 if the grid size is unknown

    images = []  # List to store album images
    for album_name, img_url in albums:
        try:
            if img_url:  # If the album has a valid image URL
                response = requests.get(img_url)  # Fetch the image from the URL
                img = Image.open(BytesIO(response.content))  # Open the image from the response content
                img = img.resize((150, 150))  # Resize each image for the grid
                images.append(img)  # Add the resized image to the images list
            else:  # If no image URL is provided
                blank_img = Image.new('RGB', (150, 150), color=(255, 255, 255))  # Placeholder image
                images.append(blank_img)
        except Exception as e:
            print(f"Error loading image for {album_name}: {e}")  # If an error occurs, print it
            blank_img = Image.new('RGB', (150, 150), color=(255, 255, 255))  # Placeholder image on error
            images.append(blank_img)

    collage_width = grid_width * 150  # Calculate total width based on the grid size
    collage_height = grid_height * 150  # Calculate total height based on the grid size
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))  # Create a blank canvas for the collage

    x_offset, y_offset = 0, 0  # Position variables for pasting images
    for i, img in enumerate(images):
        collage.paste(img, (x_offset, y_offset))  # Paste the image at the current position
        x_offset += 150  # Move to the next column
        if (i + 1) % grid_width == 0:  # After the last column, move to the next row
            x_offset = 0  # Reset the x position to start of the row
            y_offset += 150  # Move down to the next row

    return collage  # Return the collage image object
