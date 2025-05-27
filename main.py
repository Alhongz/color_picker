import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
from PIL import Image
import os
import color

st.write("## Color Extractor")
st.write("140810230020 - Alfarisy")

x = st.file_uploader("Masukan foto", accept_multiple_files=False)
n_colors = 0
pic_path = ""
if x:
    n_colors = st.number_input("Masukan jumlah output warna!", min_value=3, max_value=10)
    pic_path = "picture/pic1.jpg"

    # Buka image dari uploader
    pic = Image.open(x)

    # <<< TAMBAHKAN: pastikan folder 'picture' ada
    os.makedirs("picture", exist_ok=True)

    # <<< TAMBAHKAN: konversi ke RGB supaya bisa disimpan sebagai JPEG
    pic = pic.convert("RGB")

    # Simpan sementara
    pic.save(pic_path)
else:
    st.write()

button_start = st.button("Start Extracting")
if button_start and x:
    result = color.extract_colors(pic_path, n_colors=n_colors)
    
    st.write(f"🎯 Extracted in {result['duration']:.2f} seconds")

    # Tampilkan gambar asli
    st.image(result["original_image"], caption="Original Image")

    # Visualisasi palette
    import numpy as np

    palette = result["palette"]
    plt.figure(figsize=(n_colors, 2))
    plt.imshow([palette.astype("uint8")])
    plt.axis('off')
    plt.title("Extracted Palette", fontsize=14)

    # Tambahkan kode hex di bawah tiap warna
    for idx, hex_code in enumerate(result["hex_color"]):
        plt.text(
            x=idx, y=0.55, s=hex_code, ha='center', va='top',
            fontsize=5, color='black', rotation=0, weight='bold'
        )

    st.pyplot(plt)
    st.image(result["quanticized_image"], caption=f"Quantized with {n_colors} colors")
