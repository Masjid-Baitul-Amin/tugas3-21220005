import streamlit as st
import pandas as pd

# URL dataset dari GitHub (ganti dengan URL dataset Anda)
url = "https://raw.githubusercontent.com/ffzs/dataset/refs/heads/master/insurance.csv"

# Fungsi untuk memuat dataset
def load_data():
    data = pd.read_csv(url)
    return data

# Memuat data
data = load_data()

# Tampilkan judul aplikasi
st.title("Menampilkan 5 Kolom Dataset dari GitHub")

# Pilihan kolom yang ingin ditampilkan
columns = data.columns.tolist()  # Mengambil nama-nama kolom
selected_columns = st.multiselect("Pilih 5 Kolom untuk Ditampilkan", columns, default=columns[:5])

# Menampilkan data jika ada kolom yang dipilih
if selected_columns:
    st.write("Data yang dipilih:")
    st.write(data[selected_columns])

    # Membuat grafik terpisah untuk setiap kolom yang dipilih
    for column in selected_columns:
        st.write(f"Grafik untuk kolom: {column}")
        st.line_chart(data[[column]])
else:
    st.warning("Pilih kolom dari dataset untuk ditampilkan.")
