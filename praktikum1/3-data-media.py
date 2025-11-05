import streamlit as st
from PIL import Image
import base64

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 3: Data dan Media Elements")
st.markdown("""
**Nama Lengkap Anggota:**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

st.write("Displaying an Image")
# Displaying image by specifying path
st.image("assets/Animal2.jpeg")
# Image Courtesy by unsplash
st.write("Image Courtesy: unsplash.com")

st.write("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    'assets/Animal1.jpeg',
    'assets/Animal2.jpeg',
    'assets/Animal6.jpg',
    'assets/Animal4.jpeg',
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image courtesy
st.write("Image Courtesy: Unsplash") 

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string.decode()}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
st.write("Image Courtesy: unsplash")
# Calling Image in function
add_local_background_image('assets/Animal5.jpg')

# Membuka gambar dari path lokal
original_image = Image.open("assets/Animal1.jpeg")

# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Mengubah ukuran gambar menjadi 600x400
resized_image = original_image.resize((600, 400))

# Menampilkan gambar hasil resize
st.title("Resized Image")
st.image(resized_image)