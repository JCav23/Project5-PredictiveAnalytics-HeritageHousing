import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns 
from src.data_access import load_house_dataset

sns.set_style("darkgrid")

def app_sale_price_study():

    data = load_house_dataset()

    st.write('## House Price Study')
    st.info(
        f'#### Business Requirement 1\n'
        f'* 1 - The client is interested in discovering how house attributes correlate with sale prices. '
        f'Therefore, the client expects data visualizations of the correlated variables against the sale price.'
    )

    if st.checkbox("Inspect Raw Housing Records"):
        st.write(
            f"* The dataset has {data.shape[0]} rows, across {data.shape[1]} features.\n\n"
        )
        st.write(data.head(15))

    st.write('---')

    st.write(
        
    )

    # fig = px.scatter_3d(heritage_housing, x='OverallQual', y='SalePrice', z='OverallCond', 
    #                 color_discrete_sequence=px.colors.qualitative.Bold)
    # fig.update_layout(
    #     title = 'Quality & Condition against Sale Price'
    # )
    # fig.show()
