from functions import *
#from ? import history


# Calculating accuracy
y_prediction = model.predict_classes(X_test, batch_size=32, verbose=0)
accuracy = accuracy_score(y_test, y_prediction)
print('CNN accuracy: ',accuracy)

# Compute confusion matrix
computed_confusion_metrix = confusion_matrix(y_test, y_pred_cnn)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(computed_confusion_metrix, classes=['akiec','bcc','bkl','df','mel', 'nv', 'vasc'],
                      title='Confusion matrix')
plt.show()


# extract the probability for the label that was predicted:
plot_probabilities(y_prediction)