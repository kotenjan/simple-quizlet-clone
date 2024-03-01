import argparse
from PIL import Image
import os
import cv2
import numpy as np

class ImageMerger:
    def __init__(self, dir_path, orientation='horizontal'):
        self.dir_path = dir_path
        self.orientation = orientation

    def merge_last_two_png_files(self):
        png_files = sorted([file for file in os.listdir(self.dir_path) if file.endswith('.png')])
        last_two_png_files = png_files[-2:]

        images = [Image.open(os.path.join(self.dir_path, png)) for png in last_two_png_files]
        
        if self.orientation == 'vertical':
            self.merge_images_vertically(images, last_two_png_files)
        elif self.orientation == 'horizontal':
            self.merge_images_horizontally(images, last_two_png_files)

    def merge_images_vertically(self, images, last_two_png_files):
        max_width = max(image.size[0] for image in images)
        scaled_images = [image.resize((max_width, int(max_width / image.width * image.height)), Image.Resampling.LANCZOS) for image in images]
        total_height = sum(image.size[1] for image in scaled_images)
        new_image = Image.new('RGB', (max_width, total_height))

        current_height = 0
        for image in scaled_images:
            new_image.paste(image, (0, current_height))
            current_height += image.size[1]

        if self.show_image(new_image):
            print(f"{self.orientation} merging")
            self.save_and_cleanup(new_image, last_two_png_files)

    def merge_images_horizontally(self, images, last_two_png_files):
        max_height = max(image.size[1] for image in images)
        scaled_images = [image.resize((int(max_height / image.height * image.width), max_height), Image.Resampling.LANCZOS) for image in images]
        total_width = sum(image.size[0] for image in scaled_images)
        new_image = Image.new('RGB', (total_width, max_height))

        current_width = 0
        for image in scaled_images:
            new_image.paste(image, (current_width, 0))
            current_width += image.size[0]

        if self.show_image(new_image):
            print("MERGING")
            self.save_and_cleanup(new_image, last_two_png_files)

    def save_and_cleanup(self, new_image, last_two_png_files):
        new_image_path = os.path.join(self.dir_path, last_two_png_files[0])
        new_image.save(new_image_path)
        os.remove(os.path.join(self.dir_path, last_two_png_files[1]))

    def show_image(self, image):
        np_image = np.array(image)
        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
        cv2.namedWindow("Image Browser", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Image Browser", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Image Browser", np_image)

        proceed = True
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q') or key == 27:  # Quit on 'q' or ESC
            proceed = False

        cv2.destroyAllWindows()
        return proceed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge the last two PNG images in a directory either vertically or horizontally.')
    parser.add_argument('--orientation', type=str, required=True, choices=['v', 'h'], help='Choose v for vertical merge or h for horizontal merge.')

    args = parser.parse_args()

    orientation = 'vertical' if args.orientation == 'v' else 'horizontal'

    # Replace the path below with the directory path where your PNG files are located.
    dir_path = "/mnt/c/Users/jan/Pictures/Screenshots"
    merger = ImageMerger(dir_path, orientation)
    merger.merge_last_two_png_files()