import os
import streamlit as st
import logging
from google.cloud import logging as cloud_logging
import vertexai
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Attach a Cloud Logging handler to the root logger
log_client = cloud_logging.Client()
log_client.setup_logging()

# Get environment variables
PROJECT_ID = os.getenv("PROJECT_ID")  
LOCATION = os.getenv("LOCATION")

# Ensure environment variables are set correctly
if not PROJECT_ID or not LOCATION:
    logger.error("PROJECT_ID or LOCATION environment variable is missing!")

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def load_models():
    return GenerativeModel("gemini-pro")

text_model_pro = load_models()

# Generation Config
config = GenerationConfig(
    temperature=0.7,
    max_output_tokens=1024
)

def get_gemini_pro_text_response(
    model: GenerativeModel,
    contents: str,
    stream: bool = False
):
    try:
        # ✅ Generate response without safety settings (default Google filtering applies)
        responses = model.generate_content(
            contents,
            generation_config=config,
            stream=stream,
        )

        logger.info(f"Raw Gemini API Response: {responses}")

        final_response = []
        
        # ✅ Convert generator to list to process properly
        if isinstance(responses, (list, tuple)):
            response_list = responses  
        elif hasattr(responses, "__iter__"):  
            response_list = list(responses)  
        else:
            response_list = [responses]  

        # ✅ Extract text from each response
        for response in response_list:
            if hasattr(response, "text"):
                final_response.append(response.text)
            elif isinstance(response, dict) and "text" in response:
                final_response.append(response["text"])

        result = " ".join(final_response)
        logger.info(f"Processed Response: {result}")
        
        return result or "Hikaye olusturulamadi!"  

    except Exception as e:
        logger.error(f'Gemini API hatasi: {e}')
        return 'Hikaye olustururken bir hata olustu!'

st.header("Vertex AI Gemini API", divider="gray")
