import os
import re

# Specify the directory containing the files you want to rename
directory = 'docs/tk_apps/files/landmark_images'

# Function to replace non-alphabetic characters with spaces
# def rename_files(directory):
#     for filename in os.listdir(directory):
#         # Create a new filename by replacing non-alphabetic characters with spaces
#         new_filename = re.sub(r'[^a-zA-Z]', ' ', filename)
#         # Construct the full file paths
#         old_filepath = os.path.join(directory, filename)
#         new_filepath = os.path.join(directory, new_filename)
#         # Rename the file
#         os.rename(old_filepath, new_filepath)
#         print(f'Renamed: {old_filepath} -> {new_filepath}')

# # Call the function
# rename_files(directory)


# Function to rename files
def rename_files(directory):
    for filename in os.listdir(directory):
        # Create a new filename by replacing non-alphabetic characters with spaces
        new_filename = re.sub(r'[^a-zA-Z\'\.\-]', ' ', filename)
        # Replace multiple spaces with a single space
        new_filename = re.sub(r'\s+', ' ', new_filename).strip()
        # Replace extension
        new_filename = new_filename.replace(' jpg', '.jpg')
        new_filename = new_filename.replace(' jpeg', '.jpg')
        new_filename = new_filename.replace(' .jpg', '.jpg')

        # Construct the full file paths
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {old_filepath} -> {new_filepath}')

# Call the function
rename_files(directory)
