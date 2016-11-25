from PIL import Image
import os, pprint

old_directory = 'old'
new_directory = 'new'

new_origin = (36, 32)

for file in os.listdir(old_directory):
    filename = "{}/{}".format(old_directory, file)
    img = Image.open(filename)
    width = img.size[0]
    height = img.size[1]
    if height != 1040:
        print(file)
        continue
    cropped_img = img.crop(
        (
            new_origin[0],
            new_origin[1],
            675 + new_origin[0],
            976 + new_origin[1],
        )
    )
    save_location = "{}/{}".format(new_directory, file)
    cropped_img.save(save_location)
