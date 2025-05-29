
# Paleiskite skriptą su Streamlit komanda:
# Atidarykite terminalą (arba komandų eilutę).
# Eikite į katalogą, kuriame yra jūsų skriptas (testas.py).
# Pavyzdziui:
# cd d:/AI studijos/1 tarpinis/
# Paleiskite skriptą terminale parasydami streamlit run testas.py
# Po to Streamlit automatiškai atidarys naršyklę su jūsų programa (paprastai adresu http://localhost:8501).

import streamlit as st

st.title("Sveikinimas")
vardas = st.text_input("Įveskite vardą:")
if st.button("Spausk!"):
    st.write(f"Labas, {vardas}!")