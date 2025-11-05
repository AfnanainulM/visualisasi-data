import streamlit as st
import datetime
import pandas as pd


# HEADER SECTION

st.set_page_config(page_title="Data Visualization Practicum", layout="centered")

st.title("📊 PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 5: Forms")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi — 0110222084  
2. Faqih Al Fauzan — 0110222152  
3. Afnan Ainul Mardhiyyah — 0110222128
""")

st.markdown("---")


# TEXT INPUT SECTION

st.header("📝 Text Inputs")

name = st.text_input("Enter your name")
if name:
    st.success(f"Your name is: **{name}**")

input_text = st.text_area("Enter your review")
if input_text:
    st.info(f"You entered:\n\n{input_text}")

st.markdown("---")


# NUMBER INPUT SECTION

st.header("🔢 Number Inputs")

col1, col2 = st.columns(2)
with col1:
    st.number_input("Enter a simple number")
with col2:
    num = st.number_input("Enter a number (0–10)", 0, 10, 5, 2)
    st.caption("Min: 0 | Max: 10 | Default: 5 | Step: 2")

st.write("Total value after applying step value:", num)

st.markdown("---")


# TIME & DATE INPUT SECTION

st.header("⏰ Time & Date Inputs")

col1, col2 = st.columns(2)
with col1:
    selected_time = st.time_input("Select a time")
    st.write("Selected time:", selected_time)

with col2:
    selected_date = st.date_input("Select a date")
    st.write("Selected date:", selected_date)

st.date_input(
    "Select a date (with range)",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)

st.markdown("---")


# COLOR PICKER SECTION

st.header("🎨 Color Picker")
color_code = st.color_picker("Choose your color")
st.markdown(f"**Selected color code:** `{color_code}`")

st.markdown("---")


# DATASET UPLOAD SECTION

st.header("📂 CSV Data Upload")

data_file = st.file_uploader("Upload a CSV file", type=["csv"])
if data_file is not None:
    st.success("✅ File uploaded successfully!")
    with st.expander("View File Details"):
        file_details = {
            "File Name": data_file.name,
            "File Type": data_file.type,
            "File Size": f"{data_file.size:,} bytes"
        }
        st.json(file_details)

    df = pd.read_csv(data_file)
    st.subheader("📈 Preview of Uploaded Data:")
    st.dataframe(df)
else:
    st.info("No file uploaded yet. Please upload a CSV file.")

st.markdown("---")

# FORM SUBMISSION SECTION

st.header("📨 Submit Form")

with st.form(key="text_form"):
    text_input = st.text_input("Enter any text")
    submitted = st.form_submit_button("Submit")

if submitted:
    if text_input.strip() != "":
        st.success(f"You submitted: **{text_input}**")
    else:
        st.warning("Please enter some text before submitting.")

st.markdown("---")
st.caption("Kelompok 3 - Praktikum Visualisasi Data")