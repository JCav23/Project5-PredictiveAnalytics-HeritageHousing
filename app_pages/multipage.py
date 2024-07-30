import streamlit as st

page_image = 'https://www.shutterstock.com/image-vector/illustration-simple-house-isolated-on-600nw-1937900650.jpg'
icon_link = 'https://img.icons8.com/?size=100&id=12229&format=png&color=000000'

def background_img(file):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{page_image}");
        background-size: 15%;
        background-position: bottom right;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name,
            page_icon = icon_link
        )

        background_img(page_image)

    def app_page(self, title, function):
        self.pages.append({"title": title, "function": function})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
    