import pandas as pd
import os
import glob
import random
import shutil
import math


#names_folders_cancer = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

# Giving the biggest folder size
biggest_size = 5364

size_wanted_gone = 4764
size_wanted = 600

#creating the folders to copy the images
current_dir = os.getcwd()
os.chdir("../data/train")
os.mkdir("../copy_directory")
os.mkdir("../trash_images")
copy_directory = "../../copy_directory"

#destination_folder = []
#for dir in os.getcwd():
#    longest_dir_length = max(len(dir))
for folder in os.listdir():
    current_directory = os.getcwd()
    os.chdir(folder)
    images = os.listdir()
    if len(images) == biggest_size:
        number_of_images = len(images)
        print("Current directory: ", folder)
        print('Before resampling: ', number_of_images)
        for c in random.sample(os.listdir(), size_wanted_gone):
            shutil.move(c, "../../trash_images")
        print('After resampling: ', len(os.listdir()))
    else:
        number_of_images = len(images)
        amount_left = number_of_images % size_wanted
        amount_to_multiply = math.floor(size_wanted/number_of_images)
        print("Current directory: ", folder)
        print('Before resampling: ', number_of_images)
        if amount_to_multiply == 0:
            for c in random.sample(os.listdir(), amount_left):
                shutil.move(c, "../../trash_images")
        else:
            for c in os.listdir():
                for x in range(amount_to_multiply):
                    shutil.copy(c, f"{copy_directory}")
                    os.rename(f"{copy_directory}/{c}", f"{c[:-4]}_{x}.jpg")
        print('After resampling: ', len(os.listdir()))
        print("")
    os.chdir(current_directory)

os.rmdir("../copy_directory")
current_dir = os.getcwd()
os.chdir(current_dir)

