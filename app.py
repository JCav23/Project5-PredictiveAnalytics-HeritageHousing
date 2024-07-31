import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.app_summary import app_summary_page
from app_pages.app_sale_price_study import app_sale_price_study
from app_pages.app_predictive_analysis import app_predictive_analysis_page
from app_pages.app_hypothesis import app_hypothesis_validation
from app_pages.app_pipeline_evaluation import app_pipeline_performance

app = MultiPage(app_name= "Heritage Housing")

app.app_page("Project Summary", app_summary_page)
app.app_page("Housing Price Study", app_sale_price_study)
app.app_page("Predicting Prices", app_predictive_analysis_page)
app.app_page("Hypothesis Validation", app_hypothesis_validation)
app.app_page("Machine Learning Perfomance", app_pipeline_performance)

app.run()