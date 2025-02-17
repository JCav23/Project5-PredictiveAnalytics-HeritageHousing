import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_dataset():
    data = pd.read_csv("inputs/datasets/raw-heritage-housing/house-price-20211124T154130Z-001/house-price/house_prices_records.csv")
    return data

def load_inherited_dataset():
    data = pd.read_csv('inputs/datasets/raw-heritage-housing/house-price-20211124T154130Z-001/house-price/inherited_houses.csv')
    return data

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)