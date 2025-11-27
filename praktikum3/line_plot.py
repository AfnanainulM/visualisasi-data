import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

#layout streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi",
                              ("Single Line Plot", 
                               "Multiple & Customization",
                               "Jenis Garis Menunjukkan Tren",
                               "Subplot"))


# identitas Kelompok
st.caption("PRAKTIKUM 3 - matplotlib")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

# sigle line plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, color='blue', label='Produk A')
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    st.pyplot(fig)

# Multiple Line Plot & Customizations
def multiple_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Produk A', color='blue',
            marker='o', linestyle='--')
    ax.plot(months, product_B_sales, label='Produk B', color='red',
            marker='x', linestyle='-')
    ax.set_title('Penjualan Produk per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis Garis Menunjukkan Tren
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]

def tren_line_plot():
    fig, axs = plt.subplots()

    axs.plot(months, product_A_sales, label="Product A",
             color='blue', linestyle='--')

    axs.plot(months, product_B_sales, label="Product B",
             color='red', linestyle='-')

    axs.plot(months, product_C_sales, label="Product C",
             color='green', linestyle=':')

    axs.plot(months, product_D_sales, label="Product D",
             color='purple', linestyle='-.')

    axs.set_title("Jenis Garis Menunjukkan Tren Penjualan")
    axs.set_xlabel("Bulan")
    axs.set_ylabel("Jumlah Penjualan")
    axs.legend()
    axs.grid(True)

    st.pyplot(fig)

# Subplots
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))

    # plot pertama product C
    axs[0].plot(months, product_C_sales, label='Product C', 
                color='green', marker='d')
    axs[0].set_title('Penjualan Produk per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # plot kedua product D
    axs[1].plot(months, product_D_sales, label='Product D', 
                color='purple', marker='s')
    axs[1].set_title('Penjualan Produk per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)



# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customization":
    multiple_line_plot()
elif option == "Jenis Garis Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()
    