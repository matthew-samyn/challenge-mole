import numpy as np
import streamlit as st
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageOps
from img_classification import *
from tensorflow import keras

# labels = {"akiec": 0, "bcc": 1, "bkl": 2, "df": 3, "mel": 4, "nv": 5, "vasc": 6}
labels = {0: "actinic keratoses and intraepithelial carcinomas_AKIEC",
            1:" basal cell carcinomas_BCC", 2:"benign keratinocytic lesions_BKL",
            3: " dermatofibromas_DF", 4: "melanomas_mel_MEL", 5: "melanocytic nevi_NV",
            6: " vascular lesions proliferations_VASC"}

texts = ['Actinic keratosis is a pre-cancerous growth that may develop into squamous cell carcinomas if left untreated. These growths may be found in clusters on skin damaged by exposure to ultraviolet (UV) radiation',
         'Basal cell carcinomas (BCCs) are abnormal, uncontrolled growths that arise from the skin’s basal cells in the outermost layer of skin (epidermis)',
         'Benign keratinocytic tumours are extremely common and mainly of cosmetic concern. They may occasionally prove painful',
         'Dermatofibroma is a common overgrowth of the fibrous tissue situated in the dermis (the deeper of the two main layers of the skin). It is benign (harmless) and ill not turn into a cancer. Whilst dermatofibromas are harmless, they can be similar in appearance to other concerning skin tumours. It is therefore important to see a health professional for a diagnosis',
         'Melanoma is a cancer that develops from melanocytes, the skin cells that produce melanin pigment, which gives skin its color.',
         'Melanocytic nevi are benign neoplasms or hamartomas composed of melanocytes, the pigment-producing cells that constitutively colonize the epidermis.',
         'Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks. There are three major categories of vascular lesions: Hemangiomas, Vascular Malformations, and Pyogenic Granulomas'
         ]
# print(texts)
# make container:
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    #st.header("_ Header  _")
    st.title(" Mole detection ")
    image = Image.open('images/ai-care.jpg')
    st.image(image, width=700)
    st.write('---')

with dataset:
    st.title(" Image for diagnostic ")
    st.text("Upload the photo(jpg) with the area you want to examine:")
    uploaded_file = st.file_uploader("Choose the photo ...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded image', width=600)
        prediction_probabilities = mole_classification(image, 'models/best_model.h5')

        # plot the probabilities
        fig = plot_mole_probabilities(prediction_probabilities)
        st.write(fig)
        st.write('---')

        prediction_label = int(np.argmax(prediction_probabilities))
        probability_max = prediction_probabilities[prediction_label]
        # st.write('prediction_label: ', prediction_label)
        # st.write('Probability_max: ', probability_max)
        prediction_name = labels[prediction_label]
        # st.write('prediction_name= ', prediction_name)

        # malignant:
        if (prediction_label == 0) | (prediction_label == 1) | (prediction_label == 4):
            st.subheader('The picture is most probably a **malignant** lesion ')
            st.write("**Prediction of malignant :** ", prediction_name)
            st.write('**Description: **', texts[prediction_label])
            st.write('**Probability (%)**: ', probability_max*100)
            st.write('**It is better to ask a dermatologist for an appointment**')
            st.write('---')

        # benign:
        else:
            st.subheader('The picture is most probably a **benign** lesion')
            st.write("**Prediction of benign :** ", prediction_name)
            st.write('**Description: **', texts[prediction_label])
            st.write('**Probability (%)**: ', probability_max*100)
            st.write('**To be sure ask your dermatologist for an appointment**')
            st.write('---')

        st.subheader(" 7 types of skin lesions :")
        image = Image.open('images/7_type_moles_02.png')
        st.image(image, width=600)
        st.write('---')

with features:
    # st.header(" Dataset ")
    st.title(" Informations : ")
    st.write("Dermatologists nearby : [www.skincare.be](https://www.skincare.be)")
    st.write("Dermatologists near me : [Google search](https://www.google.com/search?q=dermatologist+near+me&rlz=1C1JZAP_enBE892BE892&oq=&aqs=chrome.0.35i39i362l8...8.495618548j0j15&sourceid=chrome&ie=UTF-8)")
    st.write("Skin cancer: [www.skincancer.org](https://www.skincancer.org/skin-cancer-information/)")
    st.write('---')