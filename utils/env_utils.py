import os

def is_streamlit_cloud():
    return os.environ.get("STREMLIT_SERVER_HEADLESS") == "1" or os.environ.get("STREAMLIT_ENV") == "cloud"
