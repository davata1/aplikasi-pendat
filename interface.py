import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
form input data diabetes :
""")

#Fractional Knapsack Problem
#Getting input from user
hamil = int(st.number_input("Kehamilan : ",0))
glukosa = int(st.number_input("Glukosa : ",0))
tekananDarah = int(st.number_input("Tekanan Darah : ",0))
tebalKulit = int(st.number_input("Ketebalan Kulit : ",0))
insulin = int(st.number_input("Insulin : ",0))
bmi = int(st.number_input("BMI : ",0))
jenisDiabetes = int(st.number_input("Jenis Diabetes : ",0))
umur = int(st.number_input("Umur : ",0))
hasil = int(st.number_input("hasil : ",0))

submit = st.button("submit")


if submit:
    st.info("Jadi,dinyakataan . ")


