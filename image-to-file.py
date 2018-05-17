from PIL import Image
import array
import argparse
from os.path import exists
#import sys

# Set command-line options
parser = argparse.ArgumentParser()
parser.add_argument('-DEC', '--decode', help='Select file to decode.', dest="file_decode")
parser.add_argument('-V', '--verbose', help='Turn verbose mode on/off. Note: Performance may be degraded if this option is used.', dest="verbose", action="store_true", default=False)
parser.add_argument('--overwrite', help='Danger! Overwrite file without any warning!', dest="overwrite", action="store_true", default=False)
parser.add_argument('-O', '--output', help='Set output filename.', dest="output")
args = parser.parse_args()

file = args.file_decode
verbose = args.verbose
overwrite = args.overwrite
output = args.output

# Open image
print("Opening image..")
image = Image.open(file)

# Check if command-line option was used
if (output != None and output != ""):
    original_filename = output
else:
    # Remove '._penc_.png' to get original filename
    original_filename = file.split('._penc_.png')[0]

# Get decimal pixel values and convert it to a bytearray
print("Converting pixels to bytes..")
pixels = bytes(image.getdata())

if verbose: print(pixels) # Show bytes if verbose is set to true

# Save file
print("Saving file as '" + original_filename + "'..")
# Check if file already exists
if (exists(original_filename)):
    if (overwrite): # If command-line option was used
        print("'-O, --overwrite' option was used, overwriting file..")
    else:
        # Ask user to overwrite file
        print("File already exists! Do you want to overwrite it? yes/no")
        while True:
            text = input("> ")
            if (text == "yes"):
                break
            if (text == "no"):
                print("Not going to overwrite file. Exiting..")
                exit()
            else:
                print("File already exists! Do you want to overwrite it? yes/no")

open(original_filename, 'wb').write(pixels)
print("Finished!")
