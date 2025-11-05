import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 2: Data Elements")
st.markdown("""
**Nama Lengkap Anggota:**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

st.subheader("DATA FRAME")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

# Menampilkan dataframe
st.dataframe(df)

# Highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

# Highlight nilai terkecil di setiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
# Menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
# Menampilkan metrik tunggal (nilai utama + perubahan nilai)
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)

# Menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm")  # naik dan baik
col2.metric(label="Populasi", value="123 miliar", delta="1 miliar", delta_color="inverse")  # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")  # netral

# Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", value="91456", delta="-113649")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

# Defining multiple arguments in write function
st.write('here is our data', df, 'data is in dataframe format.\n', "\nwrite is super function")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
# Defining chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)
# Defining chart in write() function
st.write(chart)

# Math calculation with no function defined
"Adding 5 & 4 =", 5 + 4
# Displaying variable 'a' and its value
a = 5
'a', a

# Markdown with magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
df = pd.DataFrame({'col': [1,]})
'dataframe', df

# Magic working on charts
import matplotlib.pyplot as plt
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart