import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")
# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2) #Porque JPEg?

foto = Image.open("imagens/imagem.jpg")
img = np.array(foto)
st.image(img)
st.text(img.shape)
st.text(img[100, 100]) #Buscando o pixel na linha 100 e coluna 100, o seucanal

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

red = img.copy()
red[:, :, 1] = 0
st.image(red)

green = img.copy()
green[:, 1, :] = 0
st.image(green)

blue = img.copy()
blue[:, :, 1] = 0
st.image(blue)

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)
# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)