import streamlit as st

st.write("""
# Aplikasi menghitung luas segitiga
Ini adalah aplikasi sederhana menghitung luas segitiga""")

alas = st.number_input("Input Alas", 0)
tinggi = st.number_input("Input Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas segitiga adalah {luas}")
    st.snow()