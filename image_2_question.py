import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <>")
    else:
        current_dir = sys.argv[1]

        # List all PNG files in the current directory
        png_files = [file for file in os.listdir(current_dir) if file.endswith('.png')]

        # Create and open q.txt for writing
        with open(f'{current_dir}/q.txt', 'w') as txt_file:
            # Write image names to q.txt in the specified format
            for png_file in png_files:
                image_name = os.path.splitext(png_file)[0]
                txt_file.write(f"{image_name};{png_file}\n")

        print("q.txt has been created with image names.")