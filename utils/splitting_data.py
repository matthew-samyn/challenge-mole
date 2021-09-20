import pandas as pd
import os
import glob
import random
import shutil

df = pd.read_csv("../data/HAM10000_metadata.csv")
df_cancer_type = df[["image_id","dx"]]

malignous = {4:"mel", 0:"akiec"}
benign = {5:"nv", 3:"df", 2:"bkl", 1:"bcc", 6:"vasc"}
labels = {"akiec":0, "bcc":1, "bkl":2, "df":3, "mel":4, "nv":5, "vasc":6}
folders_to_create = ["test", "validate"]
folders_containing_images = ["HAM10000_images_part_1", "HAM10000_images_part_2"]

current_dir = os.getcwd()

os.chdir("../data")

# Create test and validate folders, containing label folders
for main_folder in folders_to_create:
    os.mkdir(main_folder)
    os.chdir(main_folder)
    for label_folder in list(labels.keys()):
        os.mkdir(label_folder)
    os.chdir("..")

# Moves file from part 2 into _part_1
os.chdir("../data/HAM10000_images_part_2")
for file in os.listdir():
    shutil.move(file,"../HAM10000_images_part_1")

# Creates label folders in _part_1
os.chdir("../HAM10000_images_part_1")
for label_folder in list(labels.keys()):
    os.mkdir(label_folder)

# Changes image names, containing the label name and moves them to a subfolder.
for i, row in df_cancer_type.iterrows():
    image_name = f"{row['image_id']}.jpg"
    label = row["dx"]
    new_name_image = f"{row['image_id']}_{label}.jpg"
    os.rename(image_name, new_name_image)
    shutil.move(new_name_image, label)

# Moves .2 images into a test directory.
for label in (labels.keys()):
    os.chdir(f"{label}")
    number_of_pictures = len(os.listdir())
    test_amount = round(number_of_pictures*0.2)
    for c in random.sample(os.listdir(),test_amount):
        shutil.move(c, f"../../test/{label}")
    os.chdir("..")

# Renames _part_1 into train, removes _part_2
os.chdir(current_dir)
os.chdir("../data")
os.rename("HAM10000_images_part_1","train")
os.rmdir("HAM10000_images_part_2")
os.chdir(current_dir)