import os, re, argparse
from shutil import copyfile

#argument parsing :::
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination", type=str, default='new/')
parser.add_argument("-s", "--source", type=str, default='old/')
args = parser.parse_args()

#regular expression object building :::
regex = re.compile('[^a-zA-Z\-]') #looking at complement of any alphabetical character, or a hyphen

def slug(string):
    string = string.strip()
    string = string.replace(" ", "-").lower() #attention: data entry error might cause two spaces between words
    string = regex.sub('', string)
    string = re.sub(r"([-]){2,}", "-", string) #solve for that here: remove case of two adjacent hyphens
    return string

for file in os.listdir(args.source):
    if file.endswith(".jpg"):
        src = args.source + file
        dest = args.destination + slug(os.path.splitext(file)[0]) + ".jpg" #splitext: splits name & ext
        copyfile(src, dest)
