import os, re
from shutil import copyfile


prev = "prev/"
new = "new/"
regex = re.compile('[^a-zA-Z\-]') #looking at complement of any alphabetical character, or a hyphen

def slug(string):
    string = string.strip()
    string = string.replace(" ", "-").lower() #attention: data entry error might cause two spaces between words
    string = regex.sub('', string)
    string = re.sub(r"([-]){2,}", "-", string) #solve for that here: remove case of two adjacent hyphens
    return string

for file in os.listdir(prev):
    if file.endswith(".jpg"):
        src = prev + file
        dest = new + slug(os.path.splitext(file)[0]) + ".jpg" #splitext -> list of 0:name, 1:extension
        copyfile(src, dest)
