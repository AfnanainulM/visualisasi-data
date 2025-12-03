import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart dengan Matplotlib")
st.write("Kelompok: 3")
st.caption("PRAKTIKUM 4")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

# data
data = {
    'Jurusan' : ['Ilmu Komputer', 'Teknik Informatika', 
                'Sistem Informasi', 'Data Sience'],
    'Jumlah Mahasiswa' : [120, 150, 100, 80]
}

df = pd.DataFrame(data)

# streamlit bar chart
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

# Streamlit App - Menggunakan Matplotlib (lebih banyak kustomisasi)
st.title("Basic Bar Chart Menggunakan Matplotlib")

fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

st.title("Kustomisasi Basic Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'purple']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)

ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menambahkan nilai pada batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, str(bar.get_height()), ha='center')

st.pyplot(fig)