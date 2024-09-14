import streamlit as st
from streamlit_lottie import st_lottie
import json

# Função para carregar animação Lottie a partir de um arquivo local
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Carregar animação Lottie a partir de um arquivo local (substitua o caminho pelo arquivo que você baixou)
lottie_animation = load_lottiefile("path_to_your_downloaded_animation.json")

# Exibir a animação Lottie
st_lottie(lottie_animation, height=300, key="clothing_change")

# Listas de atitudes
old_attitudes = ["Selecione uma atitude","Orgulho", "Ira", "Egoísmo", "Impaciência", "Mentira"]
new_attitudes = ["Selecione uma atitude","Compaixão", "Bondade", "Humildade", "Paciência", "Perdão", "Amor"]

# Inicializando a lista de escolhas
if 'old_choice' not in st.session_state:
    st.session_state.old_choice = []
if 'new_choice' not in st.session_state:
    st.session_state.new_choice = []
if 'reflections' not in st.session_state:
    st.session_state.reflections = []

# Título e Introdução
st.title("Troca de Roupas Espirituais")
st.write("""
Nesta atividade, você irá refletir sobre suas atitudes e fazer uma troca espiritual, 
despindo-se das práticas antigas e revestindo-se de novas atitudes em Cristo.
""")

# Escolha de atitudes velhas
st.subheader("Escolha uma atitude antiga para se despir:")
old_choice = st.selectbox("Atitudes Velhas", old_attitudes)
if st.button("Adicionar atitude antiga"):
    st.session_state.old_choice.append(old_choice)
    st.success(f'Você adicionou "{old_choice}" às roupas velhas.')

# Escolha de atitudes novas
st.subheader("Escolha uma atitude nova para se revestir:")
new_choice = st.selectbox("Atitudes Novas", new_attitudes)
if st.button("Adicionar atitude nova"):
    st.session_state.new_choice.append(new_choice)
    st.success(f'Você se revestiu com "{new_choice}".')

# Exibir escolhas
st.subheader("Suas escolhas:")
st.write("Atitudes Velhas:", ", ".join(st.session_state.old_choice))
st.write("Atitudes Novas:", ", ".join(st.session_state.new_choice))

# Reflexão
st.subheader("Compartilhe como pode vestir essa nova atitude no dia a dia")
