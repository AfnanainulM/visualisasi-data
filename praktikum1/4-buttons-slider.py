import streamlit as st
import time

st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 4: Buttons dan Sliders")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.title('Creating Checkboxes')
st.write('Select your Hobbies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
    ('Books', 'Movies', 'Sports'))

st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing'])

st.title("Download Button")
# Creating Download Button
try:
    down_btn = st.download_button(
        label="Download Image",
        data=open("assets/Animal10.jpeg", "rb"),
        file_name="downloaded_image.jpg",
        mime="image/jpg"
    )
except FileNotFoundError:
    st.warning("File gambar tidak ditemukan. Pastikan folder 'assets' dan gambar tersedia.")

st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write('Download Complete')

st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')