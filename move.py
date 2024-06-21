import os
import shutil
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <source_directory> <destination_directory>")
    sys.exit(1)

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and f.lower().endswith(image_extensions)]

num_files = len(images)

# Ask user if they want to move half of the images
user_input = input(f"Do you want to move: \n\t{num_files} images \nfrom: \n\t{source_dir} \nto \n\t{dest_dir}? \n(Yes/no): ")

if user_input.lower() in ["", "y", "yes"]:
    for file in images:
        shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
    print(f"Moved {num_files} images.")
else:
    print("Operation cancelled.")
