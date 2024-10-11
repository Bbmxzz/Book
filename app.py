import streamlit as st
from PIL import Image as PILImage
import logging
import easyocr
from roboflow import Roboflow
import numpy as np
import os

# Initializations
rf = Roboflow(api_key="GjIhJ9A525bYsGiVQIRA")
project = rf.workspace("kwsr").project("book-gtby9")
model = project.version(6).model

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def main():
    st.title("Book OCR Application")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        img = PILImage.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        st.write("Processing...")

        # Process the image
        process_image(img)

def process_image(img):
    # Implement your processing logic here as in your Flask app
    temp_file_path = f"./{secure_filename(uploaded_file.name)}"
    img.save(temp_file_path)

    # Predict using Roboflow
    result = model.predict(temp_file_path, confidence=40, overlap=30).json()
    logging.debug(f"Roboflow result: {result}")

    if result.get('predictions'):
        prediction = result['predictions'][0]
        left = prediction['x'] - (prediction['width'] / 2)
        top = prediction['y'] - (prediction['height'] / 2)
        right = prediction['x'] + (prediction['width'] / 2)
        bottom = prediction['y'] + (prediction['height'] / 2)

        image_crop = img.crop((left, top, right, bottom)).convert('L')
        logging.debug("Image cropped successfully")

        # OCR
        reader = easyocr.Reader(['th', 'en'])
        text = reader.readtext(np.array(image_crop), detail=0, paragraph=True)
        ocr_result = " ".join(text).strip()
        logging.debug(f"OCR result: {ocr_result}")

        # Display result
        st.write("OCR Result:", ocr_result)

        # Clean up
        os.remove(temp_file_path)
    else:
        logging.error("No predictions made by Roboflow")
        st.write("Error: No predictions made by Roboflow")

if __name__ == "__main__":
    main()
