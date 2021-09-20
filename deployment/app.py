import streamlit as st
st.title("Image Classification")
st.header("Image classification Example")
st.text("Upload a mole picture for image classification as what type of formation it is.")
from PIL import Image, ImageOps

from img_classification import mole_classification
uploaded_file = st.file_uploader("Choose a mole ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded mole image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = mole_classification(image, 'models/best_model.h5')
    if label == 0:
        st.write("The picture scan has a brain tumor")
    else:
        st.write("The picture scan is healthy")