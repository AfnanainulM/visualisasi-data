import streamlit as st 
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi — 0110222084  
2. Faqih Al Fauzan — 0110222152  
3. Afnan Ainul Mardhiyyah — 0110222128
""")

st.graphviz_chart("""
            digraph {
                "Training Data" -> "ML Algorithm"
                "ML Algorithm" -> "Model"
                "Model" -> "Result Forecasting"
                "New Data" -> "Model"
                }
                  """)