import os
import streamlit as st
import logging
from google.cloud import logging as cloud_logging
import vertexai
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory
)

# configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# attach a Cloud Logging handler to the root logger
log_client = cloud_logging.Client()
log_client.setup_logging()

PROJECT_ID = os.getenv("PROJECT_ID")  
LOCATION = os.getenv("LOCATION")

#PROJECT_ID = os.environ.get("storyteller-449312")  # Your Google Cloud Project ID
#LOCATION = os.environ.get("eu-west1")  # Your Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

# prompt = """
# Ben bir hikaye yaratici yapay zeka uygulamasiyim. Cocuklar icin ahlaki degerlere uygun
# hikayeler olusturuyorum. {konu} \n
# ile alakali ortalama okuma süresi {süre} dakika olacak bir hikaye olustur. Bu hikayeyle ilgili görsellerde yaratabilirsin. 
# Olusturdugun hikayeler cocugun hayal gücünü artirici, merak uyandiracak sekilde 3 ile 8 yas arasi cocuklara
# hitap etsin. 
# """

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
    stream: bool = True
    ):
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    try:
        # ✅ Generate response first
        responses = model.generate_content(
            contents,
            generation_config=config,
            safety_settings=safety_settings,
            stream=stream,
        )

        final_response = []
        if isinstance(responses, list):
            for response in responses:
                if hasattr(response, "text"):
                    final_response.append(response.text)
                elif isinstance(response, dict) and "text" in response:
                    final_response.append(response["text"])
        elif hasattr(responses, "text"):
            final_response.append(responses.text)

        return " ".join(final_response)

    except Exception as e:
        logger.error(f'Gemini API hatasi: {e}')
        return 'Hikaye olustururken bir hata olustu!'

st.header("Vertex AI Gemini API", divider="gray")
