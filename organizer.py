import os
import shutil

# Folder to organize
folder_path = input("Enter folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt"],
    "PDFs": [".pdf"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():

            if extension in extensions:

                destination = os.path.join(folder_path, folder)

                os.makedirs(destination, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination, file)
                )

                print(f"Moved {file} → {folder}")
                break

print("Organization complete!")