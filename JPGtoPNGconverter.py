from posix import listdir
import sys
import os
from PIL import Image, ImageFilter

# grab the first and second arguments
source_folder = sys.argv[1]
dest_folder = sys.argv[2]

# check if the new folder exist  and create if not
new_dir = dest_folder
parent_dir = '/Users/mohaimenmacbookpro/Dev/_ZTM_Course/Projects/image_converter/'
new_dir_path = os.path.join(parent_dir, new_dir)

if os.path.exists(dest_folder):
    print('folder exists')
else:
    os.mkdir(new_dir_path)
# loop though the folder


for file in os.listdir(source_folder):
    if not file.startswith('.'):
        print(f'source folder:: {source_folder}')
        print(f'destination folder:: {dest_folder}')
        filename = os.fsdecode(file)
        print(filename)
        img = Image.open(parent_dir + source_folder + '/' + filename)
        grayed_img = img.convert('L')
        grayed_img.save(
            f'{parent_dir}{dest_folder}/{filename}.png', 'png')
    else:
        continue

print('testing GitHub updates')