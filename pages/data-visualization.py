import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.markdown("Data Visualization")
st.sidebar.markdown("Data Visualization")


df = pd.read_csv('/home/himani/project3/pages/cleanedData.csv')


#pie chart
region_names=df.Region.value_counts().index
region_val=df.Region.value_counts().values
f,a = plt.subplots()
a.pie(region_val,labels=region_names[:],autopct='%1.2f%%')
a.set_title("Loan defaulters on the basis of regions")
st.pyplot(f)




#2
data = df['income']
fig, ax = plt.subplots()
ax.hist(data, bins=30)
ax.set_ylabel("Density")
ax.set_xlabel("Income Value")
ax.set_title("Distribution of income")
st.pyplot(fig)


#3

status_counts = df['Status'].value_counts()
fig, ax = plt.subplots()
# Create a bar plot for loan statuses
ax.bar(status_counts.index, status_counts.values, color=['red', 'green'])
ax.set_xlabel('Loan Status')
ax.set_ylabel('Count')
ax.set_title('Loan Default Status')
st.pyplot(fig)
