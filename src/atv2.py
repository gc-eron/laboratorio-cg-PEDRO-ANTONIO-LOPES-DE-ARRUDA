import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")


img = np.zeros((8,8), dtype=np.uint8)
img[2,5] = 255
img[4:,:] = 128
st.write(img)
st.image(ampliar(img))

bandeira = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira[:] = (0, 156, 59)

bandeira[1, 4] = (255, 255, 0)
bandeira[2, 2:7] = (255, 255, 0)
bandeira[3, 2:7] = (255, 255, 0)
bandeira[4, 4] = (255, 255, 0)

bandeira[2, 2] = (0, 156, 59)
bandeira[2, 6] = (0, 156, 59)
bandeira[3, 2] = (0, 156, 59)           
bandeira[3, 6] = (0, 156, 59)

bandeira[2, 4] = (0, 34, 119)
bandeira[3, 4] = (0, 34, 119)

st.image(ampliar(bandeira))