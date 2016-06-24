import os, re, argparse, sys
from PIL import Image
from shutil import copy

#argument parsing :::
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", type=str, default='images/')
args = parser.parse_args()

location = "/var/www/jmorris/ck-gocart/cardkingdom.com/public/media/__init__website_images/eternal-masters"

for file in os.listdir(args.directory):
    if file.endswith(".png") or file.endswith(".jpg"):
        name = os.path.splitext(file)[0]
        im = Image.open(args.directory + '/' + file)
        try:
            im.load()
        except:
            print("Problem!", file)
            sys.exit(0)
        im.save(args.directory + '/' + name + ".jpg")
