import streamlit as st

page_image = './assets/img/house.png'

def background_img(file):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{image}");
        background-size: 15%;
        background-position: bottom right;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def fa_icon():
    icon_code = """
    <script src="https://kit.fontawesome.com/8fae13e677.js" crossorigin="anonymous"></script>

    <i class="fa-solid fa-house-chimney-user"></i>
    """
    st.markdown(icon_code, unsafe_allow_html=True)


class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name,
            page_icon = fa_icon
        )

    def app_page(self, title, function):
        self.pages.append({"title": title, "function": function})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()