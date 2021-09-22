import streamlit as st
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageOps
from img_classification import mole_classification
from tensorflow import keras

# make container:
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


with header:
    st.header("_ Header  _")
    st.title(" Mole detection ")
    image = Image.open('images/ai-care.jpg')
    st.image(image, width=600)
    st.write('---')

with dataset:
    st.header(" Dataset ")
    st.title(" Image for diagnostic ")
    st.text("Upload the photo(jpg) with the stain on the skin:")
    uploaded_file = st.file_uploader("Choose the photo ...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded "cancer" image.', width=600)
        # st.write("")
        st.write("Classifying...")
        #label = mole_classification(image, 'models/best_model.h5')

        # model = keras.models.load_model('models/best_model.h5')
        # label = model.predict(image)

        label = 5 # test
        st.write('label= ', label)

        # labels = {"akiec": 0, "bcc": 1, "bkl": 2, "df": 3, "mel": 4, "nv": 5, "vasc": 6}
        labels = {"actinic keratoses and intraepithelial carcinomas_akiec": 0,
                  " basal cell carcinomas_bcc": 1, "benign keratinocytic lesions_bkl": 2,
                  " dermatofibromas _df": 3, "melanomas_mel": 4, "melanocytic nevi_nv": 5,
                  " vascular lesions_vasc": 6}
        key_list = list(labels.keys())
        val_list = list(labels.values())

        position = val_list.index(label)
        cancer_name = key_list[position]

        # malignant:
        if (label == 0) | (label == 1) | (label == 4):
            st.subheader('The scanned picture has probability malignant diagnostic')
            st.write("Prediction of malignant: ", cancer_name)
            st.write('Probability: ')
            st.write('It is better to ask a dermatologist for a consultation')
            st.write('---')

        # benign:
        else:
            st.subheader('The scanned picture has probability benign diagnostic')
            st.write("Prediction of benign: ", cancer_name)
            st.write('Probability: ')
            st.write('If the probability is > 50%, it is better to ask a dermatologist for a consultation')
            st.write('---')

#    n_row=st.selectbox('Number of rows ?', options=[5, 10, 20, 50], index=0)
#    st.write(df.head(n_row))

# with features:

# with model_training:
'''
df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)
# Apply Model to Make Prediction
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

'''
'''
st.header('Plotting')
    #st.text('This is description....')
    sel_col, disp_col = st.columns(2)

    #first column:
    sel_col.subheader('Review_score count')
    rev_score= pd.DataFrame(df['review_score'].value_counts()).head(50)
    sel_col.bar_chart(rev_score, width=80)

    # 2nd column:

    disp_col.subheader('Price / total_positive:')
    x_max = disp_col.slider('X scale_max: ', 200, 1500, 1000)
    y_max = disp_col.slider('Y scale_max: ', 10, 200, 100)
    fig, ax = plt.subplots()
    #sns.lmplot(x='total_positive', y='final', data=df)
    #sns.distplot(df['final'])
    #sns.lmplot(x='num_reviews', y='final', data=df,
    #           fit_reg=False,  # No regression line
    #           hue='review_score')  # Color by evolution stage
    #plt.bar(df['total_positive'],df['final'])
    #ax.hist(df['total_positive'], rwidth=0.8)
    ax.scatter(x=df['total_positive'], y=df['final'], c='blue', alpha=0.3, edgecolors='red')
    #sns.distplot(df['total_positive'])
    plt.xlabel("total_positive")
    plt.ylabel("final (price)")
    plt.xlim(0,x_max)
    plt.ylim(0,y_max)
    
    disp_col.write(fig)

'''

