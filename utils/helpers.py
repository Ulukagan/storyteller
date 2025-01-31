import base64
import re
import streamlit as st

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_page_background(png_file, opacity=0.5):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    body {{
    background-image: url("data:image/png;base64,{bin_str}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    opacity: {opacity};
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def is_valid_email(email): 
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remove_default_placeholder():
    st.markdown(
        """
        <style>
        [data-testid="InputInstructions"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    ) 