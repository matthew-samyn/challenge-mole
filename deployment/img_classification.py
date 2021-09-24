import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
from typing import List
import pandas as pd
import plotly.express as px

labels = {0: "actinic keratoses and intraepithelial carcinomas",
           1:" basal cell carcinomas", 2:"keratinocytic lesions",
          3: " dermatofibromas", 4: "melanomas", 5: "melanocytic nevi",
          6: " vascular lesions"}

cancer_risk = ["Malignous","Malignous","Benign","Benign",
               "Malignous","Benign","Benign"]

def plot_mole_probabilities(prediction_probabilities: List):
    proba = np.array(prediction_probabilities)*100

    df = pd.DataFrame({"label":list(labels.values()),
                                "probability":proba,
                  "cancerous":cancer_risk})

    fig = px.bar(df, x="label",y="probability",color="cancerous",hover_name="cancerous",
                 color_discrete_sequence=px.colors.qualitative.Set1,
                 title="Predicted probability for every type of mole, colored by cancer-risk",
                 labels={"label":"Type of mole", "probability":"Probability", "cancerous":""})
    fig.update_layout(yaxis_range=[0,100])
    fig.update_xaxes(title_font_family="Arial")
    # fig.show()
    return fig

def mole_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1,32, 32, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (32, 32)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return prediction[0] # return probability