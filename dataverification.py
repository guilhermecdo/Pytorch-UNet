import os
from PIL import Image

# --- CONFIGURATION ---
# ❗️ Change this to the path of your image dataset
image_dir = '//home/guilherme/Desktop/Coverage-SideBySide/masks'
# ---------------------

corrupted_files = []
# You can add more extensions if needed, e.g., '.jpeg', '.bmp'
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

print(f"Scanning directory: {image_dir}")

for root, _, files in os.walk(image_dir):
    for filename in files:
        if filename.lower().endswith(image_extensions):
            file_path = os.path.join(root, filename)
            try:
                img = Image.open(file_path)
                # The .load() method forces the image data to be read from the file.
                # A simple .open() is lazy and might not catch the error.
                img.load() 
                # You can also add a check for image size if you expect a minimum
                # if img.size[0] < 10 or img.size[1] < 10:
                #    print(f"Image too small: {file_path}")
                #    corrupted_files.append(file_path)
            except (IOError, OSError) as e:
                print(f"🐛 Corrupted file found: {file_path} -> Error: {e}")
                corrupted_files.append(file_path)

print("\n--- Scan Complete ---")
if corrupted_files:
    print("Found the following corrupted files:")
    for f in corrupted_files:
        print(f)
    print("\nPlease remove or replace these files and try training again.")
else:
    print("✅ No corrupted image files were found.")