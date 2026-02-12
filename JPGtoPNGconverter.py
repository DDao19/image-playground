from PIL import Image
from pathlib import Path
import sys

user_params = sys.argv[1::]
parent_folder = Path(user_params[0])
new_folder = Path(user_params[1])

# Grab all image files
image_files = list(Path(f"{parent_folder}").glob("*.jpg"))

# Create sub folder in Pokedex called New
sub_folder = Path(f"{parent_folder}/{new_folder}")


try:
    if parent_folder.exists():
        sub_folder.mkdir(exist_ok=True)

        for image in image_files:
            image_file = Image.open(f"{parent_folder}/{image.name}")

            new_filename = image.stem + ".png"
            save_path = sub_folder / new_filename

            image_file.save(save_path)
    else:
        print("Sorry, that Parent directory does not exist")
except Exception as err:
    print(f"Something went wrong {err}")
