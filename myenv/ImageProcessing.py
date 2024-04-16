import streamlit as st
from PIL import Image
import numpy as np

# Function to resize an image
def resize_image(image, size):
    resized_image = image.resize(size)
    return resized_image

# Function to convert an image to grayscale
def to_grayscale(image):
    grayscale_image = image.convert('L')
    return grayscale_image

# Function to crop an image
def crop_image(image, box):
    cropped_image = image.crop(box)
    return cropped_image

# Function to rotate an image
def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image

# Main function
def main():
    st.title("Image Processing App")

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.subheader("Original Image")
        original_image = Image.open(uploaded_image)
        st.image(original_image, caption="Original Image", use_column_width=True)

        # Select image processing technique
        technique = st.selectbox("Select Image Processing Technique", ["Resize", "Grayscale", "Crop", "Rotate"])

        # Apply selected technique
        if technique == "Resize":
            width = st.slider("Width", 1, original_image.width, original_image.width // 2)
            height = st.slider("Height", 1, original_image.height, original_image.height // 2)
            resized_image = resize_image(original_image, (width, height))
            st.subheader("Resized Image")
            st.image(resized_image, caption="Resized Image", use_column_width=True)

        elif technique == "Grayscale":
            grayscale_image = to_grayscale(original_image)
            st.subheader("Grayscale Image")
            st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)

        elif technique == "Crop":
            left = st.slider("Left", 0, original_image.width - 1, 0)
            top = st.slider("Top", 0, original_image.height - 1, 0)
            right = st.slider("Right", left, original_image.width, original_image.width)
            bottom = st.slider("Bottom", top, original_image.height, original_image.height)
            box = (left, top, right, bottom)
            cropped_image = crop_image(original_image, box)
            st.subheader("Cropped Image")
            st.image(cropped_image, caption="Cropped Image", use_column_width=True)

        elif technique == "Rotate":
            angle = st.slider("Angle", -180, 180, 0)
            rotated_image = rotate_image(original_image, angle)
            st.subheader("Rotated Image")
            st.image(rotated_image, caption="Rotated Image", use_column_width=True)

if __name__ == "__main__":
    main()
