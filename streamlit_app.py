import streamlit as st
import requests
from PIL import Image as PILImage

def main():
    st.title("Book OCR Application")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = PILImage.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        st.write("Processing...")

        # Send image to Flask API
        files = {'file': uploaded_file.getvalue()}
        response = requests.post('http://127.0.0.1:5000/process-image', files=files)

        if response.status_code == 200:
            ocr_result = response.json().get('ocr_result')
            st.write("OCR Result:", ocr_result)
        else:
            st.write("Error:", response.json().get('error'))

if __name__ == "__main__":
    main()
