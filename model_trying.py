import tensorflow as tf
from tensorflow import keras
from keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2

physical_devices = tf.config.experimental.list_physical_devices("GPU")
print("NUM GPUs Available: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)

model = MobileNetV2(include_top=False, input_shape=(32, 32,3))

train_path = "data/train"
test_path = "data/test"
labels = {"akiec":0, "bcc":1, "bkl":2, "df":3, "mel":4, "nv":5, "vasc":6}
classes = list(labels.keys())
size = (32,32)

model_generator = ImageDataGenerator(preprocessing_function=preprocess_input, rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)

train_batches = model_generator.flow_from_directory(train_path,target_size=size,classes=classes,
                                                batch_size=10, shuffle=True, subset="training")
validation_batches = model_generator.flow_from_directory(train_path,size,classes=classes,
                                                batch_size=20, shuffle=True, subset="validation")
test_batches = ImageDataGenerator(preprocessing_function=preprocess_input)\
    .flow_from_directory(test_path,size,classes=classes, batch_size=10, shuffle=False)

from keras import Sequential
from keras.layers import Dense
from keras.layers import Flatten, Dropout, Normalization
from keras.models import Model

# Add new classifier layers. Make sure our your model will only classify 2 classes!
flat1 = Flatten()(model.layers[-1].output)
norm = Normalization()(flat1)
class1 = Dense(512, activation="relu")(norm)
class2 = Dropout(rate=.3)(class1)
class3 = Dense(128, activation="relu")(class2)
class4 = Dense(32, activation="relu")(class3)
output = Dense(7, activation="softmax")(class4)

new_model = Model(inputs=model.inputs, outputs=output)
# Summarize
new_model.summary()

from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
# Compile and fit the model. Use the Adam optimizer and crossentropical loss.
# Make sure you use your data augmentation generators instead of your original data.
learning_rate = 0.006
optimizer = Adam(learning_rate)
loss = "categorical_crossentropy"
metrics = "accuracy"

new_model.compile(optimizer=optimizer, loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False), metrics=metrics)
new_model.fit(train_batches, validation_data= validation_batches,
                                  epochs=10, shuffle=True, verbose=2)

new_model.save("models/best_model.h5")
