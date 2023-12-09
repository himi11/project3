import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Defaulter')

st.sidebar.markdown("Predict loan defaulter")


st.subheader("Enter details below")


#CREATING OUR FORM FIELDS 
with st.form("form1", clear_on_submit=True):

     gender = st.selectbox("Gender", ('Male','Female', 'Joint','Sex not available'))
     approv_in_adv = st.selectbox("Loan Approved in advance",('No', 'Yes'))  #0- nopre , 1= pre
     loan_type = st.selectbox("Loan Type" , ('Type 1','Type 2','Type 3'))
     loan_purpose = st.selectbox("loan_purpose", ('P1','P2', 'P3','P4'))
     credit_Worthiness= st.selectbox("Credit Worthiness", ('L1','L2') )
     business_or_commercial = st.selectbox("Business/Commercial", ('Yes','No'))
     rate_of_interest = st.text_input("rate_of_interest")
     neg_ammortization = st.selectbox("Negative ammortization", ('Not negative','negative'))
     interest_only = st.selectbox("Interest_only" , ('Yes', 'No'))
     lump_sum_payment = st.selectbox("Lump Sum Payment", ('Yes','No'))
     Secured_by = st.selectbox("Secured by", ('Home','land'))

     total_units = st.text_input("Total_units")

     income = st.text_input("Income",(""))
     
     credit_type = st.selectbox("Credit Type",('EXP','EQUI','CRIF','CIB'))
     credit_Score = st.text_input("Credit Score")
     
     coapplicant_credit_type = st.selectbox("Co-applicant credit type",('EXP','EQUI','CRIF','CIB'))
     age = st.selectbox("Age",("<=24","25-34","35-44","45-54","55-64","65-74" ">74"))
     
     ltv = st.text_input("LTV",placeholder="decimal value between 0-100")
     region = st.selectbox("Region",("North","South","North-East","Central"))
     dtir1 = st.text_input("dtir1")

     submit = st.form_submit_button("Predict Loan defaulter")