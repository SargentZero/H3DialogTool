import os
import re
import shutil

# Define the directory containing the .wav files.
wav_files_directory = input("Paste your directory here:  ")

wav_files_directory = wav_files_directory.replace("\\", "//")

# Function to extract characters before the bracket from a .wav filename
def extract_name(filename):
    match = re.search(r'^(.*?)\[\w+\]', filename)
    if match:
        return match.group(1)
    return None

# Function to extract characters within the brackets from a .wav filename
def extract_characters_in_brackets(filename):
    match = re.search(r'\[(\w+)\]', filename)
    if match:
        return match.group(1)
    return None

# Function to create an empty .txt file with the sound permutation name as the filename
def create_empty_txt_file(folder, final_name):
    txt_filename = f"{final_name}.txt"
    txt_path = os.path.join(folder, txt_filename)
    open(txt_path, 'w').close()

# Dictionary to keep track of created folder names
created_folders = {}

# Iterate through the .wav files in the directory
for root, _, files in os.walk(wav_files_directory):
    for filename in files:
        if filename.lower().endswith(".wav"):
            wav_path = os.path.join(root, filename)
            name = extract_name(filename)
            characters_in_brackets = extract_characters_in_brackets(filename)
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

                # Rename the .wav file to characters within brackets
                if characters_in_brackets:
                    new_filename = f"{characters_in_brackets}.wav"
                    new_wav_path = os.path.join(destination_folder, new_filename)
                    os.rename(destination_path, new_wav_path)
                    print(f"Renamed: {filename} -> {new_filename}")

                # Create an empty .txt file with the sound permutation name as the filename
                create_empty_txt_file(destination_folder, characters_in_brackets)
                print(f"Created: {characters_in_brackets}.txt")
            else:
                print(f"Skipping: {filename} (Invalid name or no name found. . . Fucking Dumbass)")

print("Folder creation, file movement, renaming, and empty .txt file creation completed. Oh yeaaaaaaaa >:)")
