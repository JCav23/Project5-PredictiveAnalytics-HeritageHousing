import streamlit as st
import pandas as pd
from src.machine_learning.predictive_analysis import predict_sale_price
from src.data_access import load_pkl_file

def app_hypothesis_validation():

    version='v1.0.0'
    pipeline = load_pkl_file(f'outputs/ml_pipeline/predict_sale_price/{version}/pipeline.pkl')

    st.write("### Project Hypothesis Validation")

    st.info(
        f"* **Hypothesis One)** It is considered that the Lot area of the property would correlate positvely with the sale price.\n\n"
        f"* **Hypothesis Two)** It is considered that the overall condition of the property would positively correlate with the sale price.\n\n"
        f"* **Hypothesis Three)** It is considered that houses with a similar square footing but higher overall quality of materials"
        f" and finish and a higher overall condition would have a higher sales price.\n\n"
        f"* **Hypothesis Four)** It is considered that those houses in a similar condition but with a higher number of bedrooms above grade, would have a higher sales price.\n\n"
        f"* **Hypothesis Five)** It is considered that houses of a similar size and number of bedrooms would have a higher sale price the more recently they were built."
    )

    st.success(
        f"#### Hypothesis One: Correct\n"
        f"* During our correlation study we analysed `LotArea` against sale price, which showed that LotArea is indeed positively correlated against `SalePrice`\n"
    )

    st.success(
        f"#### Hypothesis Two: Correct\n"
        f"* During our correlation study we analysed `OverallCond` against sale price, it showed that while not as strongly correlated as other features "
        f"there is a mild positive correlation against `SalePrice`\n"
    )

    st.success(
        f"#### Hypothesis Three: Correct\n"
        f"* Using our predictive model we were able to preform a regression analysis and confirm that our prediction was correct and houses that are of higher quality "
        f"and condition are more expensive. Below is the data used to confirm the hypothesis:"
    )
    
    low_qual_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 3,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 5,
        'OverallQual': 5,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 1973,
        'YearRemodAdd': 1994
    }, index=[0])

    high_qual_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 3,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 8,
        'OverallQual': 8,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 1973,
        'YearRemodAdd': 1994
    }, index=[0])

    if st.checkbox("Show Hypothesis Three Results:"):
    
        st.write('### Lower Quality & Condition')
        st.write(low_qual_data)
        predict_sale_price(low_qual_data, pipeline)

        st.write('### Higher Quality & Condition')
        st.write(high_qual_data)
        predict_sale_price(high_qual_data, pipeline)

    st.warning(
        f"#### Hypothesis Four: Unconfirmed\n"
        f"* Using our predictive model we were unable to preform a regression analysis and confirm whether the number of bedrooms affects `SalePrice`. "
        f"Our model is not powerful enough to perform this analysis, so future iterations could expand on this. Below is the data used to confirm the hypothesis"
    )

    low_bedroom_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 2,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 6,
        'OverallQual': 6,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 1973,
        'YearRemodAdd': 1994
    }, index=[0])

    high_bedroom_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 6,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 6,
        'OverallQual': 6,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 1973,
        'YearRemodAdd': 1994
    }, index=[0])

    if st.checkbox("Show Hypothesis Four Results:"):
    
        st.write('### Lower bedroom')
        st.write(low_bedroom_data)
        predict_sale_price(low_bedroom_data, pipeline)

        st.write('### Higher bedroom')
        st.write(high_bedroom_data)
        predict_sale_price(high_bedroom_data, pipeline)

    st.warning(
        f"#### Hypothesis Five: Unconfirmed\n"
        f"* Using our predictive model we were unable to preform a succesful analysis and confirm whether the age of the house affects `SalePrice`. "
        f"Our model is not powerful enough to perform this analysis, so future iterations could expand on this. Below is the data used to confirm the hypothesis"
    )

    old_house_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 4,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 6,
        'OverallQual': 6,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 1943,
        'YearRemodAdd': 1994
    }, index=[0])

    new_house_data = pd.DataFrame({
        '1stFlrSF': 1500,
        '2ndFlrSF': 500,
        'BedroomAbvGr': 4,
        'BsmtExposure': 'Gd',
        'BsmtFinSF1': 500,
        'BsmtFinType1': 'GLQ',
        'BsmtUnfSF': 477,
        'GarageArea': 480,
        'GarageFinish': 'Fin',
        'GarageYrBlt': 1980,
        'GrLivArea': 1500,
        'KitchenQual': 'Ex',
        'LotArea': 5000,
        'LotFrontage': 50,
        'MasVnrArea': 0,
        'EnclosedPorch': 0,
        'OpenPorchSF': 25,
        'OverallCond': 6,
        'OverallQual': 6,
        'TotalBsmtSF': 1000,
        'WoodDeckSF': 0,
        'YearBuilt': 2005,
        'YearRemodAdd': 1994
    }, index=[0])

    if st.checkbox("Show Hypothesis Five Results:"):
    
        st.write('### Lower bedroom')
        st.write(old_house_data)
        predict_sale_price(old_house_data, pipeline)

        st.write('### Higher bedroom')
        st.write(new_house_data)
        predict_sale_price(new_house_data, pipeline)