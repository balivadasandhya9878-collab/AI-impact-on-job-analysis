import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 AI Impact on Jobs Analysis")

# -------- Step 1: Load dataset --------
excel_file = "ai_job_impact_dataset_100rows.xlsx"

if os.path.exists("ai_job_impact_dataset.pkl"):
    df = pd.read_pickle("ai_job_impact_dataset.pkl")
    st.success("Loaded dataset from pickle file.")
else:
    df = pd.read_excel(excel_file)
    st.success("Loaded dataset from Excel file.")
    df.to_pickle("ai_job_impact_dataset.pkl")

# -------- Dataset Info --------
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Info")
st.write(df.describe())

# -------- Top 10 AI Impact Jobs --------
st.subheader("Top 10 Jobs by AI Impact Score")

top10 = df.sort_values("AI Impact Score (0-1)", ascending=False).head(10)
st.dataframe(top10)

# -------- Sector Distribution --------
st.subheader("Job Sector Distribution")

sector_counts = df["Job Sector"].value_counts()

fig, ax = plt.subplots()
sector_counts.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)