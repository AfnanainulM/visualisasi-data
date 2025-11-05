import streamlit as st

st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 1: Text Elements")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi - 0110222084
2. Faqih Al Fauzan - 0110222152
3. Afnan Ainul Mardhiyyah - 0110222128
""")

st.header("Ini header")
st.subheader("ini sub header")
st.text("Ini text biasa")
st.markdown("**ini text bold** dan *ini text italic*")
st.markdown("""
- baris 1
1. baris 2
2. ini menggunakan markdown multibaris
* baris 3
* ini menggunakan markdown multi baris
""")
st.caption("ini caption")
st.title("ini judul")

# Bagian 2: Menampilkan rumus

st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''')

# Bagian 3: Displaying Code

st.header("Displaying Code")
st.subheader("Python Code")

# Simpan ke Variable

code = '''
def hello():
    print("Hello, Streamlit!")
'''

# st.code() untuk menampilkan potongan kode dengan format rapih
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
    public static void main(String arg[]) {
        System.out.println("Hello World!");
    }
}
""", language='java')

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome Guest!"); // kesalahan ketik (addalert)
    // sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
    // menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')