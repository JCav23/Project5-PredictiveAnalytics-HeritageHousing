import streamlit as st
import pandas as pd 
from src.data_access import load_house_dataset, load_inherited_dataset, load_pkl_file
from src.machine_learning.predictive_analysis import predict_sale_price
from datetime import date

def app_predictive_analysis_page():
    version = 'v1.0.0'
    pipeline = load_pkl_file(f'outputs/ml_pipeline/predict_sale_price/{version}/pipeline.pkl')
    
    st.write("### Predicting Sale Price")
    st.write('---')
    st.info(
        f'#### Business Requirement 2\n'
        f'* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.'
    )

    if st.checkbox("Inspect Inherited Housing Records"):
        data = load_inherited_dataset()
        st.write(f"* The dataset has {data.shape[0]} rows, across {data.shape[1]} features.\n\n")
        st.write(data)

    if st.checkbox('Predict Price for Inherited Houses'):
        data = load_inherited_dataset()
        for i in range(len(data)):
            st.write(f"## House {i+1}:")
            predict_sale_price(data.loc[data.index == i], pipeline)

    st.write('---')
    st.write(
        f"* Below you can input the data for the house you would like to predict the `Sale Price` for."

    )

    live_data = create_input_widgets()

    if st.button("Predict Sale Price"): 
        st.write(live_data)
        predict_sale_price(live_data, pipeline)

def create_input_widgets():

    original_housing_data = load_house_dataset()
    percentageMin, percentageMax = 0.3, 1.5

    feature_1, feature_2, feature_3, feature_4, feature_5, feature_6 = st.beta_columns(6)
    feature_7, feature_8, feature_9, feature_10, feature_11, feature_12 = st.beta_columns(6)
    feature_13, feature_14, feature_15, feature_16, feature_17, feature_18 = st.beta_columns(6)
    feature_19, feature_20, feature_21, feature_22, feature_23 = st.beta_columns(5)
    

    live_data = pd.DataFrame([], index=[0])

    with feature_1:
	    feature = "1stFlrSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 50      
			)
            
    live_data[feature] = st_widget

    with feature_2:
	    feature = "2ndFlrSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 50       
			)
            
    live_data[feature] = st_widget

    with feature_3:
	    feature = "BedroomAbvGr"
	    st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 8,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)
            
    live_data[feature] = st_widget

    with feature_4:
	    feature = "BsmtExposure"
	    st_widget = st.selectbox(
			label= feature,
			options= ['Gd', 'Av', 'Mn', 'No', 'None']     
			)
            
    live_data[feature] = st_widget

    with feature_5:
	    feature = "BsmtFinSF1"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 100       
			)
            
    live_data[feature] = st_widget

    with feature_6:
	    feature = "BsmtFinType1"
	    st_widget = st.selectbox(
			label= feature,
			options= ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'None']      
			)
            
    live_data[feature] = st_widget

    with feature_7:
	    feature = "BsmtUnfSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 25       
			)
            
    live_data[feature] = st_widget

    with feature_8:
	    feature = "GarageArea"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 25       
			)
            
    live_data[feature] = st_widget

    with feature_9:
	    feature = "GarageFinish"
	    st_widget = st.selectbox(
			label= feature,
			options= ['Fin', 'RFn', 'Unf', 'None']     
			)

    live_data[feature] = st_widget

    with feature_10:
	    feature = "GarageYrBlt"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)
            
    live_data[feature] = st_widget

    with feature_11:
	    feature = "GrLivArea"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 50       
			)
            
    live_data[feature] = st_widget

    with feature_12:
	    feature = "KitchenQual"
	    st_widget = st.selectbox(
			label= feature,
			options= ['Ex', 'Gd', 'TA', 'Fa', 'Po']      
			)
            
    live_data[feature] = st_widget

    with feature_13:
	    feature = "LotArea"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 150       
			)
            
    live_data[feature] = st_widget

    with feature_14:
	    feature = "LotFrontage"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 10       
			)
            
    live_data[feature] = st_widget

    with feature_15:
	    feature = "MasVnrArea"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 10      
			)
            
    live_data[feature] = st_widget

    with feature_16:
	    feature = "EnclosedPorch"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 10      
			)
            
    live_data[feature] = st_widget

    with feature_17:
	    feature = "OpenPorchSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 10      
			)
            
    live_data[feature] = st_widget

    with feature_18:
	    feature = "OverallCond"
	    st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 10,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)

    live_data[feature] = st_widget    
    
    with feature_19:
	    feature = "OverallQual"
	    st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 10,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)

    live_data[feature] = st_widget

    with feature_20:
	    feature = "TotalBsmtSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 100       
			)

    live_data[feature] = st_widget

    with feature_21:
	    feature = "WoodDeckSF"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= int(original_housing_data[feature].max()*percentageMax),
			value= int(original_housing_data[feature].median()), 
            step = 25       
			)

    live_data[feature] = st_widget

    with feature_22:
	    feature = "YearBuilt"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)
            
    live_data[feature] = st_widget

    with feature_23:
	    feature = "YearRemodAdd"
	    st_widget = st.number_input(
			label= feature,
			min_value= int(original_housing_data[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(original_housing_data[feature].median()), 
            step = 1       
			)
            
    live_data[feature] = st_widget

    return live_data