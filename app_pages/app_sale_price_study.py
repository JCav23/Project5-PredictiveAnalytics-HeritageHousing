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
        f"* As part of the buisness requirement a study was conducted on the correlation levels of the features "
        f"found within the dataset. This was used to better understand how these features correlated to the "
        f"houses' respective **`SalePrice`**. \n\n"
        f"* Multivariate analysis was carried out to examine how both the overall `Quality`, and `Condition` "
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
        st.write('**Please use Plotly controls to examine chart in more detail**')
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
        st.plotly_chart(fig, True)

    if st.checkbox('Quality & Condition correlation against SalePrice'):
        st.write('**Please use Plotly controls to examine chart in more detail**')
        fig = px.scatter_3d(data, x='OverallQual', y='SalePrice', z='OverallCond', 
                    color_discrete_sequence=px.colors.qualitative.Bold)
        fig.update_layout(
        title = 'Quality & Condition against Sale Price'
    )
        st.plotly_chart(fig, True)

    st.write('---')

    st.write('## Conclusions')
    st.success(
        f"#### Bivariate Analysis\n\n"
        f"**More detailed conclusion insights can be found within the project notebook** "
        f"[**HERE**](https://github.com/JCav23/Project5-PredictiveAnalytics-HeritageHousing/blob/main/jupyter_notebooks/02-SalePrice_Study.ipynb)\n\n"
        f"* `Overall Quality` of the house has a postive effect on the `SalePrice` with higher quality houses being worth more.\n\n"
        f"* Size of the living area (SqFt), has a strong positive effect on the `SalePrice` meaning the larger the living area, then generally, the more expensive the house.\n\n"
        f"* Generally, the more recently the house was built, the more expensive it is\n\n"
        f"* The data shows that the more expensive houses generally tend to have larger garages."
    )

    st.success(
        f"#### Multivariate Analysis - Part 1 (Basement Features)\n\n"
        f"* The study showed that the larger basements tend to increase the `SalePrice`, with the basement quality also pushing the sale price higher.\n\n"
        f"* When looking at the size of unfinished basement area doesn't have much impact on `SalePrice` alone,"
        f" however we can see that the higher quality finish basements have a higher `SalePrice` and less square footage of unfinished basement area\n\n"
        f"* We can clearly see from the plots the more square footage of finished basement there is the more expensive the house\n\n"
        f"* Across all plots we can see the general trend is that the higher quality finishes on the basements tend to increase the houses' `SalePrice`"
        f"\n\n\n"
        f"#### Multivariate Analysis - Part 2 (Quality & Condition)\n\n"
        f"* The `Quality` of each house has a strong positive relationship with `SalePrice`, however `Condition` is does not have as much of an effect as expected."
    )