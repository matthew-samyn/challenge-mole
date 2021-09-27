import itertools
from typing import List
import numpy as np
import os
import re
from typing import Tuple
import matplotlib.pyplot as plt
import cv2
#from model import *


def get_score(h5_file:str) -> Tuple[float, float]:
    """ Extracts useful data from a .h5 file

    :param h5_file: File to extract the train and val accuracy scores from
    :return: train accuracy, difference between train and validation
    """
    scores = re.findall(r"\d+\.\d+",h5_file)
    train_accuracy = float(scores[0])
    val_accuracy = float(scores[1])
    difference = train_accuracy - val_accuracy
    return val_accuracy, difference



def keep_best_saved_h5(folder_relative:str, common_filename: str, maximum_difference:float) -> str:
    """ Goes through all common named .h5-files,
    deletes all from folder except for the best result.

    :param maximum_difference: max difference allowed between accuracy and val_accuracy.
    :return Best scoring .h5 file
    """
    current_directory = os.getcwd()
    os.chdir(current_directory + folder_relative)
    all_files = os.listdir()
    best_scoring_file = ""
    # try-except incase of errors: returns to current directory
    try:
        # Keep the files with a low difference between train_accuracy and validation_accuracy.
        # Deletes the rest from directory
        model_files = [file for file in all_files if file.startswith(common_filename)]
        scores = []
        not_overfitting_models = []
        best_scoring_file = ""
        for file in model_files:
            validation_accuracy, diff = get_score(file) # Uses function get_score()
            if abs(diff) > maximum_difference:
                os.remove(file)
            else:
                not_overfitting_models.append(file)
                scores.append(validation_accuracy)

        # Keep only the file with highest validation accuracy score.
        # Deletes the rest from directory
        highest_score_index = scores.index(max(scores))
        for i, file in enumerate(not_overfitting_models):
            if i == highest_score_index:
                best_scoring_file = file
            else:
                os.remove(file)
        os.chdir(current_directory)
    except:
        os.chdir(current_directory)
    print(f"Currently in directory:{os.getcwd()}")
    print(f"File coming out of the function: {best_scoring_file}")
    return best_scoring_file



def plot_confusion_matrix(computed_confusion_matrix, list_classes: List,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(computed_confusion_matrix, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(list_classes))
    plt.xticks(tick_marks, list_classes, rotation=45)
    plt.yticks(tick_marks, list_classes)

    if normalize:
        cm = np.round(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], 5)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')



def plot_probabilities(y_prediction: np.ndarray):
    p_max = np.amax(y_prediction, axis=1)
    plt.hist(p_max, normed=True, bins=list(np.linspace(0,1,11)))
    plt.xlabel('Probability of predicted class')
    plt.ylabel('Certainty')
    plt.show()



def plot_probabilities_by_picture(y_prediction: np.ndarray, label_list: List):
    for i in list(range(10)):

        # plot probabilities:
        ax = plt.subplot2grid((10, 5), (i, 0), colspan=4);
        plt.bar(np.arange(5), y_prediction[i], 0.35, align='center');
        plt.xticks(np.arange(5), label_list)
        plt.tick_params(axis='x', bottom='off', top='off')
        plt.ylabel('Probability')
        plt.title("Probability for all the different mole types")
        plt.ylim(0,1)
        plt.subplots_adjust(hspace = 0.5)

        # plot picture:
        ax = plt.subplot2grid((10, 5), (i, 4));
        plt.imshow(X_test[i].reshape((28,28)),cmap='gray_r', interpolation='nearest');
        plt.xlabel(label_dict[y_test[i]]); # get the label from the dict
        plt.xticks([])
        plt.yticks([])
        plt.title("Mole Example")
        plt.show()


def plot_and_print_loss(history):
    """ Plots evolution of test_loss v val_loss of a NN."""
    plt.plot(history.history['loss'], label='test_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 0.8])
    plt.xlabel('Epoch')
    plt.ylabel('Loss_score')
    plt.title("Comparing test to validation set")
    plt.legend()
    plt.grid(True)
    print(f"""Status at last epoch:
train_score = {history.history['loss'][-1]}
val_score   = {history.history['val_loss'][-1]}""")
    plt.show()


def preprocessing_hair_remove(image):
    """ Removes hairs from mole-images """
    image= plt.imread(image)
    # convert image to grayScale
    grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # kernel for morphologyEx
    kernel = cv2.getStructuringElement(1,(17,17))
    # apply MORPH_BLACKHAT to grayScale image
    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
    # apply thresholding to blackhat
    _,threshold = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
    # inpaint with original image and threshold image
    final_image = cv2.inpaint(image,threshold,1,cv2.INPAINT_TELEA)
    return final_image