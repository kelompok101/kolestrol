import streamlit as st

# Define cholesterol values globally
cholesterol_values = {
    'daging dan unggas': {'daging kambing': 71, 'daging sapi': 70, 'daging ayam': 63, 'daging bebek': 65, 'daging babi': 80,
                          'daging anjing': 44.4, 'daging kalkun': 77, 'daging unta': 61},
    'ikan': {'ikan tuna': 45, 'ikan salmon': 48, 'ikan lele': 60, 'ikan mujair': 55, 'ikan tongkol': 60, 'ikan gurame': 66,
             'ikan patin': 39},
    'susu dan telur': {'susu sapi': 250, 'telur': 155, 'mentega': 215, 'yogurt': 45, 'kuning telur': 550, 'keju': 140},
    'makanan lainnya': {'sosis daging': 150, 'hamburger': 47, 'seblak': 121, 'bakso': 74, 'kebab': 79, 'coklat': 290}
}

# Function to calculate cholesterol
def calculate_cholesterol(jenis_makanan, nama_makanan, bobot):
    if jenis_makanan in cholesterol_values and nama_makanan in cholesterol_values[jenis_makanan]:
        cholesterol_per_100g = cholesterol_values[jenis_makanan][nama_makanan]
        total_cholesterol = (cholesterol_per_100g / 100) * bobot
        return total_cholesterol
    else:
        return f"Tidak ada data kolesterol untuk {nama_makanan} dalam kategori {jenis_makanan}."

# Streamlit application start
st.title('Cholesterol Calculator For Foods🥩')  

st.markdown('''Cholesterol Calculator For Foods digunakan untuk menghitung kalori pada bahan pangan hewani. 
Silahkan pilih Bahan pangan yang diinginkan  ☆: .｡. o(≧▽≦)o .｡.:☆''')
st.markdown('---')

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Menu', ['Perkenalan dan Penjelasan Singkat', 'Perhitungan Kolesterol'], default_index=0)

if selected == 'Perkenalan dan Penjelasan Singkat':
    st.markdown('KELOMPOK 7 (1E-PMIP):')
    st.write('''
    1. Kalisa Khatelya (2320532)
    2. Nayla Shafa Aulia (2320541)
    3. Selvi Wardayanti (2320555)
    4. Syifa Aprilya (2320558)
    5. Zikri (2320562)''')

    st.header('💡 Tahukah Anda??')
    st.write('''
            Bahwa sama sekali tidak ada kolesterol dalam makanan nabati apa pun, 
            termasuk sereal, buah-buahan, sayuran, dan biji-bijian? 
            Kolesterol hanya berasal dari makanan hewani🐓🐄🐟''')
    st.write('''
                Kalkulator kolesterol adalah alat yang dapat membantu kita untuk mengetahui berapa 
                banyak kolesterol dalam makanan yang kita makan. Dengan kalkulator kolesterol ini, 
                kita dapat dengan cepat menentukan asupan kolesterol harian dan melacaknya. Seseorang 
                yang berisiko terkena penyakit jantung harus menjaga konsumsi kolesterol hariannya 
                sekitar 200 mg.''')

if selected == 'Perhitungan Kolesterol':
    jenis_makanan = st.selectbox('Pilih Jenis Bahan Pangan', list(cholesterol_values.keys()))
    nama_makanan = st.selectbox('Pilih jenis makanan', list(cholesterol_values[jenis_makanan].keys()))
    bobot = st.number_input('Masukkan bobot yang diinginkan (gram)', min_value=1, value=100)

    if st.button('Hitung Kolesterol'):
        total_cholesterol = calculate_cholesterol(jenis_makanan, nama_makanan, bobot)
        if isinstance(total_cholesterol, str):
            st.error(total_cholesterol)
        else:
            st.success(f'Perkiraan kolesterol dalam {nama_makanan} ({bobot}g): {total_cholesterol} mg')