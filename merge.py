from PIL import Image, ImageOps
import os

# Directory containing the PNG files
dir_path = '/mnt/c/Users/jan/Pictures/Screenshots'

# Get all PNG files in the directory, sorted alphabetically
png_files = sorted([file for file in os.listdir(dir_path) if file.endswith('.png')])

# Select the last two PNG files
last_two_png_files = png_files[-2:]

# Load the images
images = [Image.open(os.path.join(dir_path, png)) for png in last_two_png_files]

# Determine the maximum width
max_width = max(image.size[0] for image in images)

# Reshape the images to have the same width, keeping their proportions
scaled_images = []
for image in images:
    aspect_ratio = image.width / image.height
    new_height = int(max_width / aspect_ratio)
    scaled_image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
    scaled_images.append(scaled_image)

# Determine the total height of the scaled images
total_height = sum(image.size[1] for image in scaled_images)

# Create a new image with the appropriate size for the scaled images
new_image = Image.new('RGB', (max_width, total_height))

# Paste the scaled images into the new image
current_height = 0
for image in scaled_images:
    new_image.paste(image, (0, current_height))
    current_height += image.size[1]

# Save the new image with the name of the first of the two
new_image.save(os.path.join(dir_path, last_two_png_files[0]))
os.remove(os.path.join(dir_path, last_two_png_files[1]))

