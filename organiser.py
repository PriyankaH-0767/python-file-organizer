import os
import shutil

# File categories
images = [".jpg", ".jpeg", ".png"]
documents = [".pdf", ".docx", ".txt"]
videos = [".mp4", ".mkv"]
audio = [".mp3", ".wav"]

folder_path = input("Enter folder path: ")

try:

    for file in os.listdir(folder_path):

        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):

            extension = os.path.splitext(file)[1].lower()

            if extension in images:
                folder_name = "Images"

            elif extension in documents:
                folder_name = "Documents"

            elif extension in videos:
                folder_name = "Videos"

            elif extension in audio:
                folder_name = "Audio"

            else:
                folder_name = "Others"

            target_folder = os.path.join(folder_path, folder_name)

            os.makedirs(target_folder, exist_ok=True)

            destination = os.path.join(target_folder, file)

            shutil.move(full_path, destination)

            with open("log.txt", "a") as log:
                log.write(f"{file} moved to {folder_name}\n")

            print(f"{file} moved to {folder_name}")

    print("\nAll files organized successfully!")

except Exception as e:
    print("Error:", e)