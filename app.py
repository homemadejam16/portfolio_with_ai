import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Page configuration
st.set_page_config(
    page_title="Hongmei's Portfolio",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="auto",
)

# Sidebar menu
with st.sidebar:
    choose = option_menu(
        "Hongmei Jian Roy",
        [
            "Lucy",
            "About Me",
            "Experience",
            "Technical Skills",
            "Education",
            "Achievement"
            "Projects",
            "Contact",
        ],
        icons=[
            "robot",
            "person fill",
            "clock history",
            "tools",
            "book half",
            "clipboard",
            "trophy fill",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )

    # Social media links
    st.markdown(
        "<div style='text-align: center;'>"
        "<a href='https://www.linkedin.com/in/hongmei-jian-roy-ab35471b0'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/homemadejam16'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:homemadejam16@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )

# Map selection to modules
pages = {
    "Lucy": "subpages.home",
    "About Me": "subpages.About_Me",
    "Experience": "subpages.Experience",
    "Technical Skills": "subpages.technical_skills",
    "Education": "subpages.Education",
    "Projects": "subpages.Projects",
    "Achivements": "subpages.Achivements",
    "Contact": "subpages.Contact",
}

# Dynamically load and display the selected page
page_module = pages.get(choose)
if page_module:
    module = importlib.import_module(page_module)
    module.show_page()


