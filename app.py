import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pickle
st.title('Financial Fraud Detection Using Deep Learning')
st.write('This is a simple example of using a deep learning model to detect financial fraud')

st.write('The model is trained for  epochs 5')
co1,co2=st.columns(2)
with co1:
    step=st.slider('Represents a unit of time in the real world, with 1 step equating to 1 hour. The total simulation spans 744 steps, equivalent to 30 days',min_value=1,max_value=743,step=1)
with co2:
    type=st.selectbox('Transaction types',['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount=st.number_input('The transaction amount in the local currency')
co3,co4=st.columns(2)
with co3:
    oldbalanceOrg=st.number_input('The initial balance before the transaction')
with co4:
    newbalanceOrig=st.number_input('The new balance after the transaction')
co5,co6=st.columns(2)
with co5:
    oldbalanceDest=st.number_input('The initial recipients balance before the transaction. Not applicable for customers identified by M (Merchants)')
newbalanceDest=st.number_input('The new recipients balance after the transaction. Not applicable for M (Merchants).')
with co6:
    isflaggedFraud=st.radio('Flags large-scale, unauthorized transfers between accounts, with any single transaction exceeding 200,000 being considered illegal',(0,1))
if st.button('predict'):
    data={'step':[step],'type':type,'amount':amount,'oldbalanceOrg':oldbalanceOrg,'newbalanceOrig':newbalanceOrig,'oldbalanceDest':oldbalanceDest,'newbalanceDest':newbalanceDest,'isFlaggedFraud':isflaggedFraud}
    df=pd.DataFrame(data)
    prepocess=pickle.load(open('preprocessor.pkl','rb'))
    df=prepocess.transform(df)
    model=load_model('my_model.h5')
    pred=model.predict(df)

    if pred>0.5:
        st.error('Fraud')
    else:
        st.success('Not Fraud')






