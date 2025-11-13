import streamlit as st
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("Kelompok: 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi — 0110222084  
2. Faqih Al Fauzan — 0110222152  
3. Afnan Ainul Mardhiyyah — 0110222128
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/(10, 10) + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)