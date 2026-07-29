import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't already exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    moved_count = 0

    # Go through every file in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\nDone! Moved {moved_count} .jpg file(s) to {destination_folder}")


if __name__ == "__main__":
    # Change these paths to match folders on your own computer
    source_folder = "source_images"
    destination_folder = "jpg_backup"

    move_jpg_files(source_folder, destination_folder