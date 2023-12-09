# import streamlit as st
# import pandas as pd
# from st_aggrid import AgGrid

# st.markdown("View Clean Data")
# st.sidebar.markdown("View Clean Data")

# data = pd.read_csv('/home/himani/project3/pages/cleanedData.csv')

# options = {
#     "columnDefs": [
#         {
#             "headerName": "Gender",
#             "field": "Gender",
#             "editable": False,
#         },
#         {
#             "headerName": "approv_in_adv",
#             "field": "approv_in_adv",
#             "editable": False,
#         },
#          {
#             "headerName": "loan_type",
#             "field": "loan_type",
#             "editable": False,
#         },
#         {
#             "headerName": "loan_purpose",
#             "field": "loan_purpose",
#             "editable": False,
#         },
#          {
#             "headerName": "Credit_Worthiness",
#             "field": "Credit_Worthiness",
#             "editable": False,
#         },
#         {
#             "headerName": "business_or_commercial",
#             "field": "business_or_commercial",
#             "editable": False,
#         },
#          {
#             "headerName": "rate_of_interest",
#             "field": "rate_of_interest",
#             "editable": False,
#         },
#         {
#             "headerName": "Neg_ammortization",
#             "field": "Neg_ammortization",
#             "editable": False,
#         },
#          {
#             "headerName": "interest_only",
#             "field": "interest_only",
#             "editable": False,
#         },
#         {
#             "headerName": "lump_sum_payment",
#             "field": "lump_sum_payment",
#             "editable": False,
#         },
#          {
#             "headerName": "Secured_by",
#             "field": "Secured_by",
#             "editable": False,
#         },
#         {
#             "headerName": "total_units",
#             "field": "total_units",
#             "editable": False,
#         },
#          {
#             "headerName": "income",
#             "field": "income",
#             "editable": False,
#         },
#         {
#             "headerName": "credit_type",
#             "field": "credit_type",
#             "editable": False,
#         },
#          {
#             "headerName": "Credit_Score",
#             "field": "Credit_Score",
#             "editable": False,
#         },
#         {
#             "headerName": "co-applicant_credit_type",
#             "field": "co-applicant_credit_type",
#             "editable": False,
#         },
#       {
#             "headerName": "age",
#             "field": "age",
#             "editable": False,
#         },
#          {
#             "headerName": "LTV",
#             "field": "LTV",
#             "editable": False,
#         },
#         {
#             "headerName": "Region",
#             "field": "Region",
#             "editable": False,
#         },
#            {
#             "headerName": "dtir1",
#             "field": "dtir1",
#             "editable": False,
#         },

#     ],
# }

# grid = AgGrid(data)

# df=grid.data
# st.write(df) 
 