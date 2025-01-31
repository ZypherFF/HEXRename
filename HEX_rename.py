from PIL import Image
import os

def get_visible_color(image_path):
    with Image.open(image_path) as img:
        # Convert the image to RGBA (if it is not in that format)
        img = img.convert("RGBA")

        # Get all pixel data
        pixel_data = list(img.getdata())

        # Filters out transparent pixels
        visible_pixels = [pixel for pixel in pixel_data if pixel[3] > 0]

        # If there are no visible pixels, returns None
        if not visible_pixels:
            return None

        # Gets the color of the first visible pixel
        color = visible_pixels[0][:3]

        # Convert color to hexadecimal
        hex_color = "#{:02x}{:02x}{:02x}".format(*color)

        return hex_color

def rename_images(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Checks if the file is a PNG image
        if os.path.isfile(file_path) and filename.lower().endswith('.png'):
            color = get_visible_color(file_path)

            # If there are visible pixels, rename the file
            if color:
                new_filename = os.path.join(folder_path, f"{color}.png")

                # If the file already exists, add a counter to the name
                counter = 1
                while os.path.exists(new_filename):
                    new_filename = os.path.join(folder_path, f"{color}_{counter}.png")
                    counter += 1

                # Rename the file
                os.rename(file_path, new_filename)
                print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    folder_path = r"PATH"  # Change to your folder path
    rename_images(folder_path)
