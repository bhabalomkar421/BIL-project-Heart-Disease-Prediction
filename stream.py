from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pickle
filename = 'finalized_model1.sav'

def add():
    return 'add function'

def load_UI():
    st.text('Test')
    

    x = st.button('add')
    if(x):
        st.text(x)

def pred(input):
    print("loading saved model")
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    preds = loaded_model.predict(input.reshape(1, -1))
    return preds


load_UI()

# st.title('Heart Disease Prediction')

# age = st.text_input('Enter Age')

# sex = st.text_input('Enter Sex')

# cp = st.text_input('Enter CP')

# trestbps = st.text_input('Enter trestbps')

# chol = st.text_input('Enter chol')

# fbs = st.text_input('Enter fbs')

# restecg = st.text_input('Enter restecg')

# thalach = st.text_input('Enter thalach')

# exang = st.text_input('Enter exang')

# oldpeak = st.text_input('Enter oldpeak')

# slope = st.text_input('Enter slope')

# ca = st.text_input('Enter ca')

# thal = st.text_input('Enter thal')

# if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal):
#     print(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
#     input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
#     # s = age + sex + cp + trestbps + chol + fbs + restecg + thalach + exang + oldpeak + slope + ca + thal
#     # st.text(s)
#     input = np.array(input)
#     x = pred(input)
#     st.text(x)
#     # classify the target variable belong to which class


