# Run this script when the unwished JPG files are removed from this library.
# Then all corresponding DNG files to the removed JPG will be listed and
# moved to a subdirectory './remove'.
#
# This script needs to be placed in the same directory as the DNG files are.

import os

# Create the directory ./remove if not exist
path = "remove"
if not os.path.exists(path):
    os.mkdir(path)

for f_name_dng in os.listdir("."):
    if f_name_dng.endswith('.DNG'):
        pos = -1
        for f_name_jpg in os.listdir("."):
            pos +=1
            if f_name_jpg.endswith('.JPG'):
                if ((os.path.splitext(f_name_jpg))[0] == (os.path.splitext(f_name_dng))[0]):
                    #print(f_name_dng,"och",f_name_jpg, "existerar")
                    break
            if pos == len(os.listdir("."))-1:
                print("Motsvarande JPG fil till", f_name_dng,"existerar inte")
                os.rename('./'+f_name_dng, './remove/'+f_name_dng)