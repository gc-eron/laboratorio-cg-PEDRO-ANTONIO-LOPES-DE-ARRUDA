import cv2
import numpy as np
import streamlit as st
from PIL import Image
st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/imagem.jpg")
img = np.array(foto)
# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)

cor = np.uint8([[[230, 140, 60]]])
hsv = cv2.cvtColor(cor, cv2.COLOR_RGB2HSV)
st.text(hsv[0, 0])

rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)## De volta para RGB
st.text(rgb[0, 0])


# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)
# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)
# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)


## Tem como não ter no RGB o H que desejamos.