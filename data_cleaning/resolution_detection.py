import os
import cv2
import shutil
from imutils import paths
import argparse

def move_small_images(src_directory, dst_directory, min_width, min_height):
    # Ensure the destination directory exists
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    # Loop over the input images
    for imagePath in paths.list_images(src_directory):
        # Load the image
        image = cv2.imread(imagePath)
        if image is None:
            print(f"Warning: Couldn't read image {imagePath}")
            continue

        # Get image dimensions
        height, width = image.shape[:2]

        # Check if the image is smaller than the minimum size
        if width < min_width or height < min_height:
            print(f"Moving {imagePath} (size: {width}x{height}) to {dst_directory}")
            shutil.move(imagePath, os.path.join(dst_directory, os.path.basename(imagePath)))

if __name__ == "__main__":
    # Construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", required=True, help="Path to input directory of images")
    ap.add_argument("-d", "--destination", required=True, help="Path to destination directory for small images")
    ap.add_argument("-w", "--width", type=int, required=True, help="Minimum width of images to keep")
    ap.add_argument("-e", "--height", type=int, required=True, help="Minimum height of images to keep")
    args = vars(ap.parse_args())

    # Move small images
    move_small_images(args["images"], args["destination"], args["width"], args["height"])
