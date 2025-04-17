import os
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def create_collage(albums):
    """
    Generates a 3x3 collage of the top albums.
    :param albums: List of tuples (album_name, album_image_url)
    :return: The collage image object
    """
    # Ensure we have exactly 9 images for a 3x3 grid
    while len(albums) < 9:
        albums.append(("Empty", None))  # Use None as a placeholder for albums without images

    images = []  # List to store album images
    for album_name, img_url in albums:
        try:
            # Fetch the image from the URL if img_url is not None
            if img_url:
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))  # Open the image from the response content
                img = img.resize((150, 150))  # Resize each image to 150x150 for the grid
                images.append(img)  # Add the resized image to the images list
            else:
                # Create a placeholder image if no URL is provided
                blank_img = Image.new('RGB', (150, 150), color=(255, 255, 255))  # White background for placeholder
                images.append(blank_img)
        except Exception as e:
            print(f"Failed to load image for {album_name}: {e}")
            # In case of an error, add a blank image as a placeholder
            blank_img = Image.new('RGB', (150, 150), color=(255, 255, 255))  # White background for placeholder
            images.append(blank_img)

    # Now we have 9 images, create a 3x3 grid
    collage_width = 3 * 150  # 3 images wide (150px each)
    collage_height = 3 * 150  # 3 images tall (150px each)

    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))  # White background for collage

    # Positioning variables for pasting images into the collage
    x_offset = 0
    y_offset = 0
    for i, img in enumerate(images):
        collage.paste(img, (x_offset, y_offset))  # Paste the image at the current position
        x_offset += 150  # Move to the next column
        if (i + 1) % 3 == 0:  # After every 3 images, move to the next row
            x_offset = 0  # Reset x position to the start of the row
            y_offset += 150  # Move down to the next row

    return collage  # Return the collage image object
