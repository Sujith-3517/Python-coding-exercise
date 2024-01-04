import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Upload image from user's computer
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Convert the uploaded image to grayscale
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert('L')

    # Display the grayscale image
    st.image(gray_uploaded_img, caption="Grayscale Image", use_column_width=True)
