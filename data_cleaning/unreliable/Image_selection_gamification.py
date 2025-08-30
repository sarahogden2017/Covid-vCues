import os
import shutil
from PIL import Image
import pytesseract

# --- CONFIG ---
input_folder = "/Users/shreetikapoudel/Documents/GitHub/Covid-vCues/data_cleaning/final/unreliable"
output_folder = "unreliable_gamification"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# If tesseract is not in PATH, set its path manually (example below for Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Skip if not an image
    if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")):
        continue

    try:
        # Open image
        img = Image.open(file_path)

        # Extract text using OCR
        text = pytesseract.image_to_string(img)

        # Check if 'covid' is in extracted text
        if "covid" in text.lower():
            # Copy image to output folder
            shutil.copy(file_path, os.path.join(output_folder, filename))
            print(f"✅ Saved: {filename}")
        else:
            print(f"❌ Skipped: {filename}")

    except Exception as e:
        print(f"⚠️ Error processing {filename}: {e}")

print("Finished processing all images.")
