import itertools
from typing import List
from model import *


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

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


def plot_probabilities(y_prediciton):
    p_max = np.amax(cnn_probab, axis=1)
    plt.hist(p_max, normed=True, bins=list(np.linspace(0,1,11)))
    plt.xlabel('p of predicted class')
    plt.show()
fig, ax = plt.subplots(figsize=(6,15))


def plot_probabilities_by_picture(y_prediction, label_list: List):
    for i in list(range(10)):

        # plot probabilities:
        ax = plt.subplot2grid((10, 5), (i, 0), colspan=4);
        plt.bar(np.arange(5), y_prediction[i], 0.35, align='center');
        plt.xticks(np.arange(5), label_list)
        plt.tick_params(axis='x', bottom='off', top='off')
        plt.ylabel('Probability')
        plt.ylim(0,1)
        plt.subplots_adjust(hspace = 0.5)

        # plot picture:
        ax = plt.subplot2grid((10, 5), (i, 4));
        plt.imshow(X_test[i].reshape((28,28)),cmap='gray_r', interpolation='nearest');
        plt.xlabel(label_dict[y_test[i]]); # get the label from the dict
        plt.xticks([])
        plt.yticks([])
        plt.show()