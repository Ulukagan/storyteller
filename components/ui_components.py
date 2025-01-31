import streamlit as st
from utils.helpers import get_base64_of_bin_file
from datetime import datetime

def display_logo():
    st.markdown(
        """
        <div class="footer-container">
            <span class="powered-by-text">Powered by</span>
            <img src="data:image/svg+xml;base64,{}" class="logo-img" alt="HAPPTIQ Logo">
        </div>
        """.format(get_base64_of_bin_file('assets/HAPPTIQ_logo_RGB_whiteBG.svg')),
        unsafe_allow_html=True
    )

def display_welcome_header():
    st.markdown(
        """
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='color: #2C3E50; font-size: 2.5rem; margin-bottom: 1rem;'>
                Yapay Zeka Storyteller Platformuna Hosgeldiniz!
            </h1>
            <p style='color: #34495E; font-size: 1.2rem; margin-bottom: 2rem;'>
                Yapay Zeka ile Hikayeni Yaz...
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

def display_chat_message(sender, message, message_class):
    timestamp = datetime.now().strftime("%H:%M")
    return f"""
        <div class="chat-message {message_class}">
            <strong>{sender}</strong>
            <div style="margin-top: 0.3rem;">{message}</div>
            <div class="message-timestamp">{timestamp}</div>
        </div>
        """

def display_chat_header():
    return """
        <div class="chat-header">
            <span>💬 Chat with AI Assistant</span>
        </div>
    """