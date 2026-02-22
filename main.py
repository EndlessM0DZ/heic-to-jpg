import os
from pillow_heif import register_heif_opener
from PIL import Image
import shutil
register_heif_opener()

def convert_all_heic():
    while True:
        selected_folder = input("Please enter your folder you'd like to transfer to jpg from heic!")
        transfer_jpgs = input("Would you like to transfer jpgs automatically as well? (y/n)")
        is_transfer_jpgs = False
        if transfer_jpgs == "y" or transfer_jpgs == "Y" or transfer_jpgs == "yes" or transfer_jpgs == "YES":
            is_transfer_jpgs = True
        destination_folder = None
        if (os.path.exists(selected_folder)):
            for x in range(10000):
                destination_folder = os.path.join(selected_folder, "output")
                if x == 0:
                    pass
                else:
                    destination_folder += str(x)
                if (os.path.exists(destination_folder)):
                    continue
                else:
                    os.mkdir(destination_folder)
                    break
        else:
            continue

        for x, filename in enumerate(os.listdir(selected_folder)):
            if filename.lower().endswith(".heic"):
                heic_path = os.path.join(selected_folder, filename)
                jpg_path = os.path.join(destination_folder, filename[:-5] + ".jpg")

                img = Image.open(heic_path)
                img.save(jpg_path, "JPEG", quality=95)

                print(f"Converted: {filename} -> {jpg_path}")
            elif is_transfer_jpgs and (filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg")):
                selected_folder_file = os.path.join(selected_folder, filename)
                destination_folder_file = os.path.join(destination_folder, filename)
                shutil.copy(selected_folder_file, destination_folder_file)
            if x == len(os.listdir(selected_folder)) - 1:
                print("Success!")
        


if __name__ == "__main__":
    convert_all_heic()
