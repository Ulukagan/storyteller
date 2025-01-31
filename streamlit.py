import streamlit as st
import logging
from backend.backend import get_gemini_pro_text_response, text_model_pro
from utils.helpers import (
    set_page_background, 
    is_valid_email, 
    load_css, 
    remove_default_placeholder
)
from components.ui_components import (
    #display_logo,
    display_welcome_header, 
    display_chat_message,
    display_chat_header
)

#st.set_page_config(page_title="Yapay Zeka ile Hikayeni Yaz")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def show_login_page():
    set_page_background('assets/ai_photo.png', opacity=0.80)
    load_css('assets/styles/main.css')
    display_welcome_header()

    st.markdown("<h2 style='text-align: left; font-size: 18px;'>Lütfen gecerli bir email adresi giriniz</h2>", unsafe_allow_html=True)
    email = st.text_input('', placeholder='Email Adresi', value=st.session_state.email)
    if st.button("**Onayla**"):
        if email and is_valid_email(email):
            logger.info(f"Got email")
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Lütfen bir email adresi giriniz.")
    email_to_return = email
    #display_logo()
    return email_to_return

def initialize_session_state():
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def show_story_teller_page():
    set_page_background('assets/ai_photo.png', opacity=0.80)
    load_css('assets/styles/main.css')
    display_welcome_header()

    konu = st.selectbox(
    "Hikayeniz hangi konu ile ilgili olsun?",
    ("Macera", "Aslan", "Orman", "Deniz", "Uzay", "Dünyaturu", "Türkiye", "Kartal"),
    index=None,
    placeholder="Bir hikaye konusu seç."
    )

    süre = st.selectbox(
    "Hikayeniz hangi konu ile ilgili olsun?",
    ("5", "10", "15"),
    index=None,
    placeholder="Hikaye süreni seç."
    )

    generate_t2t = st.button("Hikayeni olustur.", key="generate_t2t")
    if generate_t2t and konu and süre:
        prompt = f"{konu} konulu, {süre} dakika süren bir hikaye oluştur."
        # st.write(prompt)
        with st.spinner("Hikayeniz olusturuluyor..."):
            response = get_gemini_pro_text_response(
                    text_model_pro,
                    prompt
                )
            if response:
                st.write("Hikaye:")
                st.write(response)
                logging.info(response)
        
def main():
    logger.info("Main method")
    initialize_session_state()
    
    if st.session_state.email == "":
        logger.info("show login")
        show_login_page()
    else:
        show_story_teller_page()

if __name__ == "__main__":
    main()
