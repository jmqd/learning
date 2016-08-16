from PIL import Image
import os, pprint, StringIO

def crop(img_buffer, new_origin, width, height, expected_height):
    img = Image.open(StringIO.StringIO(img_buffer))
    img_width = img.size[0]
    img_height = img.size[1]
    if img_height != expected_height:
        return False
    cropped_img = img.crop(
        (
            new_origin[0],
            new_origin[1],
            width + new_origin[0],
            height + new_origin[1],
        )
    return cropped_img
