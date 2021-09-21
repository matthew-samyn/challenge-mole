import pandas as pd
import os
import glob
import random
import shutil


#names_folders_cancer = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
# TODO change test amount: it is a percentage

os.chdir("../data/train")

#destination_folder = []
for dir in os.getcwd():
    longest_dir_length = max(len(dir))
    for folder in os.listdir():
        current_directory = os.getcwd()
        os.chdir(folder)
        images = os.listdir()
        if len(images) > 5000:
            print(os.getcwd())
            print('before resampling: ', len(images))
            for c in random.sample(os.listdir(), (len(images) / 2)):
                shutil.move(c, os.chdir('../../trash_images'))
            print('before after resampling: ', len(images))
        if len(images) < 150:
            print(os.getcwd())
            print('before resampling: ', len(images))
            for c in random.sample(os.listdir(), test_amount):
                shutil.copy(c, os.getcwd())
            print('before after resampling: ', len(images))
        elif 300 < len(images) < 600:
            print(os.getcwd())
            print('before resampling: ', len(images))
            for c in random.sample(os.listdir(), test_amount):
                shutil.copy(c, os.getcwd())
            print('before after resampling: ', len(images))
        elif 1000 < len(images) < 1200:
            print(os.getcwd())
            print('before resampling: ', len(images))
            pass
        os.chdir(current_directory)
current_dir = os.getcwd()
os.chdir(current_dir)