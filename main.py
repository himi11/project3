import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Defaulter')

st.sidebar.markdown("Predict loan defaulter")


st.subheader("Enter details below")


#CREATING OUR FORM FIELDS 
with st.form("form1", clear_on_submit=True):

     gender = st.text_input("Gender")
     approv_in_adv = st.text_input("approv_in_adv")
     loan_type = st.text_area("loan_type")
     loan_purpose = st.selectbox("loan_purpose", ('',''))
     credit_Worthiness= st.text_input("Credit Worthiness")
     business_or_commercial = st.selectbox("Use Type", ('Business','Commercial'))
     rate_of_interest = st.text_area("rate_of_interest")
     neg_ammortization = st.selectbox("Neg_ammortization", ('',''))
     interest_only = st.text_input("interest_only")
     lump_sum_payment = st.text_input("lump_sum_payment")
     Secured_by = st.text_area("Secured_by")
     total_units = st.selectbox("total_units", (""))
     income = st.selectbox("income",(""))
     credit_type = st.text_input("credit_type")
     credit_Score = st.text_input("Credit_Score")
     coapplicant_credit_type = st.text_area("co-applicant_credit_type")
     age = st.selectbox("age",(""))
     ltv = st.selectbox("LTV",(""))
     region = st.selectbox("Region",(""))
     dtir1 = st.text_input("dtir1")

     submit = st.form_submit_button("Predict Loan defaulter")