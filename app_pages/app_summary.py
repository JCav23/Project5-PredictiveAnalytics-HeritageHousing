import streamlit as st

def app_summary_page():

    st.write("### Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n"
        f"* *SalePrice* is the prediction target for our machine learning model and the total sale price for a house\n\n"
        f"**Project Dataset**\n\n"
        f"This project uses a representative dataset for housing records across Ames, Iowa ranging from 1872 to 2010. "
        f"It covers various features for the houses including (Quality, Kitchen, Garage, Basement, Floor Square Footage) and their respective sale price.\n\n"
        f"**Futher Information**\n\n"
        f"For details about the entire dataset including full explanation of the abbreviations and units please visit the projects "
        f"**[README](https://github.com/JCav23/Project5-PredictiveAnalytics-HeritageHousing)** or "
        f"**[KAGGLE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**"
    )

    st.write("### Business Requirements")

    st.success(
        f"* 1 - The client is interested in discovering how house attributes correlate with sale prices. " 
        f"Therefore, the client expects data visualizations of the correlated variables against the sale price.\n\n"
        f"* 2 - The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa."
    )