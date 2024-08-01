import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_access import load_house_dataset, load_pkl_file
from src.machine_learning.regression_performance import performance_output

def app_pipeline_performance():

    version = "v1.0.0"
    pipeline = load_pkl_file(f'outputs/ml_pipeline/predict_sale_price/{version}/pipeline.pkl')
    X_train = pd.read_csv(f'outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv')
    X_test = pd.read_csv(f'outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv')
    y_train = pd.read_csv(f'outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv')
    y_test = pd.read_csv(f'outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv')

    st.write("## Machine Learning Pipeline Performance")
    st.info(
        f"* Based on our business requirements from the client we aimed to create a *Regressor* pipeline, "
        f"with a target of 0.7 or higher, we were able to consider that our pipeline was successful.\n\n"
        f"* We also trialed a second pipeline integrating Principle Componant Analysis (PCA), "
        f"however it did not perform as well and our orignal pipeline was more successful.\n\n"
        f"* Below you will find listed the pipeline steps, along with the performance metrics, "
        "and feature importance plot, representing how much impact the features had on model performance."
    )
    st.write('---')

    st.write('## Pipeline Steps')
    st.code(pipeline)
    st.write('---')

    st.write('## Model Performance: ')
    col1, col2 = st.beta_columns(2)

    with col1:
        st.write('### Feature Importance')
        st.image('assets/img/Feature Importance.png')

    with col2:
        st.write('### Performance Metrics')
        performance_output(
            X_train=X_train, y_train=y_train,
            X_test=X_test, y_test=y_test,
            pipeline=pipeline)
    