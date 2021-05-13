from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pickle
filename = 'finalized_model1.sav'

def predict():
    return 'add function'

def load_UI():
    """ loads the GUI """
    st.title('Heart Disease Prediction')

    age = st.text_input('Enter Age')

    sex = st.text_input('Enter Sex')

    cp = st.text_input('Enter CP')

    trestbps = st.text_input('Enter trestbps')

    chol = st.text_input('Enter chol')

    fbs = st.text_input('Enter fbs')

    restecg = st.text_input('Enter restecg')

    thalach = st.text_input('Enter thalach')

    exang = st.text_input('Enter exang')

    oldpeak = st.text_input('Enter oldpeak')

    slope = st.text_input('Enter slope')

    ca = st.text_input('Enter ca')

    thal = st.text_input('Enter thal')

    x = st.button('predict')
    if(x):
        if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal):
            input = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
            if(pred(input)[0] == 0):
                st.text('Your are Safe, You don\'t have any Heart Disease !!! Stay Safe Track your health Daily')
            else:  
                st.text('Your report says that you haveHeart Disease')
        else:
            st.text('Please fill all the fields!!!') 

def pred(input):
    print("loading saved model")
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    preds = loaded_model.predict(input.reshape(1, -1))
    return preds


load_UI()