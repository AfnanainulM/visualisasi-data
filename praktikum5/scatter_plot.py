# import library
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

#adataset utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 120, 150, 180]

#dataset tambahan penjualan
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# data untuk analisis
data = {
    'Suhu' : [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Coklat' : [40, 45,50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanilla' : [82,80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Strawberry' : [55, 50, 55, 68, 65, 60, 65, 70, 72],
    'Kelembapan' : [50, 65, 70, 75, 80, 85, 90, 95, 100]
}

# konversi ke dataframe
df = pd.DataFrame(data)

# layout utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header('Pengaturan Visualisasi')

# menu di sidebar
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# identitas kelompok
st.caption("PRAKTIKUM 5 - Matplotlib Scatter Plot")
st.markdown("""
**Kelompok 3 :**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

# 1. Basic Scatter Plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2. Kustomisasi Scatter Plot
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolors='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu (Kustomisasi)')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3. Multiple Scatter Plot
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label="Hari Kerja", s=80)
    ax.scatter(suhu, penjualan_weekend, color='purple', label="Akhir Pekan", s=80)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 4. Analisis dengan Scatter Plot
def scatter_3_variable():
    st.subheader("4. Analisis dengan Scatter Plot")
    # opsi jenis es krim
    jenis_es_krim = st.selectbox('Pilih Jenis Es Krim', ['Coklat', 'Vanilla', 'Strawberry'])

    # logika untuk opsi jenis es krim berdasarkan pilihan
    if jenis_es_krim == 'Coklat':
        penjualan = df['Penjualan_Coklat']
    elif jenis_es_krim == 'Vanilla':
            penjualan = df['Penjualan_Vanilla']
    else: 
        penjualan = df['Penjualan_Strawberry']
    
    st.subheader("Data Penjualan Es Krim dan Suhu")
    st.dataframe(df)

    # scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # styling plot
    ax.set_title(f'Hubungan Penjualan {jenis_es_krim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_es_krim}')
    fig.colorbar(scatter, label='Kelembapan (%)')
    
    st.pyplot(fig)

    # ringkasan hubungan
    st.subheader("Analisis Hubungan")
    st.write(f'Grafik menunjukan hubungan antara suhu, kelembapan, dan Penjualan Es Krim jenis **{jenis_es_krim}**')

# Routing berdasarkan menu pilihan
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter() 
elif option == "Analisis Scatter Plot":
    scatter_3_variable()