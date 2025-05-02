🧠 Storyteller
Storyteller is a Streamlit-based application that leverages LLM (e.g., Gemini Pro) to help users generate creative stories interactively through a chat interface.

🚀 Features
Interactive Streamlit frontend.
Gemini Pro-based text generation via get_gemini_pro_text_response.
Modular code structure:
backend/ for model logic.
components/ for UI elements.
utils/ for styling, validation, and helper functions.
Custom UI enhancements (background, headers, CSS).

🛠️ Installation
git clone https://github.com/yourusername/storyteller.git
cd storyteller
pip install -r requirements.txt

📦 Usage
streamlit run streamlit.py

🧩 File Structure
├── backend/               # Model logic and API interaction
├── components/            # UI components (headers, messages)
├── utils/                 # Helper functions and styling
├── streamlit.py           # Main entry point
├── requirements.txt       # Python dependencies
├── Dockerfile  

📄 License
MIT License
