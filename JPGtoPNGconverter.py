import sys
import os
from PIL import Image

# grab the sourse and destination folder names from the terminal command
image_folder = f'{sys.argv[1]}/'
output_folder = f'{sys.argv[2]}/'


# check if the output folder already exist. if it doesn't exist, create a new one
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop over the images
# convert to png format and apply black and white filter
# save them to the output folder
for filename in os.listdir(image_folder):
    # .DS_Store is a hiden system file that may exist in the folder and cause an issue
    # below if statement prevent the program from including .DS_Store in the loop
    if not filename.startswith('.'):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        grayed_img = img.convert('L')
        grayed_img .save(f'{output_folder}{clean_name}.png', 'png')
        print('all done')
