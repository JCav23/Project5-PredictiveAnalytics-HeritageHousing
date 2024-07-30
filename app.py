import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.app_summary import app_summary_page

app = MultiPage(app_name= "Heritage Housing")

app.app_page("Project Summary", app_summary_page)

app.run()