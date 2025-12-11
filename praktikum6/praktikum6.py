# import
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# header
st.title("Praktikum 6 Visualisasi Data")
st.write("Kelompok: 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

# data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# data quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# tambahan wajib supaya tidak error
male = q1_male
female = q1_female

# 1. Grafik Stacked Vertical Bar Chart
st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, bottom=male, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)


# 2. Grafik Stacked Vertical Bar Chart dengan Matplotlib
st.subheader("2. Stacked Vertical Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Produk A', color='mediumpurple')
ax.bar(x, product_b, bottom=product_a, label='Produk B', color='lightgreen')

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)


# 3. Grafik Kustomisasi Stacked Vertical Bar Chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Produk A', color='plum')
ax.bar(x, product_b, bottom=product_a, label='Produk B', color='palegreen')

# anotasi
for i in range(len(x)):
    ax.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', va='center', color='white')
    ax.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', va='center', color='black')

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)


# 4. Grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# quarter 1
ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label='Q1 Female', color='lightpink', width=width)

# quarter 2
ax.bar(x + width/2, q2_male, label='Q2 Male', color='blue', width=width)
ax.bar(x + width/2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)