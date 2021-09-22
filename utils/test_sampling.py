import pandas as pd
import os
import glob
import random
import shutil


#names_folders_cancer = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
# TODO change test amount: it is a percentage

#understanding the folders size
dictionary_size_folders = {'akiec': 262, 'bcc': 411, 'bkl': 879, 'df': 92, 'mel': 890, 'nv': 5364, 'vasc': 114}


#creating the folders to copy the images

current_dir = os.getcwd()

os.chdir("../train")
os.mkdir('../copes')
folder_to_copy = "../copies"

# Create test and validate folders, containing label folders
for main_folder in folders_to_create:
    os.mkdir(main_folder)
    os.chdir(main_folder)
    for label_folder in list(labels.keys()):
        os.mkdir(label_folder)
    os.chdir("..")



os.chdir("../data/train")

#destination_folder = []
#for dir in os.getcwd():
#    longest_dir_length = max(len(dir))
for folder in os.listdir():
    current_directory = os.getcwd()
    os.chdir(folder)
    images = os.listdir()
    print(len(images))
    if len(images) > 5000:
        print('before resampling: ', len(images))
        for c in random.sample(os.listdir(), (len(images) / 3)):
            shutil.move(c, os.chdir('../../trash_images'))
        print('before after resampling: ', len(images))
    if len(images) < 150:
        print('before resampling: ', len(images))
        for c in os.listdir():
            for x in range(10):
                old_file = os.path.join(os.getcwd(), c)
                new_file = os.path.join(os.getcwd(), f"{c}_{x}")
                os.rename(old_file, new_file)
        print('before after resampling: ', len(images))
    elif 150 < len(images) < 600:
        print('before resampling: ', len(images))
        for c in os.listdir():
            for x in range(4):
                old_file = os.path.join(os.getcwd(), c)
                new_file = os.path.join(os.getcwd(), f"{c}_{x}")
                os.rename(old_file, new_file)
        print('before after resampling: ', len(images))
    elif 600 < len(images) < 1200:
        print('before resampling: ', len(images))
        for c in os.listdir():
            for x in range(2):
                old_file = os.path.join(os.getcwd(), c)
                new_file = os.path.join(os.getcwd(), f"{c}_{x}")
                os.rename(old_file, new_file)
    os.chdir(current_directory)

current_dir = os.getcwd()
os.chdir(current_dir)

