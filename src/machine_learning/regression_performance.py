import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error

def performance_output(X_train, y_train, X_test, y_test, pipeline):
    st.write("### Model Performance")
    st.info("* Train Set")
    performance_evaluation(X_train, y_train, pipeline)

    st.info("* Test Set")
    performance_evaluation(X_test, y_test, pipeline)

def performance_evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write("* **R2 Score:**", r2_score(y, prediction).round(3))
    st.write("* **Mean Absolute Error:**", mean_absolute_error(y, prediction).round(3))