import os

# Define the path to the MP_DATA folder
mp_data_path = "MP_DATA"

# Check if the MP_DATA folder exists
if not os.path.exists(mp_data_path):
    print("Error: MP_DATA folder does not exist.")
    exit()

# Create folders from A to Z
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    folder_path = os.path.join(mp_data_path, letter)
    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{letter}' created successfully.")
    else:
        print(f"Folder '{letter}' already exists.")

print("Folders creation complete.")
