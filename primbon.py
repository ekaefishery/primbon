from datetime import datetime
import streamlit as st

st.title ("Primbon")

nama = st.text_input("masukan nama kamu")

tl = st.date_input("masukan tanggal lahir",min_value=datetime.strptime('1945-01-01','%Y-%m-%d'))

hari_lahir_num = tl.isoweekday()
hari = {
   1:'Senin',
   2:'Selasa',
   3:'Rabu',
   4:'Kamis',
   5:'Jumat',
   6:'Sabtu',
   7:'Minggu' 
}

watak = {
   1:"""Baik Hati""",
   2:"""Suka Menolong""",
   3:"""Rajin Menabung""",
   4:"""Suka Makan""",
   5:"""Suka Main""",
   6:"""Suka Tidur""",
   7:"""Pembelajar""" 
}

st.subheader(f'Hello, {nama}!')
st.subheader(f'Kamu Lahir Hari, {hari[hari_lahir_num]}!')
st.write(watak[hari_lahir_num])


