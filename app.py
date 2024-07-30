import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.app_summary import app_summary_page
from app_pages.app_sale_price_study import app_sale_price_study

app = MultiPage(app_name= "Heritage Housing")

app.app_page("Project Summary", app_summary_page)
app.app_page("Housing Price Study", app_sale_price_study)

app.run()