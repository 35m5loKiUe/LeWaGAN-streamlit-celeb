import streamlit as st
import os
#from dotenv import load_dotenv
import random

import requests

'''
# Le WaGAN
'''

#load_dotenv()


st.markdown('''
  Projet du Wagon - batch 995
''')


with st.sidebar:

    st.markdown('''Les vecteurs propres influent sur les paramètres des images générées''')


    # initializing with a random number
    if "rn" not in st.session_state:
        st.session_state["rn"] = random.randint(1,100)

    def change_number():
        st.session_state["rn"] = random.randint(1,100)
        return

    st.button("Génération d'une nouvelle image", on_click=change_number)
    seed = st.session_state.rn

    v1 = st.slider('vecteur propre 1', min_value=1, max_value=10)
    v2 = st.slider('vecteur propre 2', min_value=1, max_value=10)
    v3 = st.slider('vecteur propre 3', min_value=1, max_value=10)
    v4 = st.slider('vecteur propre 4', min_value=1, max_value=10)
    v5 = st.slider('vecteur propre 5', min_value=1, max_value=10)

params_api = {'v1':v1,
          'v2':v2,
          'v3':v3,
          'v4':v4,
          'v5':v5,
          'seed':seed
}

params_init = {'v1':1,
          'v2':1,
          'v3':1,
          'v4':1,
          'v5':1,
          'seed':seed
}

url = 'https://lewagandocker-vl3hfwrb3a-ew.a.run.app/image?'

res = requests.get(url, params=params_api)
res_init = requests.get(url, params=params_init)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(" ")

with col2:
    if res_init.status_code == 200:
                ### Display the image returned by the API
        st.image(res_init.content, caption="Image générée par l'IA ☝️")
    else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res_init.status_code, res_init.content)

with col3:
    st.markdown(" ")


with col4:
    if res.status_code == 200:
                ### Display the image returned by the API
        st.image(res.content, caption="Image générée par l'AI, avec les vecteurs propres associés ☝️")
    else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

with col5:
    st.markdown(" ")
