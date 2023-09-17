import os
import re
import shutil

# Define the directory containing the .wav files. **MAKE SURE YOU USE REPLACE THE SINGLE BACK SLASHES "\" WITH DOUBLE FORWARD SLASHES "//"**
wav_files_directory = r"C://Program Files (x86)//Steam//steamapps//common//H3EK//data//your_directory_to_your_.wav_files"

# Function to extract characters before the bracket from a .wav filename
def extract_name(filename):
    match = re.search(r'^(.*?)\[\w+\]', filename)
    if match:
        return match.group(1)
    return None

# Dictionary to keep track of created folder names
created_folders = {}

# Iterate through the .wav files in the directory
for root, _, files in os.walk(wav_files_directory):
    for filename in files:
        if filename.lower().endswith(".wav"):
            wav_path = os.path.join(root, filename)
            name = extract_name(filename)
            if name and len(name) > 0:  # Check if a name was extracted
                if name not in created_folders:
                    # Create a folder with the extracted name if it doesn't exist
                    folder_path = os.path.join(root, name)
                    os.makedirs(folder_path, exist_ok=True)
                    created_folders[name] = folder_path
                # Move the .wav file to the corresponding folder
                destination_folder = created_folders[name]
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(wav_path, destination_path)
                print(f"Moved: {filename} -> {destination_path}")
            else:
                print(f"Skipping: {filename} (Invalid name or no name found. . . Dumbass)")

print("Folder creation and file movement completed. Yeah baby.")
