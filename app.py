import streamlit as st
import os
#from dotenv import load_dotenv
import random

import requests

'''
# Le WaGAN - Célébrités
'''

#load_dotenv()


st.markdown('''
  Projet du Wagon - batch 995
''')


with st.sidebar:

    st.markdown('''Les vecteurs propres influent sur les paramètres des images générées''')


    # initializing with a random number
    #if "rn" not in st.session_state:
    #    st.session_state["rn"] = random.randint(1,100)

    #def change_number():
    #    st.session_state["rn"] = random.randint(1,100)
    #    return

    #st.button("Génération d'une nouvelle image", on_click=change_number)
    
    seed = st.number_input('choisir un seed', min_value=1, max_value=100)

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

url = 'https://lewagan-docker-celeb-vl3hfwrb3a-ez.a.run.app/image?'

res = requests.get(url, params=params_api)
res_init = requests.get(url, params=params_init)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(" ")

with col2:
  
  
    if res_init.status_code == 200:
                ### Display the image returned by the API
        st.image(res_init.content)
    else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res_init.status_code, res_init.content)
    
    if res.status_code == 200:
                ### Display the image returned by the API
        st.image(res.content)
    else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

with col3:
    st.markdown(" ")

