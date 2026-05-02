import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np

st.title("App chỉnh sửa ảnh")

uploaded_file = st.file_uploader("Upload ảnh", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.subheader("Ảnh gốc")
    st.image(image)

    # ===== Brightness =====
    brightness = st.slider("Độ sáng", 0.5, 2.0, 1.0)

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    # ===== Resize =====
    scale = st.slider("Phóng to / thu nhỏ", 0.5, 2.0, 1.0)

    width, height = image.size
    new_size = (int(width * scale), int(height * scale))
    image = image.resize(new_size)

    st.subheader("Ảnh sau chỉnh sửa")
    st.image(image)

    # ===== Save =====
    if st.button("Tải ảnh"):
        image.save("output.jpg")
        st.success("Đã lưu ảnh output.jpg")
