import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns 
from src.data_access import load_house_dataset

sns.set_style("darkgrid")

def app_sale_price_study():

    data = load_house_dataset()
    data = data.drop(columns=['EnclosedPorch', 'GarageFinish', 'LotFrontage', 'WoodDeckSF'])
    data = data.dropna()

    st.write('## Sale Price Study')
    st.write('---')
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
    st.write('## Introduction')
    st.write(
        f"* As part of the busisness requirement a study was conducted on the correlation levels of the features "
        f"found within the dataset. This was used to better understand how these features correlated to the "
        f"houses' respective **`SalePrice`**. \n\n"
        f"* Multivariate analysis was carried out to examine how both the Overall `Quality`, and `Condition` "
        f"of the house affects the `Sale Price`\n\n"
        f"* A study was also carried out to examine the effect the size and quality of the Basement can have on "
        f"on `SalePrice`."
    )

    st.write('---')
    st.write('## Correlation Results')
    if st.checkbox('Sale Price Correlation by Feature'):
        top_correlated = ['OverallQual', 'GrLivArea', 'YearBuilt', 'GarageArea', 'LotArea']
        target = 'SalePrice'
        for column in top_correlated:
            fig = sns.jointplot(data=data, x=column, y=target, kind='reg')
            plt.suptitle(f'{column} against {target}')
            plt.tight_layout()
            st.pyplot(fig)

    if st.checkbox('Basement Features against SalePrice'):
        fig = px.scatter_matrix(data_frame=data,
                        dimensions=["SalePrice", "TotalBsmtSF", "BsmtUnfSF", "BsmtFinSF1"],
                        color='BsmtFinType1'
                        )
        fig.update_layout(
            title='Basement Features',
            height=1000,
            hovermode='closest'
        )
        fig.update_traces(diagonal_visible=False)
        st.plotly_chart(fig)

    if st.checkbox('Quality & Condition correlation against SalePrice'):
        fig = px.scatter_3d(data, x='OverallQual', y='SalePrice', z='OverallCond', 
                    color_discrete_sequence=px.colors.qualitative.Bold)
        fig.update_layout(
        title = 'Quality & Condition against Sale Price'
    )
        st.plotly_chart(fig)
